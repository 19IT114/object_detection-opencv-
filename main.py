import numpy as np
import cv2


cap = cv2.VideoCapture(0)
cascade_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame,0)
    detections = cascade_classifier.detectMultiScale(frame, 1.1, 9)

    if(len(detections) > 0):
        (x,y,w,h) = detections[0]
        frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(255,255,255),2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()