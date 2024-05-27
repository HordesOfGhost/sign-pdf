from utils.bounding_box import * 
from PIL import Image
import numpy as np
import os

def add_sign_to_sign_area(pdf_image, sign_image, absolute_sign_area):
    (x1, y1), (x2, y2) = absolute_sign_area

    resized_sign_image = cv2.resize(sign_image,(int(x2 - x1), int(y2 - y1)))    
    pdf_image[y1:y2, x1:x2] = resized_sign_image
    return pdf_image


def add_sign_to_sign_area_transparent(pdf_image, sign_image_path, absolute_sign_area, page):

    pdf_file_path = f'{page}_pdf.jpg'

    cv2.imwrite(pdf_file_path,pdf_image)
    pdf_image = Image.open(pdf_file_path)

    # Open the transparent PNG image
    sign_image = Image.open(sign_image_path)

    (x1, y1), (x2, y2) = absolute_sign_area

    # Resize the PNG image to fit within the rectangular region
    resized_sign_image = sign_image.resize((x2 - x1, y2 - y1))

    # Create a new image with the same size as the PDF image
    combined_image = Image.new("RGB", pdf_image.size)

    # Paste the PDF image onto the new canvas
    combined_image.paste(pdf_image, (0, 0))

    # Paste the transparent PNG image onto the canvas within the rectangular region
    combined_image.paste(resized_sign_image, (x1, y1), mask=resized_sign_image)

    # Convert the combined image back to a numpy array
    combined_image_array = np.array(combined_image)

    if os.path.exists(pdf_file_path):
        os.remove(pdf_file_path)
    
    return combined_image_array