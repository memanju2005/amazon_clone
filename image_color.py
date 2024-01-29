from PIL import Image

# Open an image
image = Image.open("web-colors\\sign-in.png")

# Get the color of a pixel at a specific location (x, y)
pixel_color = image.getpixel((4, 4))
print("Pixel color at (x, y):", pixel_color)