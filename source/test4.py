# coding:utf-8

'''
浮雕效果
'''

import cv2
import numpy as np
gray=cv2.imread('img/cxk.jpg',0)
imgInfo=gray.shape
height=imgInfo[0]
weight=imgInfo[1]

dst=np.zeros((height,weight,1),np.uint8)
for i in range(0,height):
    for j in range(0,weight-1):
        gray0=gray[i,j]
        gray1=gray[i,j+1]
        newp=gray0-gray1+150
        if newp>255:
            newp=255
        else:
            newp=0
        dst[i,j]=newp
cv2.imshow('dst',dst)
cv2.waitKey(0)