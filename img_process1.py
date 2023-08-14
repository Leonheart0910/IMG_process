import cv2
import numpy as np
import pytesseract
from pytesseract import Output

# Set the path for Tesseract. Replace 'C:/Program Files/Tesseract-OCR/tesseract.exe' with the actual path if it's different.
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def remove_chinese_from_image(input_path, output_path):
    # Load the image
    image = cv2.imread(input_path, cv2.IMREAD_COLOR)
    
    # Convert the image to gray scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Get bounding boxes for words in the image
    boxes = pytesseract.image_to_boxes(image, lang='chi_sim+eng')

    # For each bounding box, check if the character is Chinese and if so, remove it from the image
    for box in boxes.splitlines():
        b = box.split()
        char = b[0]
        
        # Check if the character is Chinese
        if '\u4e00' <= char <= '\u9fff':
            (x, y, w, h) = (int(b[1]), int(b[2]), int(b[3]), int(b[4]))
            cv2.rectangle(image, (x, image.shape[0] - y), (w, image.shape[0] - h), (255, 255, 255), -1)

    # Save the modified image
    cv2.imwrite(output_path, image)

# Example usage:
input_path1 = "C:\\Users\\halo0\\Desktop\\et.jpg"
output_path1 = "C:\\Users\\halo0\\Desktop\\output_image1.jpg"
remove_chinese_from_image(input_path1, output_path1)
