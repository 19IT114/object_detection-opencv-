import cv2
face_cascade = cv2.CascadeClassifier("C:/Users/91989/PycharmProjects/pythonProject/haarcascades/haarcascade_frontalface_default.xml")

img = cv2.imread("C:/Users/91989/PycharmProjects/pythonProject/i.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
fa = face_cascade.detectMultiScale(gray,1.1,3)
i = 1
for(x,y,w,h) in fa:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.putText(img,str(i), (x,y), cv2.FONT_ITALIC, 1, (255,0,0), 3)
    i = i+1
cv2.rectangle(img,(0,0),(350,40),(255,0,0),-1)
cv2.putText(img,"Faces Detected = "+str(fa.shape[0]), (5,30), cv2.FONT_ITALIC, 1, (255,255,255), 3)

cv2.imshow("Face Count",img)
cv2.waitKey(0)
cv2.destroyAllWindows()