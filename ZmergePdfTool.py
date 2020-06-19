from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfFileMerger
import csv
import os

usersCwd = os.getcwd()

# For Windows Only OS -> '%SystemDrive%/Users/%username%'

def chooseFile(fileFlag):
    fileName = ''
    whileFlag = False
    while whileFlag == False:
        if fileFlag == 'source':
            fileName = filedialog.askopenfilenames(initialdir=usersCwd, title='Select pdfs Source File', filetypes=(("pdf Files", "*.pdf"),("All Files", "*.*")))
            listFiles = list(fileName)
            print(fileName)
        elif fileFlag == 'target':
            fileName = filedialog.asksaveasfilename(initialdir=usersCwd, title='Save pdf Target File', filetypes=(("pdf Files", "*.pdf"),("All Files", "*.*")))
        if len(fileName) > 0:
            whileFlag = True
        else:
            resVar = messagebox.askquestion('Cancelation Alert', 'Do You Want To Exit The App . . .')
            if resVar == 'yes':
                exit(0)
            elif resVar == 'no':
                whileFlag = False
    return fileName

def createTargetCsv(sourceFile, targetFile):
    nameVar = ''
    timeVar = ''
    n = 0
    inFile = open(sourceFile)
    outFile = open(targetFile, 'w')
    fileCont = csv.reader(inFile)

    for fileRow in fileCont:
        tVar = ''.join(fileRow)
        if n > 3 and tVar[:1].isalpha() == True:
            outFile.write(nameVar + timeVar + '\n')
            nameVar = ''
            timeVar = ''
            n = 0
        if tVar[:1].isalpha() == True:
            n = n + 1
            nameVar += tVar + ';'
        if tVar[:1].isdigit() == True:
            timeVar += tVar + ';'
            n = n + 1
    outFile.write(nameVar + timeVar + '\n')
    inFile.close()
    outFile.close()

def MergePdfFiles(pdfFiles, outFile):
    mergePdf = PdfFileMerger()
    for fPdf in pdfFiles:
        if fPdf.endswith('pdf') or fPdf.endswith('PDF'):
            mergePdf.append(fPdf)
    mergePdf.write(outFile)         
    mergePdf.close()

sourceFile = chooseFile('source')
outFile = chooseFile('target')
#createTargetCsv(sourceFile, outFile)
mergePdf = MergePdfFiles(sourceFile, outFile)
messagebox.showwarning('File Created', 'Process Ended')