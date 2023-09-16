import PyPDF3 as MyPdf
#-----------------
MyPdfFile=open("Files/MyPDF.pdf","rb")
#---------------
pdf_reader=MyPdf.PdfFileReader(MyPdfFile,strict=False)
#---------------
# ---- create a pdf writer for new pdf file ---
PdfWriter = MyPdf.PdfFileWriter()
PdfWriter.addPage(pdf_reader.getPage(1))
# -------- create new pdf file object --------
SplitPdfFile = open("Files/Splitted/1.pdf", "wb")
PdfWriter.write(SplitPdfFile)
SplitPdfFile.close()
