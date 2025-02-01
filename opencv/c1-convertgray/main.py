import cv2 as cv

myimg = cv.imread("monalisa.jpg",0)

#gray_format = cv.cvtColor(myimg, cv.COLOR_BGR2GRAY)

cv.imshow("Orijinal", myimg)
#cv.imshow("Gri", gray_format)

cv.waitKey(0)
