# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:19:10 2021

@author: BurakM & BurakCimtay
"""

import os
import cv2 as cv2
import numpy as np
import glob

# select the path
path = "E:/Tuvis/Yolov5_Son/C6/data/images/"
save_path = "E:/Tuvis/Yolov5_Son/C6/data/dst_images/"

# #i= clg0    cl=cliplimit, g=tilegridsize
# i = 104400000

# for img in glob.glob(path + "/*.jpg"):
#     image = cv.imread(img,0)
#   #Create a CLAHE object
#     clahe = cv.createCLAHE(clipLimit=10, tileGridSize=(4, 4))
#   # Adaptive threshold equalization for limiting contrast
#     dst = clahe.apply(image)
#     cv.imwrite("C:/Users/Burak/Desktop/deneme/enhancement/dst%i.jpg" %i, dst)
#     i +=1

for filename in glob.glob(path + "/*.jpg", recursive=True):
    filename=os.path.basename(filename)
    filename= os.path.splitext(filename)
    print(filename[0])
    image_name=filename[0]
    img = cv2.imread(path+str(image_name)+".jpg", 0)
  #Create a CLAHE object
    clahe = cv2.createCLAHE(clipLimit=10, tileGridSize=(4, 4))
  # Adaptive threshold equalization for limiting contrast
    dst = clahe.apply(img)
    cv2.imwrite(save_path+ str(image_name) +".jpg", dst)

# #her cl,g değeri için sadece bir equa oluşuyor equa cl,g'den bağımsız    
# a = 0  
# for img in glob.glob(path + "/*.jpg"):
#     image = cv.imread(img,0) 
#    # Use global histogram equalization
#     equa = cv.equalizeHist(image)
#     cv.imwrite("C:/Users/Burak/Desktop/deneme/enhancement/equa%a.jpg" %a, equa)
#     a +=1
#     """cv.imshow('equa', equa)
#     cv.waitKey()
# cv.destroyAllWindows()"""


   