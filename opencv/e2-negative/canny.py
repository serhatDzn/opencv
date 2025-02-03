import cv2 as cv

image = cv.imread("canny.jpg",0)

negative = cv.bitwise_not(image)

cv.imshow("Negatif Resim", negative)
cv.imshow("Orijinal Resim", image)

cv.waitKey(0)