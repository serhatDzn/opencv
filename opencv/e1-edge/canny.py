import cv2 as cv

image = cv.imread("canny.jpg",0)

kenar = cv.Canny(image, 100, 200)

cv.imshow("Kenarlar", kenar)
cv.imshow("Orijinal Resim", image)

cv.waitKey(0)