import PyPDF3 as MyPdf
#-----------------
MyPdfFile=open("Files/MyPDF.pdf","rb")
#---------------
pdf_reader=MyPdf.PdfFileReader(MyPdfFile,strict=False)
#---------------
# ---- create a pdf writer for new pdf file ---
PdfWriter = MyPdf.PdfFileWriter()
#----- Copy source Pdf to Pdf writer -------
for page_index in range(pdf_reader.getNumPages()):
     PdfWriter.addPage(pdf_reader.getPage(page_index))
#------------------
PdfWriter.encrypt(user_pwd="", owner_pwd=None,use_128bit=True,allow_printing=True,allow_commenting=False)
#------------Save Encrypted file ---------------
output_pdf_file= open("Files/MyPdf_Locked.pdf", 'wb')
PdfWriter.write(output_pdf_file)
#-----------------------
output_pdf_file.close()
MyPdfFile.close()
