from utils.bounding_box import * 


def add_sign_to_sign_area(pdf_image, sign_image, absolute_sign_area):
    print(absolute_sign_area)
    (x1, y1), (x2, y2) = absolute_sign_area

    resized_sign_image = cv2.resize(sign_image,(int(x2 - x1), int(y2 - y1)))
    print(resized_sign_image.shape)
        
    print("x1:", x1)
    print("x2:", x2)
    print("y1:", y1)
    print("y2:", y2)

    # Try printing the dimensions of the slice
    print(pdf_image.shape)
    print("Dimensions of the slice:", pdf_image[y1:y2, x1:x2].shape)
    pdf_image[y1:y2, x1:x2] = resized_sign_image
    return pdf_image