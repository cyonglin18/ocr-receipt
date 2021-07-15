#
# https://www.kaggle.com/dmitryyemelyanov/receipt-ocr-part-1-image-segmentation-by-opencv

import numpy as np 
import cv2
import matplotlib.pyplot as plt

from PIL import Image

file_name = 'receipt2.jpg'
img = Image.open(file_name)
img.thumbnail((800,800), Image.ANTIALIAS)
img
