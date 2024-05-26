import argparse
from utils.pdf_img_converter import *
from utils.bounding_box import *
from utils.merge import *

ag = argparse.ArgumentParser()
ag.add_argument("-p", "--pdf", type = str, required = True, help = "Input pdf file where sign is requierd." )
ag.add_argument("-s", "--sign", type = str, required = False, help = "Input sign as a image file.")
ag.add_argument("-o", "--output", type = str, required = False, help = "Output for signed pdf.")


arguments = ag.parse_args()
pdf_file_path = arguments.pdf
sign_image_file_path = arguments.sign
output_pdf_file_path = arguments.output

resized_dimension = (800,800)

sign_image = cv2.imread(sign_image_file_path, -1)
pdf_images = convert_pdf_to_image(pdf_file_path)



sign_area_per_page = []


for pdf_image in pdf_images:
    sign_area_per_page.append(get_bounding_box(pdf_image, resized_dimension))


if sign_image[-1] == 4:
    for page, sign_areas in enumerate(sign_area_per_page):
        for sign_area in sign_areas:
            absolute_sign_area = get_absolute_bounding_box(sign_area, resized_dimension, pdf_images[page].shape)
            pdf_images[page] = add_sign_to_sign_area(pdf_images[page], sign_image, absolute_sign_area)


    images_to_pdf(pdf_images, output_pdf_file_path )

else:
    for page, sign_areas in enumerate(sign_area_per_page):
        for sign_area in sign_areas:
            absolute_sign_area = get_absolute_bounding_box(sign_area, resized_dimension, pdf_images[page].shape)
            