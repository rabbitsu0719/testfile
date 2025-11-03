import pytesseract
from PIL import Image
import os

img = Image.open('01.jpg')
config = "--oem 1 --psm 6 -c preserve_interword_spaces=1"
text = pytesseract.image_to_string(img, lang='kor+eng')

print("추출된 텍스트: ", text)
