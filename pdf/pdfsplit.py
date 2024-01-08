import os
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter


# Replace 'your_pdf_file.pdf' with the path to your PDF file
# ( the location should be should be in ' ' below.)
pdf_file_path = r' '

# Create a directory to store the extracted pages
# ( the location should be should be in ' ' below.)
output_directory = r' '
os.makedirs(output_directory, exist_ok=True)

with open(pdf_file_path, 'rb') as file:
    pdf_reader = PdfReader(file)
    
    # Loop through each page and save it as a separate file
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        
        # Use the first line of text as the file name
        file_name = page.extract_text().split('\n')[1].strip()
        
        # Handle potential naming conflicts by appending a number
        file_name = file_name[:50] if len(file_name) > 50 else file_name  # Limit file name length
        
        # Save the page as a separate PDF file
        output_file_path = os.path.join(output_directory, f'{file_name}.pdf')
        
        # Create a new PDF writer and add the current page
        pdf_writer = PdfWriter()
        pdf_writer.add_page(page)
        
        # Write the page to the output file
        with open(output_file_path, 'wb') as output_file:
            pdf_writer.write(output_file)

print("Extraction complete. Check the 'extracted_pages' directory for individual PDFs.")
