#   在预先就应该去除噪声
#   需要相机校准

import numpy as np
import cv2 as cv
import sys
from matplotlib import pyplot as plt

#   三通道
img = cv.imread('test.jpeg')
if img is None:
    sys.exit("Could not read the image.")

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#   cv.imshow('imgray', imgray)

#   卷积去噪声  https://docs.opencv.org/3.4/d4/d13/tutorial_py_filtering.html
#   kernel = np.ones((5,5),np.float32)/25
#   dst = cv.filter2D(img,-1,kernel)

#   同型去噪    https://docs.opencv.org/3.4/d9/d61/tutorial_py_morphological_ops.html
#   kernel = np.ones((5,5),np.uint8)
#   opening = cv.morphologyEx(imgray, cv.MORPH_OPEN, kernel)

"""
#   mask    模式
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_blue = np.array([0,0,0])
upper_blue = np.array([50,50,50])
# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_blue, upper_blue)
# Bitwise-AND mask and original image
res = cv.bitwise_and(img,img, mask= mask)
cv.imshow('frame',img)
cv.imshow('mask',mask)
cv.imshow('res',res)
"""

"""
#  不同阀值方式
ret,thresh1 = cv.threshold(imgray,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(imgray,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(imgray,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(imgray,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(imgray,127,255,cv.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [imgray, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
"""

# 阀值二值化
ret, thresh = cv.threshold(imgray, 50, 255, cv.THRESH_BINARY_INV)

#cv.imshow('Approx Poly DP', thresh)


contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#   矩  https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html
cnt = contours[0]
M = cv.moments(cnt)
print( M )

#   显示所有等高线
#cv.drawContours(imgray, contours, -1, (255,0,0), 3)
#cv.imshow('contours', imgray)



# Iterate through each contour
result = []          ## 空列表
for c in contours:
    x,y,w,h = cv.boundingRect(c)
    if (w > 100):
        #cv.rectangle(imgray, (x, y), (x+w, y+h), (255, 0, 255), 2)
        rect = cv.minAreaRect(c)
        box = cv.boxPoints(rect)
        box = np.int0(box)
        result.append(box) 

#   cv.imshow('Bounding Rectangle', imgray)
cv.drawContours(imgray, result, -1, (255,0,0), 3)
cv.imshow('contours', imgray)
print("result contour", result)

# Iterate through each contour and compute the approx contour
"""
#   用多边形围起来
for c in contours:
    accuracy = 0.03 * cv.arcLength(c, True)
    approx = cv.approxPolyDP(c, accuracy, True)
    cv.drawContours(imgray, [approx], 0, (255, 255, 0), 2)
    cv.imshow('Approx Poly DP', imgray)
"""

# 随便按个按钮关闭
cv.waitKey(0)
#cv.destroyAllWindows()
