import numpy as np
import cv2
import pyautogui
from PIL import Image
from pytesseract import pytesseract

#take screenshot using pyautogui
x = 540
y = 50
image = pyautogui.screenshot(region=(x, y, x+300, y+100))

image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

#-------------------------------------------
#extrack words
path_to_tesseract = r"" #download tesseract and put the location of tesseract.exe

#providing the tesseract executable
#location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

#extract the text from the image
text = pytesseract.image_to_string(image)

# Displaying the extracted text
print(text[:-1])

texts = text[:-1].replace("‘", "'").split()

#---------------------------------------------------
#keyboard input

for i in texts:
    pyautogui.write(i)
    print(i)
    pyautogui.press("space")
