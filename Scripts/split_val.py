import os
import glob
import cv2

for i in range(25):
    j=0
    path="E:/Tuvis/Split_Classes/"
    path=path+str(i)+"/"
    for filename in glob.glob(path+"*.jpg",recursive=True):
        filename_str=filename
        filename=os.path.basename(filename)
        filename= os.path.splitext(filename)
        print(filename[0])
        image_path=filename[0]
        img = cv2.imread(path+str(image_path)+".jpg")
        cv2.imwrite('E:/Tuvis/Split_Classes/val/'+str(image_path) +".jpg", img)
        os.remove(filename_str)
        j=j+1

        if j==4:
            break