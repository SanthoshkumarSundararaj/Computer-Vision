import numpy as np
import cv2

img = cv2.imread('ipad.jpeg',0)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('ipadgray.png',img)
