import cv2
from tracker import  *

#creating a tracker object
tracker = EuclideanDistTracker()

cap = cv2.VideoCapture("C:/Users/91989/PycharmProjects/pythonProject/Obj_detection/Sabar.mp4")  # READING THE FRAMES FROM THE VEDIO


#OBJECT DETECTION FROM A STABLE VEDIO

object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=60) #object detector for detecting the objects in our vedio using Background subtraction method

while True:
    ret, frame = cap.read()

    height, width, _ = frame.shape # getting
    print(height,width)


    #Extracting the region of Interest
    x_start = 150
    x_end = 360
    y_start = 0
    y_end = 640
    roi = frame[x_start:x_end,y_start:y_end] # Interested area for counting the objects
    #roi = frame[150:720, 850:1280]

    #Object Detection
    mask = object_detector.apply(roi) # applying mask to the original vedio frames to mark neccessary objects in white and unneccessary in black.
    _, mask =cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    countours, _ =  cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in countours:
        #Calculating area ang removing samller area to discard unneccessary object
        area = cv2.contourArea(cnt)

        if(area > 900):
            #cv2.drawContours(roi, [cnt], -1, (0,255,0), 2 )
            x,y,w,h = cv2.boundingRect(cnt) # bounding parameters of the objet
            cv2.rectangle(roi, (x,y) , (x+w, y+h), (0,255,0), 1)
            detections.append([x,y,w,h])

    #object tracker
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Region of Interest",roi)
    cv2.imshow("Frame", frame) # Displaying the original frames
    cv2.imshow("Mask", mask) # Displaying the masked frames

    key = cv2.waitKey(100)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()