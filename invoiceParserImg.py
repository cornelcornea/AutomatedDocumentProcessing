import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('Factura-Piata-Unirii-6-Cluj-Napoca.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())
cv2.imshow('img', img)
cv2.waitKey(0)


