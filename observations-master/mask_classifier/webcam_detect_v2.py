import numpy as np
import time
import cv2


#cap = cv2.VideoCapture('rtsp://admin:admin@192.168.1.73:554/cam/realmonitor?channel=0&subtype=0')
#cap = cv2.VideoCapture(0)

#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
i=0
for i in range(5):
    
    
    cap = cv2.VideoCapture('rtsp://admin:admin@192.168.1.73/cam1/mpeg4')

    #print('About to start the Read command')
    ret, frame = cap.read()
    #print('About to show frame of Video.')
    print(frame.shape)
    ROI = frame[200:1000, 650:1300]
    cv2.imshow("Capturing",ROI)
    print(ROI.shape)
    
    cv2.imwrite('img'+str(i)+'.png', ROI)
    #print('Running..')
    time.sleep(1)
    i+=1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()