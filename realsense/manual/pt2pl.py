import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

sourcePath="./zz_test_panda/scene/integrated.ply"
tatgetPath="./zz_test_panda/scene/cropped_1.ply"
singleframePath="./zz_test_panda/scene/singleframe.ply"

# 加载点云
print("Load a ply point cloud, print it, and render it")
#pcd = o3d.io.read_point_cloud(sourcePath)
#pcd = o3d.io.read_point_cloud(tatgetPath)
pcd = o3d.io.read_point_cloud(singleframePath)

# 分割
plane_model, inliers = pcd.segment_plane(distance_threshold=0.01,
                                         ransac_n=3,
                                         num_iterations=1000)
[a, b, c, d] = plane_model
print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")

inlier_cloud = pcd.select_by_index(inliers)
inlier_cloud.paint_uniform_color([1.0, 0, 0])
outlier_cloud = pcd.select_by_index(inliers, invert=True)


o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud],
            front= [ -0.12109781037531148, -0.067873032753074228, -0.99031740959512848 ],
			lookat= [ 0.3134765625, 0.044091457811535228, 0.34410855566261028 ],
			up= [ 0.022294674751066466, -0.99759391284426524, 0.065645506577472368 ],
			zoom= 0.70799999999999996)