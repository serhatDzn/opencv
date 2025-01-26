import cv2 as cv

image = cv.imread("monalisa.jpg")

(mavi,yesil,kirmizi) = image[15,15]

print(f"""b- {mavi}
g- {yesil}
r- {kirmizi}""")

