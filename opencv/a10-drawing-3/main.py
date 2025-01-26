import cv2 as cv

"""
yukseklik=328
genislik=220
derinlik=3
"""

img = cv.imread("monalisa.jpg")

p1 = (200,300)
p2= (30,30)
lineCol = (55,152,255)
thickNesss = 4


cv.line(img,p1,p2,lineCol,thickNesss)

cv.imshow("image",img)

cv.waitKey(0)



