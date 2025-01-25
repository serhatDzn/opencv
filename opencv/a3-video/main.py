import cv2 as cv

# video=cv.VideoCapture("video.mp4")
# while True:
#     kontrol, yakala=video.read()
#     if not kontrol:
#         print("Video Okuma İşlemi Başarısız!")
#     cv.imshow("Görüntü",yakala)
#     if cv.waitKey(20) & 0xFF==ord('p'):
#         break

myvideo = cv.VideoCapture("video.mp4")
while True:
    control, capt = myvideo.read()
    if not control:
        print("video reading failed")
    cv.imshow("Image", capt)
    if cv.waitKey(20) & 0xFF==ord('p'):
        break