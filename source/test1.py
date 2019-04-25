# coding:utf-8

'''
RGB图像底片效果
'''

import cv2

src = cv2.imread(r'img/cxk.jpg')

dist = 255 - src

cv2.imshow('src', src)
cv2.imshow('convert', dist)

cv2.waitKey()
cv2.destroyAllWindows()