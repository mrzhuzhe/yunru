import numpy as np
import cv2

def build_filters():
    filters = []
    ksize = 31
    for theta in np.arange(0, np.pi, np.pi / 16):
        kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
        kern /= 1.5*kern.sum()
        filters.append(kern)
    return filters

filters = build_filters()

img = cv2.imread('./imgs/test5.jpeg')


def process(img, filters):
    accum = np.zeros_like(img)
    for kern in filters:
        fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
        np.maximum(accum, fimg, accum)
    return accum


res = process(img, filters)


gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)

#cony_threshold = 50
#thresh = cv2.Canny(res, cony_threshold, 2 * cony_threshold)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


result = []          ## 空列表
for c in contours:    
    x,y,w,h = cv2.boundingRect(c)
    #if (w > 0 and h > 0 and w < 50 and h < 50):
        #if ( w/h < 2 and w/h > 0.5):
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #box = cv2.boxPoints(rect)
    #box = np.int0(box)
    #if ( w/h < 2 and w/h > 0.5):
    #result.append(box) 

#cv2.drawContours(img, result, -1, (255,0,0), 3)

cv2.imshow('res', res)
cv2.waitKey(0)

cv2.imshow('thresh', thresh)
cv2.waitKey(0)


cv2.imshow('img', img)
cv2.waitKey(0)