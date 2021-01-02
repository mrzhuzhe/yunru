# Bin packing 2
Grasp pose detection in point clouds

Dex-Net 2.0: deep learning to plan robust grasps with synthetic point clouds and analytic grasp metrics

Robotic Pick and Place of Novel Objects in Clutter with Multi-Affordance Grasping and Cross-Domain Image Matching

Grasp Pose Detection in Dense Clutter

- Point cloud proccessing：
1. crop ( axis aligned bounding boxes ) AABB
2. normal estimation ( before merging )
3. merge point clouds ( w / concatenating pts )
4. Down sample "voxelization!"

- Normal estimation: 
fit a plane to a brunch of data 

d = ( P_i - P ) ^ T * n
min sum | d( P_i - P ) ^ T * n' | s.t: |n| = 1

L = sum | ( P_i - P ) ^ T * n | + ...
only depend on n

theta l / theta p = 0 
p = 1 / N sum P_i

sum ( p_i - p') ^ T * n * n ^ T * ( p_i - p') 

min n^T * W * n  s.t : |n| = 1

根据局部相邻元素计算法向量

- scoring a grasp candidate, X_g ?
collision checking ( cost infi if in collision ) 

Robot model: collisions between hand and bins

Point cloud: collision between hand and point cloud

- 55:00 59:00 有一段计算夹取物品接触面的演示
其中包含碰撞的情况，接触面的大小
有一段演示表示抓取分数的曲线寻找曲线优劣的变化

- limitation of using geomerty only
1. 不考虑物理效果
2. 可变形物体
3. deeplearning