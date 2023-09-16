import PyPDF3 as MyPdf
#-----------------
MyPdfFile=open("Files/MyPDF.pdf","rb")
#---------------
pdf_reader=MyPdf.PdfFileReader(MyPdfFile,strict=False)
#---------------
for page_index in range(pdf_reader.getNumPages()):
    # ---------------
    pdf_reader = MyPdf.PdfFileReader(MyPdfFile, strict=False)
    # ---- create a pdf writer for new pdf file ---
    PdfWriter = MyPdf.PdfFileWriter()
    PdfWriter.addPage(pdf_reader.getPage(page_index))
    # -------- create new pdf file object --------
    # ----------create splitted file name -------------------------
    SplittedPdfFileName = str(page_index) + ".pdf"
    # -------
    SplitPdfFile = open("Files/Splitted/"+SplittedPdfFileName, "wb")
    PdfWriter.write(SplitPdfFile)
    SplitPdfFile.close()