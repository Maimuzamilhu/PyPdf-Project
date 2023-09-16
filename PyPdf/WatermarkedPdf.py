import PyPDF3 as MyPdf

#----------Open watermark pdf file ------------------
watermark =  "Files/Wmark.pdf"
WmPdfFile =open(watermark,"rb")
#----------Create pdf reader file for watermark------
WmFileReader = MyPdf.PdfFileReader(WmPdfFile,strict=False)
WaterMarkPage = WmFileReader.getPage(0)
#-----------open original pdf file & create reader--
originalfile = "Files/MyPdf.pdf"
OrgPdfFile =open(originalfile,"rb")
OrgPdfReader = MyPdf.PdfFileReader(OrgPdfFile,strict=False)
#---------create pdf writer for out file---------
PdfOutWriter= MyPdf.PdfFileWriter()
#----------------------------
for page_index in range(OrgPdfReader.getNumPages()):
    #------ get the current page of original pdf ------
    OrgPdfPage:MyPdf.pdf.PageObject=OrgPdfReader.getPage(page_index)
    # -------merge vm to current page of original pdf ---
    #if page_index==2:
        #OrgPdfPage.mergePage(WaterMarkPage)
    #--------
    OrgPdfPage.mergePage(WaterMarkPage)
    PdfOutWriter.addPage(OrgPdfPage)

#----------save watermarked file -------------
watermarkedfile =  "Files/MyPdfWatermarked.pdf"
OutPdfFile=open(watermarkedfile, 'wb')
PdfOutWriter.write(OutPdfFile)
#----------------
WmPdfFile.close()
OrgPdfFile.close()
OutPdfFile.close()