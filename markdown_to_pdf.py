import os
import re
import glob
import traceback
import argparse
from datetime import datetime
from fpdf import FPDF
from markdown2 import markdown

CONFIG = {
    "miejscowosc": "Warszawa",
    "autor": "Jan Kowalski",
    "wyrazy_zaufania": "Z poważaniem",
    "font_path": "/Library/Fonts/Arial Unicode.ttf"
}

def load_config(config_path=".config"):
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    CONFIG[key.strip()] = value.strip()
    return CONFIG

def get_latest_md_file(directory):
    list_of_files = glob.glob(os.path.join(directory, '*.md'))
    if not list_of_files:
        return None
    return max(list_of_files, key=os.path.getmtime)

def convert_md_to_pdf(md_path, config=None):
    config = config or CONFIG
    print(f"Loading {md_path}...")
    
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    html_content = markdown(md_text)
    html_content = html_content.replace('<hr />', '<hr>')

    pdf = FPDF()
    pdf.add_page()

    font_path = config.get("font_path", "/Library/Fonts/Arial Unicode.ttf")
    if os.path.exists(font_path):
        pdf.add_font("Arial", "", font_path)
        pdf.add_font("Arial", "B", font_path)
        pdf.add_font("Arial", "I", font_path)
        pdf.add_font("Arial", "BI", font_path)
        pdf.set_font("Arial", size=11)
    else:
        print(f"Warning: Font {font_path} not found. Falling back to Helvetica.")
        pdf.set_font("Helvetica", size=11)

    pdf.set_author(config.get("autor", "Jan Kowalski"))
    pdf.set_title(os.path.basename(md_path))

    pdf.write_html(html_content)
    
    pdf_path = md_path.replace('.md', '.pdf')
    pdf.output(pdf_path)
    print(f"Successfully generated: {pdf_path}")
    return pdf_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown to PDF")
    parser.add_argument("file", nargs="?", help="Path to .md file (default: latest in output/)")
    parser.add_argument("--config", default=".config", help="Path to config file")
    args = parser.parse_args()
    
    config = load_config(args.config)
    
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    md_path = args.file or get_latest_md_file(output_dir)
    
    if md_path:
        try:
            convert_md_to_pdf(md_path, config)
        except Exception as e:
            print(f"Critical error during conversion: {e}")
            traceback.print_exc()
    else:
        print("No .md files found in the output directory.")
