#-----------------------------------
import PyPDF3 as MyPdf
# ----- create pdf file merger object ----------
PdfMerger =MyPdf.PdfFileMerger(strict=False)
#---------------
PdfMerger.append("Files/MyPDF.pdf")
PdfMerger.append("Files/MyFile2.pdf")
#---------------
# ----- write the combined pdf to output pdf file ------
MergedPdfFile=open("Files/MergedPDFFile.pdf","wb")
PdfMerger.write(MergedPdfFile)
#---------------
PdfMerger.close()
MergedPdfFile.close()