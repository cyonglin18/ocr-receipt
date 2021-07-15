import cv2
import numpy as np
import pytesseract
import os

#pytesseract.pytesseract.tesseract_cmd = 

imgQ = cv2.imread('receipt2.jpg')
h, w, c = imgQ.shape
#imgQ = cv2.resize(imgQ, (w//3, h//3))

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]



custom_config = r'--oem 3 --psm 6'
pytesseract.image_to_string(imgQ, config=custom_config)

imgQ = get_grayscale(imgQ)
#imgQ = remove_noise(imgQ)
imgQ = thresholding(imgQ)
boxes = pytesseract.image_to_boxes(imgQ)

for b in boxes.splitlines():
    b = b.split(' ')
    imgQ = cv2.rectangle(imgQ, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)




#orb = cv2.ORB_create(5000)

#kp1, des1 = orb.detectAndCompute(imgQ, None)

#imgKp1 = cv2.drawKeypoints(imgQ, kp1, None)

cv2.imshow("Output", imgQ)
cv2.waitKey(0)


