import open3d as o3d
import matplotlib.pyplot as plt
import numpy as np
import cv2

bag_filename = "zz_test_panda.bag"

bag_reader = o3d.t.io.RSBagReader()
bag_reader.open(bag_filename)

while not bag_reader.is_eof():
    im_rgbd = bag_reader.next_frame()
    # process im_rgbd.depth and im_rgbd.color
    depth_frame = im_rgbd.depth
    color_frame = im_rgbd.color
    if not depth_frame or not color_frame:
        continue

    # Convert images to numpy arrays
    depth_image = np.asanyarray(depth_frame)
    color_image = np.asanyarray(color_frame)

    # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.09), cv2.COLORMAP_JET)

    depth_colormap_dim = depth_colormap.shape
    color_colormap_dim = color_image.shape

    # If depth and color resolutions are different, resize color image to match depth image for display
    if depth_colormap_dim != color_colormap_dim:
        resized_color_image = cv2.resize(color_image, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]), interpolation=cv2.INTER_AREA)
        images = np.hstack((resized_color_image, depth_colormap))
    else:
        images = np.hstack((color_image, depth_colormap))

    # Show images   
    cv2.imshow('RealSense', images)
    cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
    cv2.setWindowProperty('RealSense', cv2.WND_PROP_TOPMOST, 1.0)
    cv2.waitKey(1)

bag_reader.close()
