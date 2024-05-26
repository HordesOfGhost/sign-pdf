import argparse
from utils.pdf_to_img import *
from utils.get_bounding_box import *
from utils.pdf_merger import *

ag = argparse.ArgumentParser()
ag.add_argument("-p", "--pdf", type = str, required = True, help = "Input pdf file where sign is requierd." )
ag.add_argument("-s", "--sign", type = str, required = False, help = "Input sign as a image file.")

arguments = ag.parse_args()
pdf_file_path = arguments.pdf
sign_image_file_path = arguments.sign

resize_parameter = (800,800)

pdf_images = convert_pdf_to_image(pdf_file_path)

sign_area_per_page = []

for pdf_image in pdf_images:
    sign_area_per_page.append(get_bounding_box(pdf_image, resize_parameter))

for sign_areas in sign_area_per_page:
    for sign_area in sign_areas:
        merge_pdf_with_image(pdf_file_path, sign_image_file_path, )

