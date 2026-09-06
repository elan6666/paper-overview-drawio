#!/usr/bin/env python3
"""Compile native paper-overview scenes; validate scientific parity; export and audit."""
import argparse
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

SHAPES = {
    'rect': 'shape=rectangle;rounded=0;',
    'roundrect': 'shape=rectangle;rounded=1;arcSize=10;',
    'ellipse': 'shape=ellipse;',
    'text': 'shape=label;strokeColor=none;fillColor=none;',
    'cylinder': 'shape=cylinder;',
    'triangle': 'shape=triangle;',
    'hexagon': 'shape=hexagon;',
}
KINDS = {'data', 'conditioning', 'loss', 'update'}
FINGERPRINT = ('flow_direction', 'panel_structure', 'focal_point', 'detail_strategy')

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def write(path, value):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def require(ok, message):
    if not ok:
        raise ValueError(message)

def indexed(items, context):
    ids = [x['id'] for x in items]
    require(len(ids) == len(set(ids)), f'{context}: duplicate IDs')
    require(all(isinstance(i, str) and i and i not in ('0', '1') for i in ids), f'{context}: invalid ID')
    return dict(zip(ids, items))

def color(value):
    require(value == 'none' or re.fullmatch(r'#[0-9A-Fa-f]{6}', value), f'Invalid color: {value}')
    return value

def box(item):
    values = tuple(float(item[k]) for k in ('x', 'y', 'w', 'h'))
    require(all(math.isfinite(v) for v in values), 'Non-finite geometry')
    require(values[2] > 0 and values[3] > 0, f"{item['id']}: nonpositive size")
    return values

def inside(child, parent, pad=0):
    x,y,w,h=child; a,b,c,d=parent
    return x>=a+pad and y>=b+pad and x+w<=a+c-pad and y+h<=b+d-pad

def validate(contract, scene):
    require(contract.get('schema_version') == scene.get('schema_version') == 1, 'schema_version must be 1')
    require(contract.get('paper') and contract.get('message'), 'Paper/message required')
    cn=indexed(contract['nodes'], 'contract nodes'); ce=indexed(contract['edges'], 'contract edges')
    require(cn, 'Empty paper graph')
    for n in cn.values(): require(n.get('label') and n.get('evidence'), f"{n['id']}: label/evidence required")
    for e in ce.values():
        require(e['source'] in cn and e['target'] in cn, f"{e['id']}: unknown canonical endpoint")
        require(e.get('kind') in KINDS and e.get('evidence'), f"{e['id']}: kind/evidence required")
    canvas=scene['canvas']; w=float(canvas['width']);h=float(canvas['height'])
    require(w>0 and h>0 and math.isfinite(w+h), 'Invalid canvas')
    width_mm=float(contract['width_mm']); floor=float(contract.get('minimum_font_pt',7))
    require(width_mm>0 and floor>0, 'Invalid physical size/font floor')
    pt_per_px=width_mm/25.4*72/w
    groups=indexed(scene.get('groups',[]),'groups'); ns=indexed(scene['nodes'],'scene nodes'); es=indexed(scene['edges'],'scene edges')
    allids=list(groups)+list(ns)+list(es)
    require(len(allids)==len(set(allids)), 'IDs collide across object types')
    seen_n=set();seen_e=set(); notes=[]
    for g in groups.values():
        require(inside(box(g),(0,0,w,h)), f"{g['id']}: group outside canvas")
        require(float(g.get('font_size',17))*pt_per_px>=floor, f"{g['id']}: heading too small at final width")
    for n in ns.values():
        require(n.get('shape','rect') in SHAPES, f"{n['id']}: non-native shape")
        require(not any(k in n for k in ('image','svg','url','style')), f"{n['id']}: external/raw artwork forbidden")
        require(inside(box(n),(0,0,w,h)), f"{n['id']}: outside canvas")
        if n.get('group'):
            require(n['group'] in groups, f"{n['id']}: unknown group")
            require(inside(box(n),box(groups[n['group']]),4), f"{n['id']}: group containment failed")
            require(n['y']>=groups[n['group']]['y']+32, f"{n['id']}: overlaps group heading band")
        sid=n.get('semantic_id')
        if sid:
            require(sid in cn, f"{n['id']}: unsupported scientific entity")
            require(n.get('label')==cn[sid]['label'] or n.get('label_override_reason'), f"{n['id']}: changed label without reason")
            seen_n.add(sid)
        else: require(n.get('role')=='decoration', f"{n['id']}: semantic_id or decoration role required")
        label=n.get('label','');font=float(n.get('font_size',16))
        require(font>0 and math.isfinite(font), f"{n['id']}: invalid font")
        if label:
            require(font*pt_per_px>=floor, f"{n['id']}: font {font*pt_per_px:.2f} pt below floor")
            # Estimate only; final rendered inspection remains mandatory.
            max_units=max(sum(1 if ord(c)>255 else .52 for c in line) for line in label.split('\n'))
            require(max_units*font<=n['w']-8, f"{n['id']}: likely horizontal text overflow; add line breaks or widen")
            require(len(label.split('\n'))*font*1.2<=n['h']-6, f"{n['id']}: likely vertical text overflow")
    for e in es.values():
        require(e['source'] in ns and e['target'] in ns, f"{e['id']}: missing endpoint")
        kind=e.get('kind','data');sid=e.get('semantic_id')
        if kind=='callout': require(not sid, f"{e['id']}: callout must not claim a computational edge")
        else:
            require(sid in ce, f"{e['id']}: unsupported scientific edge")
            ref=ce[sid]
            require(kind==ref['kind'], f"{e['id']}: changed edge kind")
            require(ns[e['source']].get('semantic_id')==ref['source'] and ns[e['target']].get('semantic_id')==ref['target'], f"{e['id']}: changed scientific direction/endpoints")
            seen_e.add(sid)
        for p in e.get('points',[]): require(len(p)==2 and 0<=p[0]<=w and 0<=p[1]<=h, f"{e['id']}: waypoint out of canvas")
        for key in ('exit','entry'):
            if key in e: require(len(e[key])==2 and all(0<=v<=1 for v in e[key]), f"{e['id']}: invalid anchor")
        if e.get('label'): require(float(e.get('font_size',15))*pt_per_px>=floor, f"{e['id']}: edge label too small")
    require(seen_n==set(cn), 'Missing semantic nodes: '+str(sorted(set(cn)-seen_n)))
    require(seen_e==set(ce), 'Missing semantic edges: '+str(sorted(set(ce)-seen_e)))
    fp=scene.get('fingerprint',{})
    require(all(fp.get(k) for k in FINGERPRINT), 'Incomplete composition fingerprint')
    return {'status':'pass','native_nodes':len(ns),'scientific_nodes':len(cn),'scientific_edges':len(ce),'width_mm':width_mm,'font_scale_pt_per_px':pt_per_px,'limits':'Static geometry/semantic checks only; rendered review required.'}

