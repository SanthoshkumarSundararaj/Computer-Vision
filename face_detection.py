import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
        # cap.read will return one status variable and the captured image  
	ret, img = cap.read() 

	# classifier will work on gray scale images
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# This will detect all the faces in the current frame and returns the co-ordinates of the faces
	# gray = input image 
	# 1.3,5 some parameters for getting accurate values
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	
	# we will be having multiple faces so we need get each and every faces and draw rectangle
	for (x,y,w,h) in faces:
		# input = colored image
		# x,y - first point : x+w,y+h - end point
		# 2 - thickness
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes :
			cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
	# to show the image
	cv2.imshow('img',img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

# release camera
cap.release()
cv2.destroyAllWindows()

