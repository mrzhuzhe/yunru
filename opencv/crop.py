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

def process(img, filters):
    accum = np.zeros_like(img)
    for kern in filters:
        fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
        np.maximum(accum, fimg, accum)
    return accum

img = cv2.imread('./imgs/test3.jpeg')

filters = build_filters()

_w0 = img.shape[0]
_h0 = img.shape[1]

_cr = int(402 / 2)
_cx = 278 + _cr
_cy = 718 + _cr

res = process(img, filters)

gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

mask = np.zeros((_w0,_h0),dtype=np.uint8)
cv2.circle(mask,(_cx,_cy),_cr,(255,255,255),-1,8,0)


out = gray*mask

cv2.circle(out,(_cx,_cy), int(_cr * 0.8),(0,0,0),-1,8,0)


cv2.imshow('img', out)
cv2.waitKey(0)

ret, thresh = cv2.threshold(out, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('thresh', thresh)
cv2.waitKey(0)

"""

gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

#cony_threshold = 50
#thresh = cv2.Canny(res, cony_threshold, 2 * cony_threshold)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


result = []          ## 空列表
for c in contours:    
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

#cv2.drawContours(img, result, -1, (255,0,0), 3)

cv2.imshow('res', res)
cv2.waitKey(0)

cv2.imshow('thresh', thresh)
cv2.waitKey(0)


cv2.imshow('img', img)
cv2.waitKey(0)
"""