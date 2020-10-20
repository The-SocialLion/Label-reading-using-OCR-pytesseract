try:
    from PIL import Image # if any error follow this just like if else
except ImportError:
    import Image
    
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe' # openening tesseract exe file in read mode

def recText(filename):
    text=pytesseract.image_to_string(Image.open(filename))#converting image to string
    return text# return text present in image using the necessary filters
# location of image
info = recText('test.png')
print(info)
file=open("result.txt","w")# copying the text in notpad in write mode
file.write(info)
file.close()
print("written succesful")
