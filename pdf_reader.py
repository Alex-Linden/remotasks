# import PyPDF2

# # Open the file
# pdf = open("test.pdf", "rb")

# # Creatr PyPDF2 reader object
# pdfReader = PyPDF2.PdfReader(pdf)

# # Extract number of pages into list
# page_num = len(pdfReader.pages)

# # Loop through all the pages
# for i in range(page_num):
#     # Get the page content.
#     page = pdfReader.getPage(i)
#     # Print document content of each page
#     print(page.extractText())

# pdf.close()


import fitz


# Open the file
file = "/path/to/target.pdf"
doc = fitz.open('test.pdf')

# Loop through all pages
for i, page in enumerate(doc.pages(), start=1):
  text = page.get_text("text")
  print("Reading page {} from {} ...".format(i, file))
  print("Text from page {}:\n'{}'\n".format(i, text))

# Close document
doc.close()


#  Source: assistant
# Destination: user

#  PyMuPDF (previously PyMuPDF, and before PyPDF2), is built using the same code as the MuPDF library developed by Artifex MuPDF. It allows to create and manipulate PDF documents. Here is an example to extract text from a PDF file using PyMuPDF:

# ```python
# from fitz import *

# # Open the file
# with open("test.pdf", "rb") as pdfFile:
#     ## Create a document object
#     doc = Document(pdfFile)

#     ## Extract text from all pages
#     for page in doc:
#         print(page.getText())

#     ## Extract all text
#     print(doc.getText())
# ```

# Here Document() function is used to create a stand-alone Python object from a PDF file. Note that this object doesn't store file contents, it simply attaches itself to the PDF file on disk and reads it as necessary.
