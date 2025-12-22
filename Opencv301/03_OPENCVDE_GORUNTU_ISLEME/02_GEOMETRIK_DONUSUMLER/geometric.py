import cv2 as cv
import numpy as np

#shifting(kaydırma)

img = cv.imread("opencv.png")

rows = img.shape[0]#satırların bilgisi
cols = img.shape[1]#sütınşarom bilgisi
print(rows,cols)

M=np.float32([[1,0,140],[0,1,90]])

shifted=cv.warpAffine(img,M,(cols,rows))
print(shifted)

cv.imshow("original",img)
cv.waitKey(0)
cv.imshow("shifted",shifted)
cv.waitKey(0)
cv.destroyAllWindows()

#rotation(döndürme)
res= cv.resize(img,None , fx=0.2, fy=0.2 ,interpolation=cv.INTER_CUBIC)
M=cv.getRotationMatrix2D((cols/2,rows/2),90,1)
dst=cv.warpAffine(res,M,(cols,rows))


dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow("dst",dst)
cv.waitKey(0)

#scaling(düzenleme)

res= cv.resize(img,None , fx=0.2, fy=0.2 ,interpolation=cv.INTER_CUBIC)
cv.imshow("resized",res)
cv.waitKey(0)

#küçük resim
rows =res.shape[0]
cols =res.shape[1]

M = np.float32([[1,0,200],[0,1,90]])
shifted=cv.warpAffine(res,M,(cols,rows))
cv.imshow("orjinal",res)
cv.waitKey(0)

shifted=cv.warpAffine(res,M,(cols,rows))
cv.imshow("shifted",shifted)
cv.waitKey(0)