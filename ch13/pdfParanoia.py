#! python3
# pdfParanoia.py - Walks through the folders and find .pdf files and
# encrypt the file with given password. Save in different filename
# and try decrypting those files.

import PyPDF2, os, sys

# Walk through folders and subfolders to find all PDFs
# use 'os.walk' and find files ends with .pdf
pdfs = []
for folderName, subfolders, filenames in os.walk('.'):
    for filename in filenames:
    	if filename.endswith('.pdf'):
    		pdfs.append(os.path.abspath(folderName) + '\\' + filename)

for filename in pdfs:
    pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfReader.numPages):
    	pdfWriter.addPage(pdfReader.getPage(pageNum))
    # Encrypt the PDFs with password from command line
    pdfWriter.encrypt(sys.argv[1])
    # Save files with _encrypted.pdf suffix and delete older files.
    resultPdf = open(os.path.splitext(filename)[0] + '_encrypted.pdf', 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()