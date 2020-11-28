import os
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\nd_xing\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('s1.png')

text = tess.image_to_string(img)

text_file = open("text.txt", "w")

text_file.write(text)

text_file.close()

os.startfile('text.txt')