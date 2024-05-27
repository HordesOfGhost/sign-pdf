import argparse
from utils.pdf_img_converter import *
from utils.bounding_box import *
from utils.merge import *


'''

    ArgParsers.

'''

ag = argparse.ArgumentParser()
ag.add_argument("-p", "--pdf", type = str, required = True, help = "Input pdf file where sign is requierd." )
ag.add_argument("-s", "--sign", type = str, required = True, help = "Input sign as a image file.")
ag.add_argument("-o", "--output", type = str, required = True, help = "Output for signed pdf.")

'''

    Get Argument values from ArgParsers.

'''
arguments = ag.parse_args()
pdf_file_path = arguments.pdf
sign_image_file_path = arguments.sign
output_pdf_file_path = arguments.output

'''

    Set resize_dimension to better visualize pdf-page images for drawing bounding box.

'''
resized_dimension = (800,800)


'''

    If the sign image is a transparent png then read the alpha channel too. 
    Else Read only 3 channels.

'''
if os.path.splitext(sign_image_file_path)[1].lower() == '.png':
    sign_image = cv2.imread(sign_image_file_path, -1)
else:
    sign_image = cv2.imread(sign_image_file_path)

'''

    Read pdf file and convert it to array of images.

'''
pdf_images = convert_pdf_to_image(pdf_file_path)


'''

    Get sign_areas for each pdf pages.

'''
sign_area_per_page = []
for pdf_image in pdf_images:
    sign_area_per_page.append(get_bounding_box(pdf_image, resized_dimension))

'''

    Finally paste the sign onto pdf images.

'''


for page, sign_areas in enumerate(sign_area_per_page):
    
    if sign_areas:
        for sign_area in sign_areas:
            absolute_sign_area = get_absolute_bounding_box(sign_area, resized_dimension, pdf_images[page].shape)
            
            # For sing image as jpg or jpeg
            if sign_image.shape[-1] == 3: 
                pdf_images[page] = add_sign_to_sign_area(pdf_images[page], sign_image, absolute_sign_area)
                
            # For transparent png sign images.
            else:
                pdf_images[page] = add_transparent_sign_to_sign_area(pdf_images[page], sign_image_file_path, absolute_sign_area, page)


images_to_pdf(pdf_images, output_pdf_file_path )




