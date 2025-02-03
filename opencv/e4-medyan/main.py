import cv2 as cv

image = cv.imread("la.png")

medyan = cv.medianBlur(image, 7)

cv.imshow("Medyan",medyan)
cv.imshow("Original",image)
cv.waitKey(0)