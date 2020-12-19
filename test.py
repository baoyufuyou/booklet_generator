from pyPdf import PdfFileWriter, PdfFileReader
output_pdf = PdfFileWriter()

with open(r'Marr_Vision_A_Computational_Investigation.pdf', 'rb') as readfile:
    input_pdf = PdfFileReader(readfile)
    total_pages = input_pdf.getNumPages()
    print('pages: {}'.format(total_pages))
     
    unit_num = int(total_pages//4)
    rest = int(total_pages%4)
    # print(rest)
    for unit in range(0, unit_num):
        start_page = 4 * unit
        output_pdf.addPage(input_pdf.getPage(start_page+4))
        output_pdf.addPage(input_pdf.getPage(start_page+1))
        output_pdf.addPage(input_pdf.getPage(start_page+2))
        output_pdf.addPage(input_pdf.getPage(start_page+3))
        # output_pdf.addPage(input_pdf.getPage(page))
        print(start_page+4)
    for page in range(0, rest):
        start_page = 4 * unit_num
        print(start_page + page + 1)
        output_pdf.addPage(input_pdf.getPage(start_page + page ))
    with open(r'test.pdf', "wb") as writefile:
        output_pdf.write(writefile)
