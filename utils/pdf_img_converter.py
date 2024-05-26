from pdf2image import convert_from_path
import os
import cv2
import numpy as np
from fpdf import FPDF

poppler_path = r"utils/poppler/Library/bin"
poppler_path = os.path.abspath(poppler_path)

def convert_pdf_to_image(pdf_path):

    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_path,poppler_path=poppler_path)
    
    cv_images = []

    for i,image in enumerate(images):
        
        cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv_images.append(cv_image)
        
    return cv_images

def images_to_pdf(image_list, pdf_filename, pdf_metadata):
    pdf = FPDF()
    for idx,image in enumerate(image_list):
        
        temp_image_path = f"temp_image_{idx}.png"
        cv2.imwrite(temp_image_path, image)
        pdf.add_page()
        pdf.image(temp_image_path, 0, 0, 210, 297) # A4 Size
        
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path) 
    pdf.output(pdf_filename, "F")