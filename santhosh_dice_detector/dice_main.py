import cv2 
import numpy as np
import sys

# read original image
img = cv2.imread("8.png")

# create binary image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
binary = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#cv2.imshow("adapt",binary)
edges = cv2.Canny(img,100,200)
#cv2.imshow("canny",edges)
# find contours
(_, contours, _) = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
	area = cv2.contourArea(contours[c])
	if area > 2000 & area <3500:
	 	x,y,w,h = cv2.boundingRect(c)

        #contour = cv2.drawContours(img, contours, -1, (0, 0, 255), 5)
         	con = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

#rect= cv2.minAreaRect(c)
#box = cv2.boxPoints(rect)
#box = np.int0(box)
#contour = cv2.drawContours(img, contours, -1, (0, 0, 255), 5)
cv2.imshow("con",con)

# display original image with contours
#cv2.namedWindow("output", cv2.WINDOW_NORMAL)
#cv2.imshow("output", img)
cv2.waitKey(0)
