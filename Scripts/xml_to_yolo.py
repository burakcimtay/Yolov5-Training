# -*- coding: utf-8 -*-

from xml.dom import minidom
import os
import glob
import time

lut={}
lut["kirpik"]               =0
lut["CIMBIZ_IZI"]           =1
lut["atkiyi_iceri_alma"]    =2
lut["COZGU_KOPUGU"]         =3
lut["ENINE_BANT"]           =4
lut["ATKI_BIRIKIMI"]        =5
lut["atki_birikimi"]        =5
lut["gergin_gevsek_tel"]    =6
lut["PAS_LEKESI"]           =7
lut["tefe"]                 =8
lut["DUGUM"]                =9
lut["YAG_LEKESI"]           =10
lut["cift_atki"]            =11
lut["ATKI_KACIGI"]          =12
lut["AYAK_KACIGI"]          =13
lut["optik_lekesi"]         =14
lut["IPLIK_DUZGUNSUZLUGU"]  =15
lut["yarim_atki"]           =16
lut["TEL_YOLU_COZGU_KACIGI"]=17
lut["TEL_YOLU"]             =17
lut["taraz"]                =18
lut["YANLIS_TEL"]           =19
lut["hafif_tefe"]           =20
lut["NOPE"]                 =21
lut["yagli_iplik"]          =22
lut["hafif_taraz"]          =23
lut["IP_CEKMESI"]           =24

def convert_coordinates(size, box):
    dw = 1.0/size[0]
    dh = 1.0/size[1]
    x = (box[0]+box[1])/2.0
    y = (box[2]+box[3])/2.0
    w = box[1]-box[0]
    h = box[3]-box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def convert_xml2yolo( lut ):

    for fname in glob.glob("*.xml"):
        
        xmldoc = minidom.parse(fname)
        
        fname_out = (fname[:-4]+'.txt')

        with open(fname_out, "w") as f:

            itemlist = xmldoc.getElementsByTagName('object')
            size = xmldoc.getElementsByTagName('size')[0]
            width = int((size.getElementsByTagName('width')[0]).firstChild.data)
            height = int((size.getElementsByTagName('height')[0]).firstChild.data)

            for item in itemlist:
                # get class label
                classid =  (item.getElementsByTagName('name')[0]).firstChild.data
                if classid in lut:
                    label_str = str(lut[classid])
                else:
                    label_str = "-1"
                    print ("warning: label '%s' not in look-up table" % classid)

                # get bbox coordinates
                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width,height), b)
                #print(bb)

                f.write(label_str + " " + " ".join([("%.6f" % a) for a in bb]) + '\n')

        print ("wrote %s" % fname_out)
        time.sleep(0.1)



def main():
    convert_xml2yolo( lut )


if __name__ == '__main__':
    main()