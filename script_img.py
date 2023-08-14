import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Open the image with PIL
im = Image.open("C:/Users/halo0/Desktop/고퍼/text_removed_image.jpg.jpg")

# Create an ImageDraw object
draw=ImageDraw.Draw(im)

# Specify the font size
fontsize = 160  # Increased from 16 to 160

# Specify the font
font = ImageFont.truetype("arial.ttf", fontsize)

# Text to write
text = "sdfsdfsdf"

# Get the size of the text
textwidth, textheight = draw.textsize(text, font)

# Calculate x, y position to center the text
x = (im.width - textwidth) / 3
y = (im.height - textheight) / 3

# Write text on the image
draw.text((x, y), text, font=font, fill=(255,255,255))

# Save the image
im.save("title.png")

# Open the image with OpenCV
image = cv2.imread("title2.png")

# Convert color from BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image)
plt.show()
