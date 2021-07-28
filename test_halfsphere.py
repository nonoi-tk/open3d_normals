import numpy as np
import open3d as o3d

#なす角cos = ベクトル内積 / ノルムの積
#arccos(cos) = radian
def vector_angle(u, v):
    return np.arccos(np.dot(u,v) / (np.linalg.norm(u)* np.linalg.norm(v)))

pcd = o3d.io.read_point_cloud("./halfsphere.ply")

KD = o3d.geometry.KDTreeSearchParamHybrid(radius = 40, max_nn = 30)
o3d.estimate_normals(pcd, search_param = KD)
o3d.geometry.orient_normals_to_align_with_direction(pcd)
normals_list = np.asarray(pcd.normals)[:, :]
normals_point = np.asarray(pcd.points)[:, :]
print(len(normals_list))
print((np.asarray(normals_list)[:, :]))
o3d.visualization.draw_geometries([pcd],"estimated normals")

_normals_point =[]

for i in range(len(normals_list)):
    uvZ = (0,0,1)#z-axis unit vector
    rad = vector_angle(normals_list[i], uvZ)
    deg = np.rad2deg(rad)
    print("rad:",rad, " deg",deg)
#    print(deg)
    if( abs(deg) == 90.0 ):
        _normals_point.append(normals_point[i,:])

pointcloud = o3d.PointCloud()
pointcloud.points = o3d.Vector3dVector((np.asarray(_normals_point)[:, :]))
o3d.visualization.draw_geometries([pointcloud],"anagle")
