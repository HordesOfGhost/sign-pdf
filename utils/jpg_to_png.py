import cv2
import numpy as np

# Read image
img = cv2.imread("../sign-sakila.jpeg")

# Convert BGR to BGRA (add alpha channel)
img_bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

# Define white threshold
# Pixels close to white will become transparent
threshold = 120
white_mask = (
    (img[:, :, 0] > threshold) &
    (img[:, :, 1] > threshold) &
    (img[:, :, 2] > threshold)
)

img_bgra[:, :, 0] = 0  # B
img_bgra[:, :, 1] = 0  # G
img_bgra[:, :, 2] = 0  # R
img_bgra[:, :, 3] = 255  # fully opaque

# Make white pixels transparent
img_bgra[white_mask, 3] = 0



# Save as PNG
cv2.imwrite("output.png", img_bgra)
