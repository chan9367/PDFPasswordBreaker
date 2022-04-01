import PyPDF2


pdf = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))
pdfWriter.encrypt('impostor')
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()


dictFile = open('dictionary.txt')
pdfReader2 = PyPDF2.PdfFileReader(open('encryptedminutes.pdf', 'rb'))
for word in dictFile.readlines():
    flag1 = pdfReader2.decrypt(word.strip())
    if(flag1 == 1):
        print(word.strip())
        break
    flag2 = pdfReader2.decrypt(word.lower().strip())
    if(flag2 == 1):
        print(word.lower().strip())
        break

