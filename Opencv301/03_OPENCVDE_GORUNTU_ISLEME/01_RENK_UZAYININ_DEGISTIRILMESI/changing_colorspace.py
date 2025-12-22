#RENK UZAYINI DEĞİŞTİRMEK)CHANGING COLORSPACE)

import cv2 as cv

#HSV (HUE SATURATION VALUE [ÖZÜ,DOYGUNLUĞU , DEĞERİ])

img =cv.imread('opencv.png')
cv.namedWindow("rgb", cv.WINDOW_AUTOSIZE)
cv.imshow("rgb", img)
cv.waitKey(0)

#RGB'DEN GRİYE

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(0)

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)
cv.waitKey(0)
