import cv2 as cv
import numpy as np

src = cv.imread('C:/Users/yigit/Desktop/Ders/python/Opencv301/03_OPENCVDE_GORUNTU_ISLEME/07_GAUSSIAN_BILATERAL_BLUR/fastimage.jpg')
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
cv.waitKey(0)

h, w = src.shape[:2]
dst = cv.bilateralFilter(src, 0,100, 20)#çap bilgisi , sigma color, sigma boşluğu(sigmalar ne kadar değişirse o kadar blur gelir)

result = np.zeros([h,w*2,3],dtype=src.dtype)
result[0:h,0:w] = src
result[0:h,w:2*w,:] = dst
cv.imshow("result", result)
cv.waitKey(0)

