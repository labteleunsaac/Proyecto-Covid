import cv2
import os
#from keras.models import load_model
import numpy as np
#from pygame import mixer
import time
from label_detect import classify_face
from glob import glob  


#mixer.init()
#sound = mixer.Sound('alarm.wav')


#face = cv2.CascadeClassifier('/media/preeth/Data/prajna_files/Drowsiness_detection/haar_cascade_files/haarcascade_frontalface_alt.xml')
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('rtsp://admin:admin@192.168.1.73/cam1/mpeg4')
#cap = cv2.VideoCapture('rtsp://admin:admin@192.168.1.73:554/cam/realmonitor?channel=0&subtype=0')
#cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
score=0
thicc=2
#faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))
while(True):
    ret, frame = cap.read()
    height,width = frame.shape[:2]
    label = classify_face(frame)
    if(label == 'with_mask'):
        print("No Beep")
    else:
        #sound.play()
        print("Beep")   
    cv2.putText(frame,str(label),(100,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()