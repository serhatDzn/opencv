
import cv2 as cv

print("OpenCV version :",cv.__version__)

oku = cv.imread("monalisa.jpg")

if oku is None:
    print("Resim dosyası bulunamadı.")
    exit()

(yukseklik, genislik, derinlik) = oku.shape

print(f"yukseklik={yukseklik}\ngenislik={genislik}\nderinlik={derinlik}")

cv.imshow("Image", oku)

cv.waitKey(0)


