import cv2 as cv
import numpy as np
from holoviews.plotting.bokeh.styles import font_size

path = "C:/Users/yigit/Desktop/python/02_BASIC_OPERATIONS/01_BASIC_OPERATIONS/03_CREATE_IMAGE/"

img = cv.imread(path + "opencv.png")
cv.namedWindow("image_create", cv.WINDOW_AUTOSIZE)
cv.imshow("image_create", img)
cv.waitKey(0)
cv.destroyAllWindows()

m1=np.copy(img)

m2=img
#255 beyaz renk 0 siyah renk
print(type(img))
img[0:200, 150:350, :]= 255
cv.imshow("m2", m2)
cv.waitKey(0)
#img.shape= resmin boyutu img.dtype=resmin tipi
m3=np.zeros(img.shape, img.dtype)
cv.imshow("m3", m3)
cv.waitKey(0)
#siyah kutu
m4=np.zeros([512,512],np.uint8)
cv.imshow("m4", m4)
cv.waitKey(0)
#gri kutu
m5=np.zeros([512,512],np.uint8)
m5[:,:] = 127
cv.imshow("m5", m5)
cv.waitKey(0)
#özel şekil(başta renkler)
img=np.ones((550,770,3))
black=(0,0,0)
red=(0,0,255)
green=(0,255,0)
#rectangel dikdörgen çizer, line=iki nokta arasında düz çizgi çizer
cv.rectangle(img,(480,250),(100,450),black,8)
cv.rectangle(img,(580,150),(200,350),black,8)
cv.line(img,(100,450),(200,350),black,8)
cv.line(img,(480,250),(580,150),black,8)
cv.line(img,(100,250),(200,150),black,8)
cv.line(img,(480,450),(580,350),black,8)

#yazı için başlangıç noktası, font kalınlığı, font boyu ve fontu
start_point=(150,100)
font_thickness=2
font_size=1
font=cv.FONT_HERSHEY_DUPLEX
#Resime yazı eklemek için
cv.putText(img,'www.harikaresimcizerim.com',start_point,font,font_size,red,font_thickness)
cv.imshow("dikdortgen",img)
cv.waitKey(0)