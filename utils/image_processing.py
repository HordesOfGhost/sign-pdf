import cv2
import numpy as np

def make_image_transparent(image):
    # Check if the image already has an alpha channel
    if image.shape[2] == 4:
        print("The image already has an alpha channel.")
    else:
        # Convert the image to BGRA (add an alpha channel)
        b, g, r = cv2.split(image)
        alpha = np.ones(b.shape, dtype=b.dtype) * 255
        image = cv2.merge((b, g, r, alpha))
    
    # Make the image transparent by modifying the alpha channel
    alpha = image[:, :, 3]
    alpha = (alpha * 0.5).astype(image.dtype)
    image[:, :, 3] = alpha
    
    # Convert back to BGR by discarding the alpha channel
    transparent_image = image[:, :, :3]
    
    return transparent_image
