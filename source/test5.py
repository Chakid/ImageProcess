import cv2
import numpy as np
#读取彩色原图
src=cv2.imread('img/cxk.jpg',1)
gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
img_info=src.shape
image_height=img_info[0]
image_weight=img_info[1]
dst=np.zeros((image_height,image_weight,1),np.uint8)
for i in range(image_height):
    for j in range(image_weight):
        grayPixel=gray[i][j]
        dst[i][j]=255-grayPixel
cv2.imshow('gary',dst)
cv2.waitKey(0)