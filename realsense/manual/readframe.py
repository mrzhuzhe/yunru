# 用来读取单独一帧来调试

import open3d as o3d
import matplotlib.pyplot as plt
import numpy as np
import copy

mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
mesh_tx = copy.deepcopy(mesh).translate((1.3, 0, 0))
mesh_ty = copy.deepcopy(mesh).translate((0, 1.3, 0))
print(f'Center of mesh: {mesh.get_center()}')
print(f'Center of mesh tx: {mesh_tx.get_center()}')
print(f'Center of mesh ty: {mesh_ty.get_center()}')


print("Read Redwood dataset")
color_raw = o3d.io.read_image("./zz_test_panda/color/00017.jpg")
depth_raw = o3d.io.read_image("./zz_test_panda/depth/00017.png")
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


# 点云太多了 需要下采样
#print("Downsample the point cloud with a voxel of 0.05")
downpcd = pcd.voxel_down_sample(voxel_size=0.01)

# 估计法向量
#downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

"""
o3d.visualization.draw_geometries([downpcd], zoom=0.5,
                                front=[-1, -1, -1],
                                lookat=[0, 0, 0],
                                up=[-0.0694, -1, 0.2024],
                                point_show_normal=True
                                )
"""

radii = [0.005, 0.01, 0.02, 0.04]
#rec_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(downpcd, o3d.utility.DoubleVector(radii))
o3d.visualization.draw_geometries([ 
    #downpcd,
    pcd
    #rec_mesh, 
    #mesh, mesh_tx, mesh_ty
    ],
    front = [ 0.16656991818720754, 0.19508326294033895, -0.96653866082824524 ],
    lookat = [ -0.05104928070021364, -0.36317995086867577, 1.8474828417562952 ],
    up = [ -0.026059428944545732, -0.97901950138666249, -0.20209334988488648 ],
    zoom = 0.64799999999999991
    )
o3d.io.write_point_cloud("./zz_test_panda/scene/singleframe.ply", pcd)