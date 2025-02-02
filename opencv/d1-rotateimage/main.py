import cv2 as cv

image = cv.imread("monalisa.jpg")

yukseklik=328
genislik=220

merkez_nokta=(genislik/2,yukseklik/2)

d = cv.getRotationMatrix2D(merkez_nokta, -30, 2.0)

dondurme =cv.warpAffine(image, d, (genislik, yukseklik))

cv.imshow("Dondurulmus Resim", dondurme)
cv.imshow("Orijinal Resim", image)


cv.waitKey(0)