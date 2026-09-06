#!/usr/bin/env python3
"""Make a three-panel review PNG from final vector PDFs at equal physical width."""
import argparse
from pathlib import Path
import sys

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('pdfs',nargs=3);p.add_argument('--out',required=True);p.add_argument('--dpi',type=int,default=144);a=p.parse_args()
    try:
        import pymupdf as fitz
    except ImportError:
        try:import fitz
        except ImportError:sys.exit('Install pymupdf for PDF preview rendering')
    docs=[fitz.open(x) for x in a.pdfs]
    if not all(len(d)==1 for d in docs):sys.exit('Each version must be a one-page PDF')
    widths=[d[0].rect.width for d in docs]
    if max(widths)-min(widths)>.6:sys.exit('Normalize all PDFs to the same physical width before comparison')
    width=widths[0];gap=18;header=28;maxh=max(d[0].rect.height for d in docs)
    result=fitz.open();page=result.new_page(width=3*width+4*gap,height=maxh+header+2*gap)
    for i,d in enumerate(docs):
        x=gap+i*(width+gap);page.insert_text((x,gap+11),f'Version {i+1}',fontsize=10,color=(.2,.3,.35))
        rect=fitz.Rect(x,gap+header,x+width,gap+header+d[0].rect.height);page.show_pdf_page(rect,d,0)
    target=Path(a.out);target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():sys.exit('Refusing overwrite; choose a new comparison path')
    page.get_pixmap(matrix=fitz.Matrix(a.dpi/72,a.dpi/72)).save(target)
    print(target)
if __name__=='__main__':main()
