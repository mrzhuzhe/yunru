import cv2
import numpy as np

assert float(cv2.__version__.rsplit('.', 1)[0]) >= 3, 'OpenCV version 3 or newer required.'

npz_calib_file = np.load('calibration_data.npz')

distCoeff = npz_calib_file['distCoeff']
intrinsic_matrix = npz_calib_file['intrinsic_matrix']

npz_calib_file.close()

DIM=(1280, 720)
intrinsic_matrix=np.array([
 [857.48296979,   0.,         968.06224829],
 [  0.,         876.71824265, 556.37145899],
 [  0.,           0.,           1.        ]
])
distCoeff=np.array([
    [-2.57614020e-01],
    [8.77086999e-02], 
    [-2.56970803e-04], 
    [-5.93390389e-04],
    [-1.52194091e-02]
])

# use Knew to scale the output
#Knew = K.copy()
#Knew[(0,1), (0,1)] = .4 * Knew[(0,1), (0,1)]

#newcameramatrix, _ = cv2.getOptimalCameraMatrix(
#    intrinsic_matrix, distCoeff, (DIM[0], DIM[1]), 1, (DIM[0], DIM[1])
#)

img = cv2.imread('10038.jpeg')
#img = cv2.resize(img, (1920, 1080), interpolation = cv2.INTER_AREA)
#img = cv2.copyMakeBorder(img,  180, 180, 320, 320, cv2.BORDER_CONSTANT)
img = cv2.copyMakeBorder(img,  180, 180, 320, 320, cv2.BORDER_CONSTANT)
#img_undistorted = cv2.fisheye.undistortImage(img, K, D=D, Knew=Knew)
img_undistorted = cv2.undistort(img, intrinsic_matrix, distCoeff, None)#, newcameramatrix)
#zcv2.imwrite('fisheye_sample_undistorted.jpg', img_undistorted)

#cv2.namedWindow("main", cv2.WINDOW_NORMAL)
#cv2.resizeWindow('image', int(1080*1.5), int(1920*1.5)) 
cv2.imshow('main', img_undistorted)
cv2.waitKey()