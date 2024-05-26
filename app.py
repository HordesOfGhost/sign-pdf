import argparse
from utils.pdf_to_img import *
from utils.get_bounding_box import *


ag = argparse.ArgumentParser()
ag.add_argument("-p", "--pdf", type = str, required = True, help = "Input pdf file where sign is requierd." )
ag.add_argument("-s", "--sign", type = str, required = False, help = "Input sign as a image file.")

arguments = ag.parse_args()
pdf_file_path = arguments.pdf
sign_image_file_path = arguments.sign


pdf_images = convert_pdf_to_image(pdf_file_path)

for pdf_image in pdf_images:
    get_bounding_box(pdf_image)

