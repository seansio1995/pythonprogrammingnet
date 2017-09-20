import urllib.request
import cv2
import numpy as np
import os

def get_images():
    pic_num=1
    read_list = urllib.request.urlopen("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02992529").read()
    for list0 in read_list.decode().split("\r\n"):
        #print(list0)
        try:
            print("Downloading {}.".format(list0))
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            pic_num+=1

get_images()
