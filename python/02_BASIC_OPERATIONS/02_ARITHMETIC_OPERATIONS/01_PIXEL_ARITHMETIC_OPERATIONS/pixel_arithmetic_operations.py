import cv2 as cv
import numpy as np

path = "C:/Users/yigit/Desktop/python/02_BASIC_OPERATIONS/02_ARITHMETIC_OPERATIONS/01_PIXEL_ARITHMETIC_OPERATIONS/"

src1=cv.imread(path+"test0.png")
src2=cv.imread(path+"test1.png")

#hight(yükseklik), weight(genişlik) ch(kanal sayısı) bilgisi öğrenmek için ch=renk yapısı (gri tonu(1), rgp(3),alfa kabalı(rgb+A)

h,w,ch=src1.shape

print(("h,w,ch",h,w,ch))

#Amaç piksellerin toplama, çıkartma, çarpma , bölünme
#add(toplama)
add_result=np.zeros(src1.shape,src2.dtype)
cv.add(src1,src2,add_result)
cv.imshow("add_result",add_result)
cv.waitKey(0)

#subtract(çıkartma)
sub_result=np.zeros(src1.shape,src2.dtype)
cv.subtract(src1,src2,sub_result)
cv.imshow("sub_result",sub_result)
cv.waitKey(0)

#multiply(çarpma)
mul_result=np.zeros(src1.shape,src2.dtype)
cv.multiply(src1,src2,mul_result)
cv.imshow("mul_result",mul_result)
cv.waitKey(0)

#divide(bölme)
div_result=np.zeros(src1.shape,src2.dtype)
cv.divide(src1,src2,div_result)
cv.imshow("div_result",div_result)
cv.waitKey(0)
