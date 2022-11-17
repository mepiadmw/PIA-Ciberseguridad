from PyPDF2 import PdfReader

def scanpdf(input2):
  reader=PdfReader(input2)
  meta = reader.metadata
  return meta