import numpy as np
import cv2
import os

cap = cv2.VideoCapture("black.avi")

currentframe = 0

while(True):
    
    ret, frame = cap.read()
 
    name = "./frame" + str(currentframe) + ".jpg"
    print("creating..." + name)    
    cv2.imwrite(name,frame)
    currentframe += 1
    
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()
