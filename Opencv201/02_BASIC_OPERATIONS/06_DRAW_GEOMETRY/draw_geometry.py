import cv2 as cv
import numpy as np

image= np.zeros((512,512,3), dtype=np.uint8)

cv.rectangle(image, (100,100),(300,300),(255,0,0),2,cv.LINE_8,0)#kare
cv.circle(image, (256,256),50,(0,0,255),2,cv.LINE_8,0)
cv.ellipse(image, (256,256),(150,50),360,0,360,(0,255,0),2,cv.LINE_8,0)
cv.imshow("image",image)
cv.waitKey(0)
cv.destroyAllWindows()

for i in range(10000):
    image[:,:,:]=0
    x1 = np.random.rand()*512
    y1 = np.random.rand()*512
    x2 = np.random.rand()*512
    y2 = np.random.rand()*512

    b=np.random.randint(0,256)
    g=np.random.randint(0,256)
    r=np.random.randint(0,256)

    cv.line(image,(np.int_(x1),np.int_(y1)),(np.int_(x2),np.int_(y2)),(b,g,r),4,cv.LINE_8,0)
    cv.rectangle(image,(np.int_(x1),np.int_(y1)),(np.int_(x2),np.int_(y2)),(b,g,r),1,cv.LINE_8,0)
    cv.imshow("image",image)
    c=cv.waitKey(1)

    if c == 27:
        break