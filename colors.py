import numpy as np
import time
import argparse
import cv2
# load the image
image = cv2.imread('Cropped/croppedsatellite.png')
imageYCB = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
imageLAB = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def filter(thresh):
	bgr = [40,180,40]
	minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
	maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
	maskBGR = cv2.inRange(image, minBGR, maxBGR)
	resultBGR = cv2.bitwise_and(image, image, mask = maskBGR)

	#convert this array to 3D, then convert it to HSV and take the first element 
	# this will be same as shown in the above figure [65, 229, 158]
	hsv = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]
	 
	minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
	maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])

	maskHSV = cv2.inRange(imageHSV, minHSV, maxHSV)
	resultHSV = cv2.bitwise_and(imageHSV, imageHSV, mask = maskHSV)

	#convert 1D array to 3D, then convert it to YCrCb and take the first element 
	ycb = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2YCrCb)[0][0]

	minYCB = np.array([ycb[0] - thresh, ycb[1] - thresh, ycb[2] - thresh])
	maxYCB = np.array([ycb[0] + thresh, ycb[1] + thresh, ycb[2] + thresh])

	maskYCB = cv2.inRange(imageYCB, minYCB, maxYCB)
	resultYCB = cv2.bitwise_and(imageYCB, imageYCB, mask = maskYCB)

	#convert 1D array to 3D, then convert it to LAB and take the first element 
	lab = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2LAB)[0][0]

	minLAB = np.array([lab[0] - thresh, lab[1] - thresh, lab[2] - thresh])
	maxLAB = np.array([lab[0] + thresh, lab[1] + thresh, lab[2] + thresh])

	maskLAB = cv2.inRange(imageLAB, minLAB, maxLAB)
	resultLAB = cv2.bitwise_and(imageLAB, imageLAB, mask = maskLAB)

	cv2.imwrite("thresh = "+ str(thresh)+".jpg", resultBGR)
for thresh in range(60,120):
    filter(thresh)
