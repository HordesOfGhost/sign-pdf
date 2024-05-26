from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfWriter, PdfReader

def create_image_pdf(image_path, x, y, width, height):
    c = canvas.Canvas(pagesize=letter)
    c.drawImage(image_path, x, y, width, height)
    return c

def merge_pdf_with_image(background_pdf_path, image_path, x_position, y_position, image_width, image_height):
    
    overlay_pdf = create_image_pdf(image_path, x_position, y_position, image_width, image_height)

    # Read the PDFs
    background_pdf = PdfReader(open(background_pdf_path, "rb"))


    output = PdfWriter()

    # Iterate over each page of the background PDF
    for i in range(len(background_pdf.pages)):
        background_page = background_pdf.pages[i]
        overlay_page = overlay_pdf.pages[0]  # Use the single overlay page for all pages

        # Merge the overlay page onto the background page
        background_page.merge_page(overlay_page)
        output.add_page(background_page)

    # Write the result to a new PDF
    with open(f"signed_{background_pdf_path}", "wb") as output_file:
        output.write(output_file)

    print(f"PDF with overlay image saved as 'signed_{background_pdf_path}'")