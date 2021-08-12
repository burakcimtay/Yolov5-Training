# Yolov5

## YOLO Nedir?

YOLO, konvolüsyonel sinir ağlarını (CNN) kullanarak nesne tespiti yapan bir algoritmadır. Açılımı “You Only Look Once“, yani “Sadece Bir Kez Bak“. Bu adın seçilmesinin nedeni algoritmanın nesne tespitini tek seferde yapabilecek kadar hızlı olmasıdır. YOLO algoritması çalışmaya başladığında görüntülerdeki veya videolardaki nesneleri ve bu nesnelerin koordinatlarını aynı anda tespit eder.

* Aşağıdaki Görsele Tıklayarak Örnek Çalışmayı Görebilirsiniz

[![YOLO](https://i1.wp.com/yapayzeka.ai/wp-content/uploads/2017/11/darknet_yolo_kapak.png?fit=1036%2C583&ssl=1)](http://www.youtube.com/watch?v=qE-aogEqGag&t=15s "YOLO")

## Environment Kurulumu
  * Yolo'yu kullanırken ekran kartını kullanabilmek için CUDA ve CUDNN kurulumu yapmanız gerekmektedir.
  * Öncelikle Powershell'i açıp pip komutumuzu güncelliyoruz.
  ```
  python -m pip install --upgrade pip
  ```
  * Daha sonra Virtualenv kurulumunu gerçekleştiriyoruz. 
  ```
  pip install virtualenv
  ```
  * Environment'i kurmak istediğiniz klasöre Powershell üzerinden gidiniz.
  ```
  cd ... Örn: cd C:\Anaconda3\envs
  ```
  * Bulunduğunuz klasöre "Yolov5" environmentini kurmak için Powershell'e bu komutu giriniz.

  ```
  virtualenv yolov5 -p Python_dizini Örn: (virtualenv yolov5 -p C:\Anaconda3\python.exe)
  ```

  * Powershell üzerinden bu environmenti aktifleştirmek için oluşturduğumuz environment içindeki Scripts klasörününde bulunan activate dosyasını Powershell üzerinden çalıştırın.

  ```
  (Örn: .\yolov5\Scripts\activate) ya da (cd .\yolov5\Scripts\ yazdıktan sonra .\activate komutunu girmeniz yeterli.)
  ```
  ![image](https://user-images.githubusercontent.com/73792173/125974212-89ffd573-1219-4f58-bf6a-aaf64fd26474.png)

  * Repomuzun içindeki yolov5 dizinine gidiyoruz.
  ```
  cd yolov5_dizini
  ```
  * Yolov5 için gerekli kütüphaneleri kuruyoruz. 
  ```
  pip install -r requirements.txt
  ```
  * Hata alırsanız aşağıdaki adımları kontrol ediniz.
    * Visual C++ kurulu olduğundan emin olun.
    * Environment'in doğru kurulduğundan emin olun.
    * Environment'in aktif olduğundan emin olun.

## Repo Düzeni

* Scripts klasöründe işimize yarayabilecek scriptler bulunuyor. 
* Data klasörü içinde YOLOv5 için train, val ve test datasetlerimizin nerede bulunduğu, kaç sınıf olduğu ve sınıf isimleri gibi bilgilerin bulunduğu bir yaml dosyamız var.
* Dataset klasöründe train, val ve test görsellerimizin ve etiketlerimizin bulunacağı klasörler var.
* yolov5 klasörü bizim yolov5'i çalıştıracağımız klasör.

## Eğitim

* Yolov5 environmentinin aktif olduğu Powersell'de modelimizi çalıştıracağımız yolov5 klasörünün içine giriyoruz.
```
cd ...
```
* Train.py dosyasının alabileceği parametreleri görebilmek için help komutunu kullanabiliriz.
```
python train.py --help
```
* Powershell'den train.py dosyasını parametrelerini problemimize uygun olacak şekilde girerek çalıştırıyoruz.
```
python train.py --img 640 --epochs 50 --data ..\data\data.yaml --cfg yolov5s.yaml --batch-size 64
                                                                                yolov5m        40
                                                                                yolov5l        24
                                                                                yolov5x        16
```
* Transfer learning yapmak istersek --weights komutunu da ekleyerek istediğimiz ağırlıkları eğitimimize transfer edebiliriz.
```
python train.py --img 640 --epochs 50 --data ..\data\data.yaml --cfg models\yolov5s.yaml --batch-size 64 --weights .\runs\train\weights\last.pt
                                                                                yolov5m               40
                                                                                yolov5l               24
                                                                                yolov5x               16
```
* Eğitim sonuçlarını ve ağırlıklarınızı görebilmek için yolov5 klasörünün içinde aşağıdaki dizine giriniz.
```
.\runs\train\
```

## Test

* Test.py dosyasının alabileceği parametreleri görebilmek için help komutunu kullanabiliriz.
```
python test.py --help
```
* Powershell'den test.py dosyasını parametrelerini problemimize uygun olacak şekilde girerek çalıştırıyoruz.
```
python test.py --data ..\data\data.yaml --weights .\runs\train\train_name\weights\best.pt --task test
```
* Test sonuçlarını ve ağırlıklarınızı görebilmek için yolov5 klasörünün içinde aşağıdaki dizine giriniz.
```
.\runs\test\
```

## Detect

* detect.py dosyasının alabileceği parametreleri görebilmek için help komutunu kullanabiliriz.
```
python test.py --help
```
* Powershell'den detect.py dosyasını parametrelerini problemimize uygun olacak şekilde girerek çalıştırıyoruz.
```
python .\detect.py --weights .\runs\train\train_name\weights\best.pt --conf 0.4 --source 0  # webcam
                                                                                         file.jpg  # image 
                                                                                         file.mp4  # video
                                                                                         path/  # directory
                                                                                         path/*.jpg  # glob
                                                                                         'https://youtu.be/NUsoVlDFqZg'  # YouTube video
                                                                                         'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```
* Yapılan tespitleri görebilmek için yolov5 klasörünün içinde aşağıdaki dizine giriniz.
```
.\runs\detect\
```
