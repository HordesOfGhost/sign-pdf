from PIL import Image

# Load the JPEG image
jpeg_image = Image.open("test.png")

# Load the transparent PNG image
png_image = Image.open("test/signature.png")

# Create a new image with the same size as the JPEG
combined_image = Image.new("RGB", jpeg_image.size)

# Paste the JPEG image onto the new canvas
combined_image.paste(jpeg_image, (0, 0))

# Define the rectangular region
left, top, right, bottom = 100, 200, 400, 500  # Example coordinates

# Resize the PNG image to fit within the rectangular region
overlay_width = right - left
overlay_height = bottom - top
png_image = png_image.resize((overlay_width, overlay_height))

# Paste the transparent PNG image onto the canvas within the rectangular region
combined_image.paste(png_image, (left, top), mask=png_image)

# Save the combined image
combined_image.save("combined_image.png")