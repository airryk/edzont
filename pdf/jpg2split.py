import os
import string
import fitz  # PyMuPDF

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_file_path = r'C:\Users\dzont\Music\pdf\22024timetable.pdf'

# Create a directory to store the extracted images
output_directory = r'C:\Users\dzont\Music\pdf\JPG'
os.makedirs(output_directory, exist_ok=True)

# Open the PDF file
pdf_document = fitz.open(pdf_file_path)

valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
# Loop through each page and save it as a separate JPG file
for i in range(pdf_document.page_count):
    page = pdf_document.load_page(i)
    
    # Extract the text from the second line of the page
    text = page.get_text("text")
    lines = text.split("\n")
    if len(lines) > 1:
        page_name = lines[2].strip()
        cleaned_page_name = ''.join(c for c in page_name if c in valid_chars)
        
        # Construct the output file name and path
        file_name = f'{cleaned_page_name}.jpg'  # Use the cleaned name as the file name
        output_file_path = os.path.join(output_directory, file_name)
        
        # Render the page as an image and save it
        mat = fitz.Matrix(2.0, 2.0)  # You can adjust the scaling factor as needed
        pix = page.get_pixmap(matrix=mat)
        pix.save(output_file_path)
        
        del pix  # Delete the reference to free memory

# Close the PDF document
pdf_document.close()


print("Conversion complete. Check the 'JPG' directory for individual JPGs.")
