from utils.bounding_box import * 


def add_sign_to_sign_area(pdf_image, sign_image, absolute_sign_area):
    (x1, y1), (x2, y2) = absolute_sign_area

    resized_sign_image = cv2.resize(sign_image,(int(x2 - x1), int(y2 - y1)))

    pdf_image[y1:y2, x1:x2] = resized_sign_image
    return pdf_image