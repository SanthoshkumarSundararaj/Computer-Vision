#import cv2
#import numpy as np
#from matplotlib import pyplot as plt

#cap = cv2.VideoCapture("dice.avi")  
#ret, img = cap.read()  

#edges = cv2.Canny(img,100,200)

#k = cv2.waitKey(30) & 0xff                              # press [Esc] to exit.


#cv2.destroyAllWindows() 


import numpy as np
import cv2

cap = cv2.VideoCapture("dice.avi")

while(True):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('Original',frame)
	edges = cv2.Canny(frame,100,200)
	cv2.imshow('Edged',edges)
	
	blur = cv2.GaussianBlur(gray, (5,5), 0)
	(t, binary) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY)
	(_, contours, _) = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(edges, contours, -1, (0,0,255), 5)

	
	if cv2.waitKey(50) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()  
