import os
import string
import fitz  # PyMuPDF

pdf_file_path = r'C:\Users\dzont\Music\pdf\temporal.pdf'
output_directory = r'C:\Users\dzont\Music\pdf\JPGTEACHERS'
os.makedirs(output_directory, exist_ok=True)

pdf_document = fitz.open(pdf_file_path)

valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

for i in range(pdf_document.page_count):
    page = pdf_document.load_page(i)
    text = page.get_text("text")
    lines = text.split("\n")
    if len(lines) > 1:
        page_name = lines[1].strip()  # Changed from lines[2] to lines[1]
        cleaned_page_name = ''.join(c for c in page_name if c in valid_chars)
        
        file_name = f'{cleaned_page_name}_2025_Temporal.jpg'
        output_file_path = os.path.join(output_directory, file_name)
        
        mat = fitz.Matrix(2.0, 2.0)
        pix = page.get_pixmap(matrix=mat)
        pix.save(output_file_path)
        
        del pix

pdf_document.close()

print("Conversion complete. Check the 'JPGTEACHERS' directory for individual JPGs.")
