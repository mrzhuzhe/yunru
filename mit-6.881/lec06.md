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

P_o + R_o * o_P_m_i = X_c * c_P_s_i 

inverse kinematics problem, differential

min sum | P_o + R_o * o_P_m_i - w_P_s_i | ^ 2 

st： R^T = R^-1, det(R) = 1

derivative via lagrange multiplies

in practice: solution for SVD

- Q: how many points do you need to give a unique solution in 2d ?

- Q: what happens if rotational sysmmetry


summmary : 
Given : model pts + scane pts +  camera frame + big assumption ( m_i = s_i ) = can solve scan pts 和 camera frame 和 实际模型mse
差的最小二乘问题 with svd

如果初始化猜想时只有“closest points” just need to improve my estimate 

Interactive Closest Point Algorithem （ICP）

- question 
outliner point 2 point  




