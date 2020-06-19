import os
from PyPDF2 import PdfFileMerger

pdfTarget = 'pdf1.pdf'
sourceDir = os.getcwd()
mergePdf = PdfFileMerger()

for fPdf in os.listdir(sourceDir):
    if fPdf.endswith('pdf') or fPdf.endswith('PDF'):
        mergePdf.append(fPdf)
        print(f'Pdf {fPdf} File')

mergePdf.write(pdfTarget)         
mergePdf.close()