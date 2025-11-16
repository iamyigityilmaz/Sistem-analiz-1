import cv2 as cv
path = "C:/Users/yigit/Desktop/python/02_BASIC_OPERATIONS/01_BASIC_OPERATIONS/02_GRAY_IMAGE/"

img= cv.imread(path + "opencv.png")
cv.imshow("colored",img)
cv.waitKey(0)
cv.namedWindow("colored",cv.WINDOW_AUTOSIZE)
cv.destroyAllWindows()
#cvtColor
#BGR İLE RBG aynı şey
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(0)
cv.destroyAllWindows()

#kaydetmek için
cv.imwrite(path + "gray_opencv.png",gray)
cv.waitKey(0)
cv.destroyAllWindows()

#direkt gri olarak açmak için

img= cv.imread(path + "opencv.png",cv.IMREAD_GRAYSCALE)
cv.namedWindow("gray",cv.WINDOW_AUTOSIZE)
cv.imshow("gray",img)
cv.waitKey(0)