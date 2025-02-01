import cv2 as cv

myimg = cv.imread("monalisa.jpg",0)

kontrol, binary = cv.threshold(myimg, 127, 255, cv.THRESH_BINARY)

kontrol, binary2 = cv.threshold(myimg, 127, 255, cv.THRESH_BINARY_INV)


cv.imshow("Binary",binary)
cv.imshow("Binary Inverse",binary2)
cv.waitKey(0)