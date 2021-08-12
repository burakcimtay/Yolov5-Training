import os
import glob
import cv2

path="E:/Tuvis/Split_Classes/"
save_path='E:/Tuvis/Split_Classes/train/images/'

for i in range(25):
    path=path+str(i)+"/"
    for filename in glob.glob(path+"*.jpg",recursive=True):
        filename_str=filename
        filename=os.path.basename(filename)
        filename= os.path.splitext(filename)
        print(filename[0])
        image_name=filename[0]
        img = cv2.imread(path+str(image_name)+".jpg")
        cv2.imwrite(save_path+str(image_name) +".jpg", img)