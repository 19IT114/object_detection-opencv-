# object_detection-opencv-

OpenCV comes with a trainer as well as detector. If you want to train your own classifier for any object like car, planes etc. you can use OpenCV to create one. Its full details are given here: Cascade Classifier Training.

OpenCV already contains many pre-trained classifiers for face, eyes, smile etc. Those XML files are stored in /haarcascades folder. 

FOR DETECTION OF FACE  and COUNTING:
1. First we need to load the required XML classifiers. 
2. Then load our input image (or video) and convert to grayscale mode.
3. Now we find the faces in the image. If faces are found, it returns the positions of detected faces as Rect(x,y,w,h).
4.  Once we get these locations, we can create a rectangle for the face.
5.  Count the total number of faces detected.
