import cv2 as cv

"""
yukseklik=328
genislik=220
derinlik=3
"""

img = cv.imread("monalisa.jpg")

color = (0,0,255)
img = cv.putText(img,"Mona Riza", (50,50),cv.FONT_ITALIC,1,color,2)

cv.imshow("Resim",img)

cv.waitKey(0)



