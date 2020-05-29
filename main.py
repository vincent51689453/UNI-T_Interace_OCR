# -*- coding: utf-8 -*-
import numpy as np
import pyautogui
import imutils
import cv2
import pytesseract
import win32gui
import win32con
import timeit

#Scope for OCR
x1,y1 = 1500,730
x2,y2 = 1600,760

#Window Size
window_x,window_y = 822,429
window_w,window_h = 793,718

#Path Detail
application = 'UTi165K V1.38'
file_path = 'D:/SmartWorkshop/UniT-165k.txt'
pytesseract.pytesseract.tesseract_cmd = 'D:/SmartWorkshop/UnitT-Hack/tesseract.exe'


def freeze_application(name,window_handler):
    #Set Application window location
    win32gui.SetWindowPos(window_handler,win32con.HWND_NOTOPMOST,window_x,window_y,window_w,window_h,0)
  

def anchor(name):
    #Get Application window detail
    handler = win32gui.FindWindow(None,name)
    title = win32gui.GetWindowText(handler)
    classname = win32gui.GetClassName(handler)
    #print("Handler:{} Window Title: {}".format(handler,title))
    rect = win32gui.GetWindowRect(handler)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    if(x!=window_x)or(y!=window_y)or(w!=window_w)or(h!=window_h):
        freeze_application(application,handler)   
    return True


anchor(application)

while True:
    #Fix window position
    anchor(application)
    # Screenshot
    start = timeit.default_timer()
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
    f = open(file_path,"w")
    f.write(text)
    stop = timeit.default_timer()
    runtime = round(stop-start,2)
    print("Tesseract:{} RunTime:{}s".format(text,runtime))
    
    
    cv2.imshow("ROI",ROI)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
