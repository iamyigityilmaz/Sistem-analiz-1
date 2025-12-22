import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

def process(image, opt=0):
    if opt == 0:
        return cv.bitwise_not(image)
    elif opt == 1:
        return cv.GaussianBlur(image, (15,15), 0)
    elif opt == 2:
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        return cv.Canny(gray, 100, 200)

index = 0

while True:
    ret, frame = capture.read()
    if not ret:
        break

    cv.imshow("video-input", frame)

    c = cv.waitKey(50) & 0xFF

    if c in [49, 50, 51]:  # 1,2,3
        index = c - 49

    result = process(frame, index)
    cv.imshow("result", result)

    if c == 27:  # ESC
        break

capture.release()
cv.destroyAllWindows()
