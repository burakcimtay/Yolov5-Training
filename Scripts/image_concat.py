import glob
import cv2
import os

first_image_path="E:/Tuvis/GroundTruth/25_class_last/groundtruth/"
second_image_path="E:/Tuvis/Yolov5_Son/yolov5/runs/detect/25_class/"
save_path="E:/Tuvis/GroundTruth/25_class_last/concat/"

for filename in glob.glob(first_image_path+'*.jpg',recursive=True):
    filename=os.path.basename(filename)
    filename= os.path.splitext(filename)
    print(filename[0])
    image_name=filename[0]
    img = cv2.imread(first_image_path+str(image_name)+".jpg")
    img2 = cv2.imread(second_image_path+str(image_name)+".jpg")
    
    im_h = cv2.hconcat([img, img2])
    
    cv2.imwrite(save_path+ str(image_name) +".jpg", im_h)