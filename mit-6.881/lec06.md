# geometric perception
- https://www.youtube.com/watch?v=YQYMKQUAEAw
- geometry sensor 
1. lidar / time of flights : 
velodyne spinning lidar 激光旋转雷达
hokuyo scanning lidar 北洋扫描激光雷达
luminar 500m  灯具

2. stereo   声纳
carnegie multisense stereo
point grey bumblebee

3. structured light
microsoft kinect
asus xtion
https://arxiv.org/abs/1505.05459

4. projected texture stereo
intel realsense d415
our pick for "manipulation station"
major advantage over e.g ToF: multiple cameras dont interfere with each other


- add stereo sensor to drake 
color image & depth image

- real point clouds are also messy
ICRA 2019 Chris sweeney et al

- Perceptron as a geometry / kinematics problem

Object O -> a set of points -> Object model o_P_m_i

for depth camera : depth image + camera intrinsics C_P_S_i

- goal of perception Estimata 
m_i = s_i

X_o(unknown) * o_p_m__i (known) = X_c * c_P_s__i (known)
