#!/usr/bin/env python

'''
Stitching sample
================
Show how to use Stitcher API from python in a simple way to stitch panoramas
or scans.
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv

import argparse
import sys

from os import walk

modes = (cv.Stitcher_PANORAMA, cv.Stitcher_SCANS)

parser = argparse.ArgumentParser(prog='stitching.py', description='Stitching sample.')
parser.add_argument('--mode',
    type = int, choices = modes, default = cv.Stitcher_PANORAMA,
    #type = int, choices = modes, default = cv.Stitcher_SCANS,
    help = 'Determines configuration of stitcher. The default is `PANORAMA` (%d), '
         'mode suitable for creating photo panoramas. Option `SCANS` (%d) is suitable '
         'for stitching materials under affine transformation, such as scans.' % modes)
parser.add_argument('--output', default = 'result.jpg',
    help = 'Resulting image. The default is `result.jpg`.')
#parser.add_argument('img', nargs='+', help = 'input images')

__doc__ += '\n' + parser.format_help()
#__path = "./stitching/"
__path = "./imgs/wheel/"

def main():
    args = parser.parse_args()

    # read input images
    imgs = []

    for (dirpath, dirnames, filenames) in walk(__path):
        for filename in filenames:
            print(filename)
            img = cv.imread(__path + filename)
            imgs.append(img)

    """
    for img_name in args.img:
        img = cv.imread(__path + img_name)
        if img is None:
            print("can't read image " + img_name)
            sys.exit(-1)
        imgs.append(img)
    """

    stitcher = cv.Stitcher.create(args.mode)
    status, pano = stitcher.stitch(imgs)

    if status != cv.Stitcher_OK:
        print("Can't stitch images, error code = %d" % status)
        sys.exit(-1)

    cv.imwrite(args.output, pano)
    print("stitching completed successfully. %s saved!" % args.output)

    print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()

# python stiching.py 1.jpeg 2.jpeg 3.jpeg 4.jpeg 5.jpeg 6.jpeg 7.jpeg 8.jpeg