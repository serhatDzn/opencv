import cv2 as cv

myvideo = cv.VideoCapture("video.mp4")
while True:
    control, capt = myvideo.read()
    if not control:
        print("video reading failed")
    cv.imshow("Image", capt)
    if cv.waitKey(20) & 0xFF==ord('p'):
        break