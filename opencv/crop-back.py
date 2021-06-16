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

alpha = 1
beta = 100

new_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

filters = build_filters()

_w0 = img.shape[0]
_h0 = img.shape[1]

_cr = int(402 / 2)
_cx = 278 + _cr
_cy = 718 + _cr

res = process(new_img, filters)

cv2.imshow('res', res)
cv2.waitKey(0)

gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', gray)
cv2.waitKey(0)

mask = np.zeros((_w0,_h0),dtype=np.uint8)
circle_img = cv2.circle(mask,(_cx,_cy),_cr, 1 ,-1)
masked_data = cv2.bitwise_and(gray, gray, mask=circle_img)
cv2.circle(masked_data,(_cx,_cy), int(_cr * 0.8), 0,-1)

cv2.imshow('masked_data', masked_data)
cv2.waitKey(0)

ret, thresh = cv2.threshold(masked_data, 172, 255, cv2.THRESH_BINARY)

cv2.imshow('thresh', thresh)
cv2.waitKey(0)
