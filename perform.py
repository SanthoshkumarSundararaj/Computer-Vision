import numpy as np
import cv2


img1 = cv2.imread('ipad.jpeg')
e1 = cv2.getTickCount()
for i in xrange(5,49,2):
	img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2-e1)/cv2.getTickFrequency()
print t
cv2.imshow('ipad',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
