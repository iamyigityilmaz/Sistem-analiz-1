import cv2 as cv
import os

path = "C:/Users/yigit/Desktop/Ders/python/Opencv201/02_BASIC_OPERATIONS/01_BASIC_OPERATIONS/01_LOAD_IMAGE/"
img = cv.imread(path + "akdeniz.jpg")

print(type(img))
#named window resim penceresi için
cv.namedWindow("opencv_test",cv.WINDOW_AUTOSIZE)
#imshow resimi göstermek için
cv.imshow("opencv_test",img)
#waitkey 0 sonsuza kadar çalışır ,pozitif sayı girildiğinde ekranda duracağı milisaniye sayısıdır.
cv.waitKey(0)

#pencereleri kapattığında hepsini kapatmak için
cv.destroyAllWindows()