def compile_scene(contract, scene, output):
    report=validate(contract,scene);w=scene['canvas']['width'];h=scene['canvas']['height']
    root=ET.Element('mxfile',{'host':'app.diagrams.net','type':'device','version':'31.4.2'})
    diagram=ET.SubElement(root,'diagram',{'id':'overview','name':scene['name']})
    model=ET.SubElement(diagram,'mxGraphModel',{'dx':str(w),'dy':str(h),'grid':'0','page':'1','pageScale':'1','pageWidth':str(w),'pageHeight':str(h),'math':'0','background':'#FFFFFF'})
    cells=ET.SubElement(model,'root');ET.SubElement(cells,'mxCell',{'id':'0'});ET.SubElement(cells,'mxCell',{'id':'1','parent':'0'})
    groups={g['id']:g for g in scene.get('groups',[])}
    for g in groups.values():
        s=f"swimlane;html=0;startSize=30;horizontal=1;rounded=0;collapsible=0;fillColor={color(g.get('fill','#F6F8FA'))};swimlaneFillColor={color(g.get('fill','#F6F8FA'))};strokeColor={color(g.get('stroke','#D9E1E7'))};fontColor=#263442;fontStyle=1;fontSize={g.get('font_size',17)};align=left;spacingLeft=12;"
        cell=ET.SubElement(cells,'mxCell',{'id':g['id'],'parent':'1','vertex':'1','value':g.get('label',''),'style':s})
        ET.SubElement(cell,'mxGeometry',{'x':str(g['x']),'y':str(g['y']),'width':str(g['w']),'height':str(g['h']),'as':'geometry'})
    # Edges before nodes, so strokes don't obscure labels.
    for e in scene['edges']:
        kind=e.get('kind','data');dashed=e.get('dashed',kind!='data');s='html=0;rounded=0;strokeWidth=1.3;'
        s+=('edgeStyle=orthogonalEdgeStyle;orthogonalLoop=1;jettySize=auto;' if e.get('routing')!='straight' else '')
        s+=f"endArrow={'none' if kind=='callout' else 'block'};endFill=1;endSize=7;strokeColor={color(e.get('stroke','#4D6572'))};dashed={int(dashed)};fontSize={e.get('font_size',15)};fontColor=#334B58;labelBackgroundColor=#FFFFFF;"
        for key in ('exit','entry'):
            if key in e:s+=f"{key}X={e[key][0]};{key}Y={e[key][1]};{key}Dx=0;{key}Dy=0;"
        cell=ET.SubElement(cells,'mxCell',{'id':e['id'],'parent':'1','edge':'1','source':e['source'],'target':e['target'],'value':e.get('label',''),'style':s})
        geo=ET.SubElement(cell,'mxGeometry',{'relative':'1','as':'geometry'})
        if e.get('points'):
            pts=ET.SubElement(geo,'Array',{'as':'points'})
            for x,y in e['points']:ET.SubElement(pts,'mxPoint',{'x':str(x),'y':str(y)})
    for n in scene['nodes']:
        shape=n.get('shape','rect');s=SHAPES[shape]+'html=0;whiteSpace=nowrap;overflow=visible;align=center;verticalAlign=middle;spacing=4;'
        if shape!='text':s+=f"fillColor={color(n.get('fill','#FFFFFF'))};strokeColor={color(n.get('stroke','#526A77'))};"
        s+=f"fontFamily=Helvetica;fontSize={n.get('font_size',16)};fontColor={color(n.get('font_color','#263442'))};fontStyle={1 if n.get('bold') else 0};strokeWidth=1;rotation={float(n.get('rotation',0))};"
        parent=n.get('group','1');x,y=n['x'],n['y']
        if parent!='1':x-=groups[parent]['x'];y-=groups[parent]['y']
        cell=ET.SubElement(cells,'mxCell',{'id':n['id'],'parent':parent,'vertex':'1','value':n.get('label',''),'style':s})
        ET.SubElement(cell,'mxGeometry',{'x':str(x),'y':str(y),'width':str(n['w']),'height':str(n['h']),'as':'geometry'})
    p=Path(output);p.parent.mkdir(parents=True,exist_ok=True)
    require(not p.exists(),f'Refusing overwrite: {p}; use a revisioned directory')
    ET.indent(root);ET.ElementTree(root).write(p,encoding='utf-8',xml_declaration=True)
    report.update({'drawio_sha256':sha(p),'contract_sha256':hashlib.sha256(json.dumps(contract,sort_keys=True).encode()).hexdigest()})
    write(p.with_suffix('.structure.json'),report)
    return report

