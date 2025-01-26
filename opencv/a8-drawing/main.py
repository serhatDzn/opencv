import cv2 as cv

"""
yukseklik=328
genislik=220
derinlik=3
"""

img = cv.imread("monalisa.jpg")

cv.rectangle(img,(30,10),(180,130),(255,0,0),2)

cv.imshow("Original",img)

cv.waitKey(0)





