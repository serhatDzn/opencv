import cv2 as cv

"""
yukseklik=328
genislik=220
derinlik=3
"""

img = cv.imread("monalisa.jpg")

cv.imshow("Original",img)

clipped = img[60:300,30:140]

cv.imshow("clipped", clipped)
cv.waitKey(0)





