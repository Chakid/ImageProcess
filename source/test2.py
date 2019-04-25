# coding:utf-8

'''
读入正常图像并进行灰度化处理
'''

import cv2
import matplotlib.pyplot as plt
#读入原始图像
img=cv2.imread(r'img/cxk.jpg')
#灰度化处理
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#二值化处理
ret,thresh1=cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
# cv2.imshow('src', img)
# cv2.imshow('convert', gray)


cv2.waitKey()
cv2.destroyAllWindows()


