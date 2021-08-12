import glob
import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, IncrementalPCA
import os
import cv2

path = "E:/Tuvis/Yolov5_Son/C6/data/images/"
save_path = "E:/Tuvis/Yolov5_Son/C6/data/PCA/"

k=100
for filename in glob.glob(path + "/*.jpg"):
    
    filename=os.path.basename(filename)
    filename= os.path.splitext(filename)
    print(filename[0])
    image_name=filename[0]
    
    image_raw = cv2.imread(path+str(image_name)+".jpg")
    # print(image_raw.shape)
    # Displaying the image
    plt.figure(figsize=[12,8])
    #plt.imshow(image_raw)
    image_sum = image_raw.sum(axis=2)
    # print(image_sum.shape)

    image_bw = image_sum/image_sum.max()
    # print(image_bw.max())
    plt.figure(figsize=[12,8])
    # plt.imshow(image_bw, cmap=plt.cm.gray)
    
    pca = PCA()
    pca.fit(image_bw)
    
    # #Resmin %95'ini oluşturmak için gerekli varyans belirlenir.
    
    # var_cumu = np.cumsum(pca.explained_variance_ratio_)*100

    # k = np.argmax(var_cumu>95)
    # print("Number of components explaining 95% variance: "+ str(k)) 

    # #Birkaç fotografa bakılır uygun k degeri seçilir. Sonra bu satır yorum yapılır.
    
    # plt.figure(figsize=[12,8])
    # plt.title('Cumulative Explained Variance explained by the components')
    # plt.ylabel('Cumulative Explained variance')
    # plt.xlabel('Principal components')
    # plt.axvline(x=k, color="k", linestyle="--")
    # plt.axhline(y=95, color="r", linestyle="--")
    # ax = plt.plot(var_cumu)
    # plt.savefig(save_path+ "k_degeri" +".jpg")
    
    ipca = IncrementalPCA(n_components=k)
    image_recon = ipca.inverse_transform(ipca.fit_transform(image_bw))
    #plt.imshow(image_recon,cmap = plt.cm.gray)
    plt.imsave(save_path+ str(image_name) +".jpg", image_recon,cmap = plt.cm.gray)
    plt.close('all')


