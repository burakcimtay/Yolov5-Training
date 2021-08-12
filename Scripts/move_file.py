import os
import glob
import shutil

label_path="E:/Tuvis/format/xml2yolo/xml/"
image_path="E:/Tuvis/Yolov5_Son/valid/images/"

for filename in glob.glob(image_path+"*.jpg", recursive=True):
    filename_str=filename
    filename=os.path.basename(filename)
    filename= os.path.splitext(filename)
    filename=filename[0]
    for label_name in glob.glob(label_path+"*.xml", recursive=True):
        label_name_str=label_name
        label_name=os.path.basename(label_name)
        label_name= os.path.splitext(label_name)
        label_name=label_name[0]
        if label_name==filename:
            original = r"E:/Tuvis/format/xml2yolo/xml/"+str(label_name)+".xml"
            target = r'E:/Tuvis/Yolov5_Son/valid/xml/'+str(label_name)+".xml"
            
            shutil.move(original,target)