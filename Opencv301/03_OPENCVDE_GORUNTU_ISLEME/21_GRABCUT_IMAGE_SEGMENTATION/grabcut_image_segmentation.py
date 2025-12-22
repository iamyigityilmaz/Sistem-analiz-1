import cv2 as cv
import numpy as np

src = cv.imread("C:/Users/yigit/Desktop/Ders/python/Opencv301/03_OPENCVDE_GORUNTU_ISLEME/21_GRABCUT_IMAGE_SEGMENTATION/m1.jpg")

src = cv.resize(src,(0,0), fx=0.5, fy=0.5)

r = cv.selectROI("input",src, False)

roi = src[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
img = src.copy()

cv.rectangle(img,
             (int(r[0]), int(r[1])),
             (int(r[0] + r[2]), int(r[1] + r[3])),
             (0,0,255),2)

mask = np.zeros(src.shape[:2], dtype=np.uint8)

rect = (int(r[0]),int(r[1]),int(r[2]),int(r[3]))

bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)

cv.grabCut(src, mask, rect, bgdmodel, fgdmodel, 11, mode=cv.GC_INIT_WITH_RECT)
print("BG Model:", bgdmodel)
print("FG Model:", fgdmodel)
print("Mask:", mask)

mask2 = np.where((mask==1) + (mask==3), 255, 0).astype("uint8")

result = cv.bitwise_and(src, src, mask=mask2)
cv.imshow("roi", roi)
cv.imshow("result", result)
cv.waitKey(0)
