import cv2 as cv

myimg = cv.imread("monalisa.jpg")

hsv = cv.cvtColor(myimg, cv.COLOR_BGR2HSV)

cv.imshow("Original", myimg)
cv.imshow("HSV", hsv)

cv.waitKey(0)


