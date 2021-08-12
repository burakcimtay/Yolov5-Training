import glob
import cv2
import os

for filename in glob.glob('E:/Tuvis/GroundTruth/no_ok/groundtruths/'+'*.jpg',recursive=True):
    filename=os.path.basename(filename)
    filename= os.path.splitext(filename)
    print(filename[0])
    image_path=filename[0]
    img = cv2.imread('E:/Tuvis/GroundTruth/no_ok/groundtruths/'+str(image_path)+".jpg")

    with open("E:/Tuvis/GroundTruth/no_ok/labels/"+ str(image_path) +".txt", 'r') as f: 
        for line in f: 
            label=int(line[:2])
            
            if(label==0):
                cv2.putText(img,'NOT_OK',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
                cv2.imwrite('E:/Tuvis/GroundTruth/no_ok/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==1):
            #     cv2.putText(img,'ENINE_BANT',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==2):
            #     cv2.putText(img,'ATKI_KACIGI',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==3):
            #     cv2.putText(img,'CIMBIZ_IZI',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==4):
            #     cv2.putText(img,'hafif_taraz',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==5):
            #     cv2.putText(img,'ATKI_BIRIKIMI',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==6):
            #     cv2.putText(img,'NOPE',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==7):
            #     cv2.putText(img,'COZGU_KOPUGU',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==8):
            #     cv2.putText(img,'TEL_YOLU_COZGU_KACIGI',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==9):
            #     cv2.putText(img,'YANLIS_TEL',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==10):
            #     cv2.putText(img,'optik_lekesi',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==11):
            #     cv2.putText(img,'PAS_LEKESI',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==12):
            #     cv2.putText(img,'IPLIK_DUZGUNSUZLUGU',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==13):
            #     cv2.putText(img,'atkiyi_iceri_alma',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==14):
            #     cv2.putText(img,'cift_atki',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
            
            # elif(label==15):
            #     cv2.putText(img,'tefe',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==16):
            #     cv2.putText(img,'yarim_atki',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==17):
            #     cv2.putText(img,'yagli_iplik',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==18):
            #     cv2.putText(img,'AYAK_KACIGI',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==19):
            #     cv2.putText(img,'kirpik',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==20):
            #     cv2.putText(img,'DUGUM',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==21):
            #     cv2.putText(img,'IP_CEKMESI',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
            
            # elif(label==22):
            #     cv2.putText(img,'YAG_LEKESI',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==23):
            #     cv2.putText(img,'hafif_tefe',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)
                
            # elif(label==24):
            #     cv2.putText(img,'gergin_gevsek_tel',(100,125), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,255),2)
            #     cv2.imwrite('E:/Tuvis/GroundTruth/groundthruts_labels/'+ str(image_path) +".jpg", img)