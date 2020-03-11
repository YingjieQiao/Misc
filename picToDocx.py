from PIL import Image
import pytesseract
from docx import Document

im = Image.open('/Users/danielqiao/Downloads/pic1.jpg')

text = pytesseract.image_to_string(im, lang='eng')

document = Document()
document.add_paragraph(text)
document.save('notes.docx')