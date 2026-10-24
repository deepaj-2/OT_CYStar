```python
#!/usr/bin/env python3

import os
import sys
import json
import subprocess

def convert_md_to_pdf(md_file, pdf_file):

    os.makedirs(os.path.dirname(pdf_file), exist_ok=True)

    cmd = [
        'pandoc',
        md_file,
        '-o',
        pdf_file,
        '--from=gfm',
        '--pdf-engine=xelatex',
        '-V', 'geometry:margin=1in',
        '-V', 'fontsize=11pt',
        '--toc',
        '--toc-depth=3'
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(result.stderr)
        return False

    return True


def main():

    files = json.loads(sys.argv[1])
    watermark = sys.argv[2]

    for md_file in files:

        base = os.path.basename(md_file).replace(".md", ".pdf")
        pdf = f"generated-pdfs/{base}"

        if not convert_md_to_pdf(md_file, pdf):
            continue

        subprocess.run([
            sys.executable,
            "scripts/watermark.py",
            pdf,
            pdf,
            watermark
        ])


if __name__ == "__main__":
    main()
4. watermark.py
Create:

scripts/watermark.py
Example:

from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
import sys
import io


def create_watermark(text):

    packet = io.BytesIO()

    c = canvas.Canvas(packet)
    c.drawString(100, 10, text)
    c.save()

    packet.seek(0)

    return PdfReader(packet)


def add_watermark(input_pdf, output_pdf, text):

    watermark = create_watermark(text)

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        page.merge_page(watermark.pages[0])
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)


if __name__ == "__main__":

    add_watermark(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )