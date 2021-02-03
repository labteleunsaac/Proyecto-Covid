import numpy as np
import time
import cv2

#cap = cv2.VideoCapture('rtsp://admin:admin@192.168.1.73/cam1/mpeg4')
cap = cv2.VideoCapture('rtsp://admin:admin@192.168.1.73:554/cam/realmonitor?channel=0&subtype=0')
#cap = cv2.VideoCapture(0)

while True:

    #print('About to start the Read command')
    ret, frame = cap.read()
    #print('About to show frame of Video.')
    cv2.imshow("Capturing",frame)
    #print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()