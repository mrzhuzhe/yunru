import open3d as o3d
import numpy as np

import os
import urllib.request
import tarfile
import gzip
import shutil

# mesh = o3dtut.get_armadillo_mesh()
def _relative_path(path):
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    return os.path.join(script_dir, path)

#   armadillo_path = _relative_path("../test_data/Armadillo.ply")
armadillo_path = _relative_path("../test_data/bathtub_0154.ply")
if not os.path.exists(armadillo_path):
    print("downloading armadillo mesh")
    url = "http://graphics.stanford.edu/pub/3Dscanrep/armadillo/Armadillo.ply.gz"
    urllib.request.urlretrieve(url, armadillo_path + ".gz")
    print("extract armadillo mesh")
    with gzip.open(armadillo_path + ".gz", "rb") as fin:
        with open(armadillo_path, "wb") as fout:
            shutil.copyfileobj(fin, fout)
    os.remove(armadillo_path + ".gz")
mesh = o3d.io.read_triangle_mesh(armadillo_path)
mesh.compute_vertex_normals()
    
vertices = np.asarray(mesh.vertices)
static_ids = [idx for idx in np.where(vertices[:, 1] < -30)[0]]
static_pos = []
for id in static_ids:
    static_pos.append(vertices[id])
handle_ids = [2490]
handle_pos = [vertices[2490] + np.array((-40, -40, -40))]
constraint_ids = o3d.utility.IntVector(static_ids + handle_ids)
constraint_pos = o3d.utility.Vector3dVector(static_pos + handle_pos)

with o3d.utility.VerbosityContextManager(
        o3d.utility.VerbosityLevel.Debug) as cm:
    mesh_prime = mesh.deform_as_rigid_as_possible(constraint_ids,
                                                  constraint_pos,
                                                  max_iter=50)

print('Original Mesh')
R = mesh.get_rotation_matrix_from_xyz((0, np.pi, 0))
o3d.visualization.draw_geometries([mesh.rotate(R, center=mesh.get_center())])
print('Deformed Mesh')
mesh_prime.compute_vertex_normals()
o3d.visualization.draw_geometries(
    [mesh_prime.rotate(R, center=mesh_prime.get_center())])
