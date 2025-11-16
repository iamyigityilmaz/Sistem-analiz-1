import cv2 as cv

path = "C:/Users/yigit/Desktop/python/02_BASIC_OPERATIONS/07_BASIC_THRESHOLDING/"
src=cv.imread(path+"work.jpg")

T = 127#Threshold değeri (Threshold (eşikleme), bir görüntüde pikselleri belirlenen/otomatik bir eşik değerine göre iki sınıfa (örn. nesne–arkaplan) ayırarak basitleştirme ve segmentasyon yapan tekniktir.)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

for i in range(5):
    ret, binary = cv.threshold(gray, T, 255, i)
    cv.imshow("binary_" + str(i), binary)

cv.waitKey(0)
cv.destroyAllWindows()
