# 用特征值得到关键点
import open3d as o3d
import numpy as np
import os
import time

# mesh = o3dtut.get_armadillo_mesh()
def _relative_path(path):
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    return os.path.join(script_dir, path)

armadillo_path = _relative_path("../test_data/Armadillo.ply")
mesh = o3d.io.read_triangle_mesh(armadillo_path)
mesh.compute_vertex_normals()

pcd = o3d.geometry.PointCloud()
pcd.points = mesh.vertices

tic = time.time()
keypoints = o3d.geometry.keypoint.compute_iss_keypoints(pcd)
toc = 1000 * (time.time() - tic)
print("ISS Computation took {:.0f} [ms]".format(toc))

mesh.compute_vertex_normals()
mesh.paint_uniform_color([0.5, 0.5, 0.5])
keypoints.paint_uniform_color([1.0, 0.75, 0.0])
o3d.visualization.draw_geometries([keypoints, mesh])