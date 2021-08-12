"""Before run the script, must be like this directory structure

__c6-d100
|__Split_Classes
 |__1
 |__2
 |__3
 |__4
 |__5
 |__6  """


import os
import glob
import cv2

path="D:/Tuvis/c6-d100/data/"
label_path="D:/Tuvis/c6-d100/data/yolo/"

for filename in glob.glob(path+"*.jpg",recursive=True):
    filename=os.path.basename(filename)
    filename= os.path.splitext(filename)
    print(filename[0])
    image_name=filename[0]
    img = cv2.imread(path+str(image_name)+".jpg")
    
    with open(label_path+ str(image_name) +".txt", 'r') as f: 
        for line in f: 
            label=int(line[:2])
            
            cv2.imwrite('D:/Tuvis/c6-d100/Split_Classes/'+str(label)+"/"+ str(image_name) +".jpg", img) #create the folder yourself