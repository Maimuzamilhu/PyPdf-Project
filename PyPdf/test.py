import PyPDF3 as MyPdf
from PyPDF3.generic import BooleanObject, NameObject, IndirectObject

def set_need_appearances_writer(writer: MyPdf.PdfFileWriter):
    # See 12.7.2 and 7.7.2 for more information: http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
    try:
        catalog = writer._root_object
        # get the AcroForm tree
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer
#---------open pdf file & create pdf reader object ------
OrgPdfFile =open("Files/new_document.pdf","rb")
pdf_reader=MyPdf.PdfFileReader( OrgPdfFile , strict=False )
d=pdf_reader.getFormTextFields()
print(d)
pdfWriter = MyPdf.PdfFileWriter()
set_need_appearances_writer(pdfWriter)
if "/AcroForm" in pdfWriter._root_object:
    pdfWriter._root_object["/AcroForm"].update(
        {NameObject("/NeedAppearances"): BooleanObject(True)})

#pdfWriter.addPage(pdf_reader.getPage(0))
fieldss= {'fname': "ffff", 'lname': "lllll"}
pdfWriter.addPage(pdf_reader.getPage(0))
pdfWriter.updatePageFormFieldValues(pdfWriter.getPage(0), fieldss)
pdfWriter.appendPagesFromReader()
#pdfWriter.addMetadata({'/Fname': "Mj", 'Lname': "Cute"})

#OrgPdf =open("Files/MyPDF.pdf","rb")
#pdfWriter.addAttachment("myfile",OrgPdf.read())
#print("layout: ",pdf_reader.getPageLayout())
#print("mode: ",pdf_reader.getPageMode())
#----------save watermarked file -------------
watermarkedfile =  "Files/new_document_filled.pdf"
OutPdfFile=open(watermarkedfile, 'wb')
pdfWriter.write(OutPdfFile)
OrgPdfFile.close()
OutPdfFile.close()

OutPdfFile=open(watermarkedfile, 'rb')
pdf_reader=MyPdf.PdfFileReader( OutPdfFile , strict=False )
b=pdf_reader.getDocumentInfo()
print(b)