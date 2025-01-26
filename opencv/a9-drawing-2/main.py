import cv2 as cv

"""
yukseklik=328
genislik=220
derinlik=3
"""

img = cv.imread("monalisa.jpg")



myColor=(125,150,12)
cv.circle(img,(120,120),50,myColor,-1)

cv.imshow("original",img)
# thickness -1 yapınca içi dolu

cv.waitKey(0)



