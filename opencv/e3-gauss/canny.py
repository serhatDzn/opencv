import cv2 as cv

image = cv.imread("monalisa.jpg")

bulanik = cv.GaussianBlur(image, (7,5), 2)

cv.imshow("Gaussian",bulanik)
cv.imshow("Original",image)

cv.waitKey(0)