# -*- coding: utf-8 -*-
import numpy as np
import pyautogui
import imutils
import cv2
import pytesseract

x1,y1 = 1500,730
x2,y2 = 1600,760

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/student/Desktop/UnitT-Hack/tesseract.exe'

while True:
    # Screenshot
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.rectangle(image, (x1,y1), (x2,y2), (0, 0,255), 2)
    #cv2.imshow("Screencapture", imutils.resize(image, width=960, height=1100))
    diff_len = x2-x1
    diff_wid = y2-y1
    #Capture region of interest
    ROI = image[y1:y1+diff_wid,x1:x1+diff_len]
    #OCR
    gray = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY) 
    text = pytesseract.image_to_string(gray)
    print(text)
    
    
    cv2.imshow("ROI",ROI)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
