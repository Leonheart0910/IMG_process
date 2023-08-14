import cv2
import numpy as np
import pytesseract
from pytesseract import Output

# Set Tesseract CMD path and language option to Chinese (Simplified)
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
custom_oem_psm_config = r'--oem 3 --psm 6 -l chi_sim'

def remove_chinese_text(image_path):
    # Load image
    img = cv2.imread(image_path)
    
    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Applying Gaussian Blur
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    
    # Applying adaptive thresholding
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 30)

    # Invert the image
    inverted = 255 - thresh
    
    d = pytesseract.image_to_data(inverted, output_type=Output.DICT, config=custom_oem_psm_config)
    n_boxes = len(d['level'])

    # Create mask for inpainting
    mask = np.zeros(img.shape[:2], dtype="uint8")

    # Mark detected text area in mask
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 255), -1)

    # Inpaint image
    dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

    return dst

img_text_removed = remove_chinese_text('C:/Users/halo0/Desktop/et.jpg')
cv2.imwrite('text_removed_image.jpg', img_text_removed)
