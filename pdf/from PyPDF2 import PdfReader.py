from PyPDF2 import PdfReader

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_file_path = r'C:\Users\dzont\Music\pdf\22024timetable.pdf'

# Open the PDF file
with open(pdf_file_path, 'rb') as file:
    pdf_reader = PdfReader(file)
    
    # Get text from the first page
    first_page_text = pdf_reader.pages[0].extract_text()
    
    # Split the text into lines and display line by line
    lines = first_page_text.split('\n')
    for line_number, line in enumerate(lines):
        print(f"Line {line_number + 1}: {line}")
