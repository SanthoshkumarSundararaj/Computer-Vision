import cv2

img = cv2.imread('lanes.jpg', 0)

#define the edge detec

edges = cv2.Canny(img,100,200)
cv2.imshow("",edges)
cv2.waitKey(5000)
cv2.destroyAllWindows()