def executable():
    candidate=os.environ.get('DRAWIO_PATH')
    if candidate:
        found=shutil.which(candidate) or (candidate if Path(candidate).is_file() else None)
        require(found,'DRAWIO_PATH not found');return str(found)
    mac=Path('/Applications/draw.io.app/Contents/MacOS/draw.io')
    found=str(mac) if mac.is_file() else shutil.which('drawio') or shutil.which('draw.io')
    require(found,'Draw.io Desktop unavailable; install or set DRAWIO_PATH');return found

def export_file(source,outdir,contract):
    try:import fitz
    except ImportError:raise ValueError("NOT AUDITABLE: install pymupdf for physical vector-PDF export")
    target_mm=float(contract["width_mm"])
    require(target_mm>0,"Invalid target width")
    source=Path(source).resolve();require(source.exists(),'Missing drawio source');out=Path(outdir).resolve();out.mkdir(parents=True,exist_ok=True)
    app=executable();outputs=[]
    with tempfile.TemporaryDirectory(prefix='overview-drawio-profile-') as profile:
        for fmt in ('png','svg','pdf'):
            target=out/(source.stem+'.'+fmt);require(not target.exists(),f'Refusing overwrite: {target}')
            cmd=[app,f'--user-data-dir={profile}','--disable-update','-x','-f',fmt,'--theme','light','-o',str(target),str(source)]
            if fmt in ('png','svg'):cmd+=['--border','12']
            if fmt=='png':cmd+=['--scale','2']
            if fmt=='pdf':cmd+=['--crop']
            r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
            require(r.returncode==0 and target.exists() and target.stat().st_size>100,f'Export failed {fmt}: {r.stdout}\n{r.stderr}')
            if fmt=='pdf':
                original=fitz.open(target); scaled=fitz.open()
                for page in original:
                    width=target_mm/25.4*72; height=page.rect.height*width/page.rect.width
                    new=scaled.new_page(width=width,height=height)
                    new.show_pdf_page(new.rect,original,page.number)
                temp=target.with_suffix('.normalized.pdf');scaled.save(temp);scaled.close();original.close();temp.replace(target)
            if fmt=='svg':
                svg=ET.parse(target); sr=svg.getroot()
                view=sr.attrib.get('viewBox','').split()
                if len(view)==4:ratio=float(view[3])/float(view[2])
                else:
                    num=lambda v:float(re.search(r'[0-9.]+',v).group())
                    ratio=num(sr.attrib['height'])/num(sr.attrib['width'])
                sr.set('width',f'{target_mm}mm');sr.set('height',f'{target_mm*ratio}mm')
                svg.write(target,encoding='utf-8',xml_declaration=True)
            outputs.append({'file':str(target),'sha256':sha(target)})
    result={'status':'exported','files':outputs,'visual_review':'not-reviewed'};write(out/(source.stem+'.export.json'),result);return result

