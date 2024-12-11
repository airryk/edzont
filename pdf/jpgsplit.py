import os
import re
from pdf2image import convert_from_path
import PyPDF2

def sanitize_filename(filename):
    # Remove invalid characters and replace spaces with underscores
    sanitized = re.sub(r'[<>:"/\\|?*]', '', filename)
    sanitized = sanitized.replace(' ', '_')
    # Ensure the filename is not empty and not too long
    sanitized = sanitized[:255] if sanitized else "unnamed"
    return sanitized

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_file_path = r'C:\Users\dzont\Music\pdf\temporal.pdf'
# Create a directory to store the extracted images
output_directory = r'C:\Users\dzont\Music\pdf\JPGTEACHERS'
os.makedirs(output_directory, exist_ok=True)

# Convert PDF to images
# images = convert_from_path(pdf_file_path, dpi=300)
images = convert_from_path(pdf_file_path)

# Extract text from PDF
with open(pdf_file_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Loop through each image and save it as a separate JPG file
    for i, image in enumerate(images):
        # Extract the text from the current page
        page = pdf_reader.pages[i]
        page_text = page.extract_text()
        
        # Split the text into lines and get the second line (index 1)
        lines = page_text.split('\n')
        if len(lines) > 1:
            page_name = sanitize_filename(lines[1].strip())
        else:
            page_name = f"Page_{i+1}"
        
        # Construct the output file name and path
        file_name = f'{page_name}_2025_Temporal.jpg'  # Use the extracted name as the file name
        output_file_path = os.path.join(output_directory, file_name)
        
        # Save the image as a JPG file
        image.save(output_file_path, 'JPEG')

print("Conversion complete. Check the 'JPGTEACHERS' directory for individual JPGs.")