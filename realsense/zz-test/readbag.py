import open3d as o3d
import matplotlib.pyplot as plt
import numpy as np

bag_filename = "zz_test_panda.bag"

bag_reader = o3d.t.io.RSBagReader()
bag_reader.open(bag_filename)
#while not bag_reader.is_eof():
im_rgbd = bag_reader.next_frame()
    # process im_rgbd.depth and im_rgbd.color
bag_reader.save_frames('./panda/frames')

#depth_image = np.asarray(im_rgbd.depth)

bag_reader.close()
