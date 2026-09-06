#!/usr/bin/env python3
"""Render small README previews from the published PDFs; preserve source exports."""
from pathlib import Path
import pymupdf


def main():
    base = Path(__file__).resolve().parents[1] / 'examples/perturbation-overview'
    output = base / 'previews'
    output.mkdir(exist_ok=True)
    for design in range(1, 4):
        for palette in ('restrained', 'vivid'):
            stem = f'design-{design}-{palette}'
            with pymupdf.open(base / 'figures' / f'{stem}.pdf') as doc:
                if len(doc) != 1:
                    raise ValueError(f'{stem}: expected one-page PDF')
                scale = 720 / doc[0].rect.width
                pix = doc[0].get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=False)
                target = output / f'{stem}.jpg'
                target.write_bytes(pix.tobytes('jpeg', jpg_quality=85))
                print(f'{target.name}: {target.stat().st_size:,} bytes')


if __name__ == '__main__':
    main()
