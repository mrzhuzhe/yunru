# 为什么要逐帧读，

import open3d as o3d
import matplotlib.pyplot as plt

print("Read Redwood dataset")
color_raw = o3d.io.read_image("./frames/color/00017.jpg")
depth_raw = o3d.io.read_image("./frames/depth/00017.png")
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
    color_raw, depth_raw)
print(rgbd_image)

"""
plt.subplot(1, 2, 1)
plt.title('Redwood grayscale image')
plt.imshow(rgbd_image.color)
plt.subplot(1, 2, 2)
plt.title('Redwood depth image')
plt.imshow(rgbd_image.depth)
plt.show()
"""

pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd_image,
    o3d.camera.PinholeCameraIntrinsic(
        o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
# Flip it, otherwise the pointcloud will be upside down
#pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
o3d.visualization.draw_geometries([pcd], zoom=0.5,
                                front=[-1, -1, -1],
                                lookat=[0, 0, 0],
                                up=[-0.0694, -1, 0.2024]
                                )