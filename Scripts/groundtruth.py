"""
Created by Burak Çimtay

You can change the paths and label names and run.
"""

import cv2
import matplotlib.pyplot as plt
import glob
import os

image_path="E:/Tuvis/Yolov5_Son/C6/c6_test/images/"
label_path="E:/Tuvis/Yolov5_Son/C6/c6_test/labels/"
save_path="E:/Tuvis/Yolov5_Son/C6/c6_test/groundtruths/"

for filename in glob.glob(image_path+'*.jpg',recursive=True):
    filename=os.path.basename(filename)
    filename= os.path.splitext(filename)
    print(filename[0])
    image_name=filename[0]
    img = cv2.imread(image_path+str(image_name)+".jpg")
    dh, dw, _ = img.shape

    fl = open(label_path + str(image_name) +".txt", 'r')
    data = fl.readlines()
    fl.close()

    for dt in data:

    # Split string to float
        _, x, y, w, h = map(float, dt.split(' '))

        l = int((x - w / 2) * dw)
        r = int((x + w / 2) * dw)
        t = int((y - h / 2) * dh)
        b = int((y + h / 2) * dh)
    
        if l < 0:
            l = 0
        if r > dw - 1:
            r = dw - 1
        if t < 0:
            t = 0
        if b > dh - 1:
            b = dh - 1
            
        with open(label_path+ str(image_name) +".txt", 'r') as f: 
            for line in f: 
                label=int(line[:2])
            
                if(label==0):
                    cv2.putText(img,'kirpik',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==1):
                    cv2.putText(img,'CIMBIZ_IZI',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==2):
                    cv2.putText(img,'atkiyi_iceri_alma',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==3):
                    cv2.putText(img,'COZGU_KOPUGU',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==4):
                    cv2.putText(img,'ENINE_BANT',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==5):
                    cv2.putText(img,'ATKI_BIRIKIMI',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==6):
                    cv2.putText(img,'gergin_gevsek_tel',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==7):
                    cv2.putText(img,'PAS_LEKESI',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==8):
                    cv2.putText(img,'tefe',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==9):
                    cv2.putText(img,'DUGUM',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)

                elif(label==10):
                    cv2.putText(img,'YAG_LEKESI',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==11):
                    cv2.putText(img,'cift_atki',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==12):
                    cv2.putText(img,'ATKI_KACIGI',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==13):
                    cv2.putText(img,'AYAK_KACIGI',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==14):
                    cv2.putText(img,'optik_lekesi',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            
                elif(label==15):
                    cv2.putText(img,'IPLIK_DUZGUNSUZLUGU',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==16):
                    cv2.putText(img,'yarim_atki',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==17):
                    cv2.putText(img,'TEL_YOLU_COZGU_KACIGI',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==18):
                    cv2.putText(img,'taraz',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==19):
                    cv2.putText(img,'YANLIS_TEL',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==20):
                    cv2.putText(img,'hafif_tefe',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)

                elif(label==21):
                    cv2.putText(img,'NOPE',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            
                elif(label==22):
                    cv2.putText(img,'yagli_iplik',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==23):
                    cv2.putText(img,'hafif_taraz',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                
                elif(label==24):
                    cv2.putText(img,'IP_CEKMESI',(l,t-10), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)    
        
        cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 2)

    cv2.imwrite(save_path+ str(image_name) +".jpg", img)
# plt.imshow(img)
# plt.show()