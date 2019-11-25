import cv2
import sys

# define a video source
cap = cv2.VideoCapture(0)

bg_sub = cv2.bgsegm.createBackgroundSubtractorMOG(history=10)

#bg_img = bg_sub.getBackgroundImage()
#cv2.imwrite('bg_img.jpg', bg_img)
while True:
	
	#fetch the image
	_, frame = cap.read()

	#process it 
	fg_mask = bg_sub.apply(frame)
	#bg_img = bg_sub.getBackgroundImage();	

	im2, contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)	
	#cv2.drawContours(frame, contours, -1, (0,255,0), 3)

	
	
	for c in contours:
		x, y, w, h = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
	#display and close if 'q' is pressed
	cv2.imshow("", frame)
	#cv2.imshow("", bg_img)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
