import PyPDF3 as MyPdf
#-----------------
MyPdfFile=open("Files/MyPDF.pdf","rb")
#---------------
pdf_reader=MyPdf.PdfFileReader(MyPdfFile,strict=False)
#----------get data from pdf file -----
print("Page count:",pdf_reader.getNumPages())
#------Get doc info------
doc_info=pdf_reader.getDocumentInfo()
print(doc_info)
#----
for info_item in doc_info:
    #print("Item: ",info_item)
    item_val=doc_info[str(info_item)]
    print("Item: ",str(info_item).removeprefix("/")," => ", "Value:",item_val)
#---------------
print("--------------")
print("Author:",doc_info["/Author"])
print("Producer:",doc_info["/Producer"])
MyPdfFile.close()

