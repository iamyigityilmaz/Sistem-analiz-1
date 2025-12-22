import cv2 as cv
import numpy as np

src = cv.imread("keanu.jpg")
cv.imshow("keanu", src)
cv.waitKey(0)

edge = cv.Canny(src,100,300) #daha büyük değerleri kuvvetli kenarların bulunmasını sağlar
cv.imshow("edge", edge)
cv.waitKey(0)
