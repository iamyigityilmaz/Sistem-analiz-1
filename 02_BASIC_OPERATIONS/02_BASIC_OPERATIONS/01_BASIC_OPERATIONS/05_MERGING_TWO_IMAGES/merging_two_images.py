import cv2 as cv
import numpy as np

path = "C:/Users/yigit/Desktop/python/02_BASIC_OPERATIONS/01_BASIC_OPERATIONS/05_MERGING_TWO_IMAGES/"

img1 = cv.imread(path + "rightimage.png")
img2 = cv.imread(path + "leftimage.png")

cv.imshow("sağ",img1)
cv.waitKey(0)
cv.imshow("sol",img2)
cv.waitKey(0)

horizontal = np.hstack((img1,img2))#hstack resimleri birleştirmetyi sağlar
cv.imshow("Birleştirilmiş",horizontal)
cv.waitKey(0)
cv.destroyAllWindows()

