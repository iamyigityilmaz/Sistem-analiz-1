import cv2 as cv
path= "C:/Users/yigit/Desktop/python/02_BASIC_OPERATIONS/02_ARITHMETIC_OPERATIONS/02_IMAGE_PSEUDO_COLOR_ENGANCEMENT/"
src=cv.imread(path+"labirent.jpg")
cv.imshow("input",src)
cv.waitKey(0)
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.destroyWindow("input")
# Color Map için:(Aşağıdakiler temel yapılar)
#COLORMAP_'lerle renk tonu ayarlaması yapabilirsin.

dst = cv.applyColorMap(src, cv.COLORMAP_SUMMER)
cv.imshow("output",dst)
cv.waitKey(0)