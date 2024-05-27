from pdf2image import convert_from_path
import os
import cv2
import numpy as np
from fpdf import FPDF

# Load poppler files
poppler_path = r"utils/poppler/Library/bin"
poppler_path = os.path.abspath(poppler_path)

def convert_pdf_to_image(pdf_path):
    '''

        Convert pdf pages to pdf images.

        Parameters:
            pdf_path : path to pdf file.
        
        Returns:
            pdf_images : list of pdf images for each pdf page.
            
    
    '''

    # Convert Pdf to images with convert_from_path function
    images = convert_from_path(pdf_path,poppler_path=poppler_path)
    
    # Append pdf images and return
    pdf_images = []
    for image in images:
        pdf_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        pdf_images.append(pdf_image)
        
    return pdf_images

def images_to_pdf(pdf_images, pdf_filename):
    
    '''

        Convert and save pdf images to a single pdf.

        Parameters:
            pdf_images : list of pdf images corresponding to each pdf page.
            pdf_filename : a single pdf filename or path.    
    
    '''

    pdf = FPDF()

    for idx,image in enumerate(pdf_images):
        
        # Temporarily save pdf page images.
        temp_image_path = f"temp_image_{idx}.png"
        cv2.imwrite(temp_image_path, image)
        
        # Add the signed images in pdf
        pdf.add_page()
        pdf.image(temp_image_path, 0, 0, 210, 297) # A4 Size
        
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path) 

    # Save in given path.
    pdf.output(pdf_filename, "F")