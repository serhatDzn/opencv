import cv2 as cv


resim = cv.imread("monalisa.jpg")

kopya = resim.copy()

cv.imshow("Orijinal",resim)
cv.imshow("Kopya",kopya)
cv.waitKey(0)