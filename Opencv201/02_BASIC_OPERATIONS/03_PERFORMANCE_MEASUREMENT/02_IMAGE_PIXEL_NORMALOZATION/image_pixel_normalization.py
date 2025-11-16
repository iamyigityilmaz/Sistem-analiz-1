#Performans ölçme ve geliştirme teknikleri
import cv2 as cv
import numpy as np

path="C:/Users/yigit/Desktop/python/02_BASIC_OPERATIONS/03_PERFORMANCE_MEASUREMENT/02_IMAGE_PIXEL_NORMALOZATION/"
src= cv.imread(path+"opencv.png")

print(src.shape)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
print(gray.shape)
cv.imshow("gray",gray)
cv.waitKey(0)

gray = np.float32(gray)

# NORM_MINMAX
min_value, max_value, min_loc, max_loc = cv.minMaxLoc(gray)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))



means, stddev = cv.meanStdDev(gray)
print("mean: %.2f, stddev: %.2f" % (means[0][0], stddev[0][0]))

dst = np.zeros(gray.shape, dtype=np.float32)

cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
print(dst)


means, stddev = cv.meanStdDev(dst)
print("min_value: %.2f, max_value: %.2f" % (means[0][0], stddev[0][0]))

cv.imshow("NORM_MINMAX", dst)
cv.waitKey(0)

#Norm_Inf
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1, beta=0.0, norm_type=cv.NORM_INF)

print(dst)
cv.imshow("NORM_INF", np.uint8(dst*255))
cv.waitKey(0)

#NORM_L1
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_INF)
print(dst)
cv.imshow("NORM_L1", np.uint8(dst*10000000))
cv.waitKey(0)

#Norm_L2
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst , alpha=1.0, beta=0, norm_type=cv.NORM_L2)
print(dst)
cv.imshow("NORM_L2", np.uint8(dst*10000))
cv.waitKey(0)