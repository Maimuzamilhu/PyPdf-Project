import PyPDF3 as MyPdf
#-----------------
MyPdfFile=open("Files/MyPDF.pdf","rb")
#---------------
pdf_reader=MyPdf.PdfFileReader(MyPdfFile,strict=False)
#---------------
MyWriter=MyPdf.PdfFileWriter()
#---------------
page_index_list=range(pdf_reader.numPages)
#---------------
for page_index in page_index_list:
    # ------ create rotated page object ----------
    MyPage:MyPdf.pdf.PageObject=pdf_reader.getPage(page_index)#Zero based index
    MyPage.rotateClockwise(90)#90- 180-270-360
    #--------
    MyWriter.addPage(MyPage)
#---------------
#-------- create new pdf file object --------
NewPdfFile = open( "files/rotated_Pdf_File.pdf", "wb")
MyWriter.write(NewPdfFile)
#---------------
# ----close the original pdf file ---------
MyPdfFile.close()
# ------close the new pdf file ------------
NewPdfFile.close()


