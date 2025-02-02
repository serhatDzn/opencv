import cv2 as cv

image = cv.imread("monalisa.jpg",0)

yukseklik=328
genislik=220

dikinedondurme =cv.flip(image, 0)

yatayadondurme =cv.flip(image, 1)

tumdonme =cv.flip(image, -1)

cv.imshow("Dikine Dondurulmus Resim", dikinedondurme)
cv.imshow("Yatay Dondurulmus Resim", yatayadondurme)
cv.imshow("Tum Donmus Resim", tumdonme)

cv.waitKey(0)

