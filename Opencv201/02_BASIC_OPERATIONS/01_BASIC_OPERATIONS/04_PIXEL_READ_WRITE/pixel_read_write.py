import cv2 as cv
import numpy as np
import os

path = "C:/Users/yigit/Desktop/Ders/python/Opencv201/02_BASIC_OPERATIONS/01_BASIC_OPERATIONS/04_PIXEL_READ_WRITE/"
img = cv.imread(os.path.join(path, "opencv.png"))  # <-- os.path.join ile doğru birleştirme

h, w, ch = img.shape #resimin pixel bilgilerini tanımlamak için
print("h , w, ch", h, w, ch)

for row in range(h):
    for col in range(w):
        b,g,r = img[row,col]
        b=255-b
        g=255-g
        r=255-r
        img[row,col]=(b,g,r)
cv.imshow("output",img)
cv.waitKey(0)
cv.destroyAllWindows()