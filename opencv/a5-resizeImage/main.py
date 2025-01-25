import cv2 as cv

image = cv.imread("monalisa.jpg")

(x,y,z) = image.shape
x*=2
y*=2
z*=2
shapedImage=cv.resize(image, (y,x))

cv.imshow("Original",image)

cv.imshow("Doubled",shapedImage)

cv.waitKey(0)