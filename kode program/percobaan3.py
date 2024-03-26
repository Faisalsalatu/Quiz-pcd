import cv2


image = cv2.imread("miau-rgb.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,biner = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY) 

cv2.imshow("RGB", image )
cv2.imshow("GRAY", gray)
cv2.imshow("BINER", biner)

cv2.waitKey(0)
cv2.destroyAllWindows()