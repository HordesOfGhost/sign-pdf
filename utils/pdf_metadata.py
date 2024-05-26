from pypdf import PdfReader

def get_pdf_metadata(pdf_file_path):
    with open(pdf_file_path ,"rb") as f:
        empty_pdf = PdfReader(f)


        for i in range(empty_pdf.get_num_pages()):
            empty_page = empty_pdf.get_page(i)
            return empty_page['/MediaBox']
