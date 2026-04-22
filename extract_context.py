import os
from pypdf import PdfReader
import docx

def extract_pdf(file_path):
    text = f"--- START OF {os.path.basename(file_path)} ---\n"
    with open(file_path, 'rb') as f:
        reader = PdfReader(f)
        for i, page in enumerate(reader.pages):
            text += f"\n--- Page {i+1} ---\n"
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    text += f"\n--- END OF {os.path.basename(file_path)} ---\n"
    return text

def extract_docx(file_path):
    text = f"--- START OF {os.path.basename(file_path)} ---\n"
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        text += f"[Failed to extract word doc: {e}]\n"
    text += f"\n--- END OF {os.path.basename(file_path)} ---\n"
    return text

def extract_all(input_dir, output_context_dir):
    if not os.path.exists(output_context_dir):
        os.makedirs(output_context_dir)
    
    import sys
    
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        if not os.path.isfile(file_path):
            continue
        
        base_name = os.path.splitext(filename)[0]
        ext = os.path.splitext(filename)[1].lower()
        
        try:
            if ext == '.pdf':
                print(f"Extracting PDF: {filename}...", file=sys.stderr)
                text = extract_pdf(file_path)
                output_path = os.path.join(output_context_dir, f"{base_name}.md")
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Extracted to {output_path}", file=sys.stderr)
            elif ext in ['.docx', '.doc']:
                print(f"Extracting DOCX: {filename}...", file=sys.stderr)
                text = extract_docx(file_path)
                output_path = os.path.join(output_context_dir, f"{base_name}.md")
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Extracted to {output_path}", file=sys.stderr)
        except Exception as e:
            print(f"Error extracting {filename}: {e}", file=sys.stderr)
    
    print("Extraction complete.", file=sys.stderr)

if __name__ == "__main__":
    import sys
    
    input_dir = "input"
    output_context_dir = "context"
    
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        print(f"Created input directory: {input_dir}", file=sys.stderr)
        print("Place your PDF/DOCX files there and run again.", file=sys.stderr)
    else:
        extract_all(input_dir, output_context_dir)
