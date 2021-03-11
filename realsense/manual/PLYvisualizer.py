# 自定义可视化 
# http://www.open3d.org/docs/release/tutorial/visualization/visualization.html
# 交互可视化

import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

# todo 处理前需要点云对齐

# 打印点云
print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("./zz_test_panda/scene/integrated.ply")
print(pcd)
print(np.asarray(pcd.points))

# 体素下采样
#   print("Downsample the point cloud with a voxel of 0.05")
#   downpcd = pcd.voxel_down_sample(voxel_size=0.05)

# 估计法向量
# downpcd.estimate_normals(
#    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

o3d.visualization.draw_geometries([pcd],
                                    front = [ 0.1832502989013659, 0.11843027671491421, -0.97590655162765916 ],
                                    lookat = [ -0.05104928070021364, -0.36317995086867577, 1.8474828417562952 ],
                                    up = [ -0.0063337270407514204, -0.99255409626423763, -0.12163983677585158 ],
                                    zoom = 0.50199999999999978)

#   打印法向量
# print("Print a normal vector of the 0th point")
# print(downpcd.normals[0])