def compare(contract,selection,scenes):
    require(len(scenes)==3,'Exactly three scenes required')
    require(selection['selected_styles']==[s['style_id'] for s in scenes],'Style selection/order mismatch')
    checks=[validate(contract,s) for s in scenes];pairs=[]
    for a,b in itertools.combinations(scenes,2):
        changes=[k for k in FINGERPRINT if a['fingerprint'][k]!=b['fingerprint'][k]]
        geometry=lambda s:sorted((n.get('semantic_id',''),n['x'],n['y'],n['w'],n['h']) for n in s['nodes'])
        same_geometry=geometry(a)==geometry(b)
        pairs.append({'versions':[a['name'],b['name']],'declared_differences':changes,'same_geometry':same_geometry,'review_note':'Judge visual distinction from renders, not metadata counts.'})
    return {'status':'pass','versions':checks,'pairs':pairs,'limits':'Declared fingerprints need verification against renders.'}

def audit(pdf,svg,out,floor,width_mm):
    try:import fitz
    except ImportError:raise ValueError('NOT AUDITABLE: install pymupdf for this Python interpreter')
    d=fitz.open(pdf);require(len(d)==1,'Expected one-page figure PDF')
    texts=[];fonts=[];images=[]
    for p in d:
        images.extend(p.get_images(full=True))
        for b in p.get_text('dict')['blocks']:
            for line in b.get('lines',[]):
                for span in line['spans']:
                    if span['text'].strip():texts.append(span['text']);fonts.append(span['size'])
    tree=ET.parse(svg);forbidden=[]
    for el in tree.iter():
        tag=el.tag.split('}')[-1]
        if tag in ('image','foreignObject'):forbidden.append(tag)
        if any(re.search(r'data:image/(png|jpe?g|webp|gif)|https?://',str(v),re.I) for k,v in el.attrib.items() if k.endswith('href')):forbidden.append('external/raster href')
    errors=[]
    actual_width=d[0].rect.width/72*25.4
    if abs(actual_width-width_mm)>.2:errors.append('PDF physical width differs from contract')
    svg_width=tree.getroot().get('width','')
    if svg_width != f'{float(width_mm)}mm':errors.append('SVG physical width differs from contract')
    if images:errors.append('PDF contains raster image objects')
    if forbidden:errors.append('SVG contains unsupported image/foreignObject/external artwork')
    if not texts:errors.append('PDF contains no extractable text')
    if fonts and min(fonts)<floor-.1:errors.append('Rendered font below requested floor')
    result={'status':'fail' if errors else 'pass','pdf_sha256':sha(pdf),'svg_sha256':sha(svg),'pdf_raster_images':len(images),'svg_forbidden':forbidden,'min_font_pt':min(fonts) if fonts else None,'page_width_mm':d[0].rect.width/72*25.4,'text_spans':len(texts),'errors':errors,'visual_review':'not-reviewed','limits':'Vector/text audit only, not collision or scientific verification.'}
    write(out,result);return result

def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
    b=sub.add_parser('build');b.add_argument('contract');b.add_argument('scene');b.add_argument('--out',required=True)
    e=sub.add_parser('export');e.add_argument('drawio');e.add_argument('--out-dir',required=True);e.add_argument('--contract',required=True)
    c=sub.add_parser('compare');c.add_argument('contract');c.add_argument('selection');c.add_argument('scenes',nargs=3);c.add_argument('--out')
    a=sub.add_parser('audit');a.add_argument('pdf');a.add_argument('svg');a.add_argument('--out',required=True);a.add_argument('--contract',required=True)
    args=p.parse_args()
    try:
        if args.command=='build':r=compile_scene(read(args.contract),read(args.scene),args.out)
        elif args.command=='export':r=export_file(args.drawio,args.out_dir,read(args.contract))
        elif args.command=='compare':
            r=compare(read(args.contract),read(args.selection),[read(x) for x in args.scenes])
            if args.out:write(args.out,r)
        else:
            ct=read(args.contract);r=audit(args.pdf,args.svg,args.out,float(ct.get('minimum_font_pt',7)),float(ct['width_mm']))
        print(json.dumps(r,ensure_ascii=False,indent=2));return 1 if r.get('status')=='fail' else 0
    except (ValueError,KeyError,FileNotFoundError,ET.ParseError,subprocess.TimeoutExpired) as exc:
        print(str(exc),file=sys.stderr);return 1

if __name__=='__main__':sys.exit(main())
