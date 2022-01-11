import cv2
import pytesseract

imagen = cv2.imread("isoft.png")
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
text = pytesseract.image_to_string(imagen)
print(text)