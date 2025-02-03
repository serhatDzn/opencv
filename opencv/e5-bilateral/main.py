import cv2 as cv

image = cv.imread("la.png")

bilateral = cv.bilateralFilter(image, 15, 95, 95)

cv.imshow("Bilateral",bilateral)
cv.imshow("Original",image)

cv.waitKey(0)