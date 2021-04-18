# object_detection-opencv-

OpenCV comes with a trainer as well as detector. If you want to train your own classifier for any object like car, planes etc. you can use OpenCV to create one. Its full details are given here: Cascade Classifier Training.

OpenCV already contains many pre-trained classifiers for face, eyes, smile etc. Those XML files are stored in /haarcascades folder. 

FOR DETECTION OF FACE  and COUNTING:
1. First we need to load the required XML classifiers. 
2. Then load our input image (or video) and convert to grayscale mode.
3. Now we find the faces in the image. If faces are found, it returns the positions of detected faces as Rect(x,y,w,h).
4.  Once we get these locations, we can create a rectangle for the face.
5.  Count the total number of faces detected.


# Approach for object Detection and Tracking

In the absence of any a priori scene knowledge, the most widely used method for moving object detection is background subtraction . It consists of three steps; background initialization, foreground extraction, and background maintenance . A model of the observed scene is estimated using few initial frames during background initialization. 


1.Background subtraction (BS) is a common and widely used technique for generating a foreground mask (namely, a binary image containing the pixels belonging to moving objects in   the scene) by using static cameras.
2.As the name suggests, BS calculates the foreground mask performing a subtraction between the current frame and a background model, containing the static part of the scene or,     more in general, everything that can be considered as background given the characteristics of the observed scene.

# BackgroundSubtractorMOG2 
This algorithm was used in the current Project.
It is a Gaussian Mixture-based Background/Foreground Segmentation Algorithm. It is based on two papers by Z.Zivkovic, “Improved adaptive Gausian mixture model for background subtraction” in 2004 and “Efficient Adaptive Density Estimation per Image Pixel for the Task of Background Subtraction” in 2006. One important feature of this algorithm is that it selects the appropriate number of gaussian distribution for each pixel. (Remember, in last case, we took a K gaussian distributions throughout the algorithm). It provides better adaptibility to varying scenes due illumination changes etc.

As in previous case, we have to create a background subtractor object. Here, you have an option of selecting whether shadow to be detected or not. If detectShadows = True (which is so by default), it detects and marks shadows, but decreases the speed. Shadows will be marked in gray color.

#BackgroundSubtractorGMG
This algorithm combines statistical background image estimation and per-pixel Bayesian segmentation. It was introduced by Andrew B. Godbehere, Akihiro Matsukawa, Ken Goldberg in their paper “Visual Tracking of Human Visitors under Variable-Lighting Conditions for a Responsive Audio Art Installation” in 2012. As per the paper, the system ran a successful interactive audio art installation called “Are We There Yet?” from March 31 - July 31 2011 at the Contemporary Jewish Museum in San Francisco, California.

It uses first few (120 by default) frames for background modelling. It employs probabilistic foreground segmentation algorithm that identifies possible foreground objects using Bayesian inference. The estimates are adaptive; newer observations are more heavily weighted than old observations to accommodate variable illumination. Several morphological filtering operations like closing and opening are done to remove unwanted noise. You will get a black window during first few frames.

It would be better to apply morphological opening to the result to remove the noises.
