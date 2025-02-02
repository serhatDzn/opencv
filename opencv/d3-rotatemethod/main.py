import cv2 as cv

image = cv.imread("monalisa.jpg",0)

dondurme = cv.rotate(image, cv.ROTATE_180)
dondurme2 = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)

cv.imshow("Dondurulmus Resim", dondurme)
cv.imshow("Dondurulmus Resim 2", dondurme2)

cv.waitKey(0)

