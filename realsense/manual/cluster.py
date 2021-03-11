# 聚类
# 需要移除远处点

import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

sourcePath="./zz_test_panda/scene/integrated.ply"
tatgetPath="./zz_test_panda/scene/cropped_1.ply"

# 加载点云
print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud(sourcePath)

with o3d.utility.VerbosityContextManager(
        o3d.utility.VerbosityLevel.Debug) as cm:
    labels = np.array(
        pcd.cluster_dbscan(eps=0.02, min_points=10, print_progress=True))

max_label = labels.max()
print(f"point cloud has {max_label + 1} clusters")
colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
colors[labels < 0] = 0
pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
o3d.visualization.draw_geometries([pcd],
            front= [ -0.12109781037531148, -0.067873032753074228, -0.99031740959512848 ],
			lookat= [ 0.3134765625, 0.044091457811535228, 0.34410855566261028 ],
			up= [ 0.022294674751066466, -0.99759391284426524, 0.065645506577472368 ],
			zoom= 0.70799999999999996)