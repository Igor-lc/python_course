import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('img_2.png')
text = pytesseract.image_to_string(img, lang='ukr+eng')
print(text)
