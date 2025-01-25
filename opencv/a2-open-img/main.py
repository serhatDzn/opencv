import cv2

resim = cv2.imread("monalisa.jpg")

cv2.imshow("Resim", resim)

cv2.waitKey(2000) # two second sleep
