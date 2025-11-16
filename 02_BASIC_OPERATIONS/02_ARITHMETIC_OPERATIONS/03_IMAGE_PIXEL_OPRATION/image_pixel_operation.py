import cv2 as cv
import numpy as np
path="C:/Users/yigit/Desktop/python/02_BASIC_OPERATIONS/02_ARITHMETIC_OPERATIONS/03_IMAGE_PIXEL_OPRATION/"

#resim1(siyah zemin üzerine sarı renk) np.zeros() tamamen 0 değerleriyle (siyah piksellerle) dolu bir boş görüntü veya matris oluşturu
src1=np.zeros(shape=(400,400,3),dtype=np.uint8)
src1[100:200,100:200,1] = 255
src1[100:200,100:200,2] = 255
cv.imshow("input1",src1)
cv.waitKey(0)

#resim2(siyah üzerine kırmızı)
src2=np.zeros(shape=(400,400,3),dtype=np.uint8)
src2[150:250,150:250,2] = 255
cv.imshow("input2",src2)
cv.waitKey(0)
#bitwise= mantıksal operatörleri piksel boyutunda yapılmasını sağlar
#and(matematikteki ve)
dst1=cv.bitwise_and(src1,src2)
cv.imshow("dst1",dst1)
cv.waitKey(0)

#or: İki pikselden  biri sıfırdan büyükse true
dst2=cv.bitwise_or(src1,src2)
cv.imshow("dst2",dst2)
cv.waitKey(0)

#xor pikseller farklıysa 255 (beyaz), aynıysa 0 (siyah) yapan işlemdir — yani sadece farklı bölgeleri gösterir.
dst3=cv.bitwise_xor(src1,src2)
cv.imshow("dst3",dst3)
cv.waitKey(0)

#not=pisel değerlerini ters çevirir
src=cv.imread(path+"opencv.png")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
cv.waitKey(0)

dst=cv.bitwise_not(src)
cv.imshow("dst",dst)
cv.waitKey(0)
