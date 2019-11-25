import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer/trainingData.yml")
id = 0
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

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
		id,conf = rec.predict(gray[y:y+h,x:x+w])
		cv2.putText(cv2.putText(img),str(id),(x,y+h),font,255)		
	# to show the image
	cv2.imshow('img',img)
	if(cv2.waitKey(1)==ord('q')):
		break

# release camera
cap.release()
cv2.destroyAllWindows()

