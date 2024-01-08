from PyPDF2 import PdfReader
#  The lines of code below is to find out the contents on my pdf line by line, so I can make proper reference to the line I want to call as the name of the file.
# Replace 'your_pdf_file.pdf' with the path to your PDF file
# ( uncomment the line below which is the output of the file location and the location should be should be in ' ' below.)
pdf_file_path = r' '

# Open the PDF file
with open(pdf_file_path, 'rb') as file:
    pdf_reader = PdfReader(file)
    
    # Get text from the first page
    first_page_text = pdf_reader.pages[0].extract_text()
    
    # Split the text into lines and display line by line
    lines = first_page_text.split('\n')
    for line_number, line in enumerate(lines):
        print(f"Line {line_number + 1}: {line}")
