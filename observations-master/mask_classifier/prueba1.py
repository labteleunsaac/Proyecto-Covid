import cv2
import os
#from keras.models import load_model
import numpy as np
#from pygame import mixer
from time import time, sleep
from label_detect import classify_face
from glob import glob

filelist=glob("./*jpg")[:20]

for image in filelist:
    tic=time()
    img=cv2.imread(image,1)
    label = classify_face(img)
    toc=time()-tic
    cv2.imshow('out',img)
    print(toc, img.shape)
    sleep(2)