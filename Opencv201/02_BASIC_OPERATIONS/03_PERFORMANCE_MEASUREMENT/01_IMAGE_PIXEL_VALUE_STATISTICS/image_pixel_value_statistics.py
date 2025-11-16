import cv2 as cv
import numpy as np

path="C:/Users/yigit/Desktop/python/02_BASIC_OPERATIONS/03_PERFORMANCE_MEASUREMENT/01_IMAGE_PIXEL_VALUE_STATISTICS/"

src = cv.imread(path + "gray_opencv.png", cv.IMREAD_GRAYSCALE)

#MinMaxLoc(Minimum, maximum , location)

min_value , max_value , min_loc ,max_loc = cv.minMaxLoc(src)
print("min_value: %.2f, max_value: %.2f"%(min_value , max_value))#resimin içindeki minimum ve maksimum değeri getirir.

print("min loc:", min_loc,",","max loc:",max_loc)#minimum ve maximum değerin lokasyonunu bulur

#meanStdDev(ortalama ve standart sapma)(means ortalama , stddev standart sapma)
means,stddev = cv.meanStdDev(src)
print("mean: %.2f, stddev: %.2f" % (means.item(), stddev.item()))

src[np.where(src< means)] = 0 #ortalamanın altında olan  değerlere 0 atar
src[np.where(src> means)] = 255 #ortalamanın üzerinde olan değerlere 1 atar
cv.imshow("binary", src)
cv.waitKey(0)
cv.destroyAllWindows()


