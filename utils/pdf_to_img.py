from pdf2image import convert_from_path
import os
import cv2
import numpy as np

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