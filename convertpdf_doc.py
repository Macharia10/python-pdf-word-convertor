#convert pdf to document
from pdf2docx import Converter

#name of the file you want to convert
pdf_file = "server checker\TRIC.pdf"
docx_file = "server checker\TRIC.docx"
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()