# Tactile Manipulation 软体触觉控制

> naveenoid.wordpress.com

> 只有视频 ppt都没 https://www.youtube.com/watch?v=8dObqk0jt0o

# 0. why

shadow robot hand company

robot touch something 9:11 有介绍一些设备 https://www.youtube.com/watch?v=8dObqk0jt0o&feature=youtu.be

occlusion 咬合控制

# 1. classfify tactile sensors

directions/ resolution/ Force/ Pressure Maps/ Dense Geometry

Visue-tactile / Dense Geometry sensors

Gripper proprioception/ slip sensing/ contact pressure sensing/ force sensing/ geometry sensing

# 2. camera based tactile sensors

# 3. object classification

通过触觉信息进行分类 演示在 41:43

# 4. in-hand pose estimation

open loop + undderactuated / compliant grippers are sometimes not enough to understand in hand pose

Depth Registration, dense geometry sensors 

1:03 秒有 深度感知的例子

问题： 过于局部，会被图像中没有但是有接触的部分迷惑，不能获取到约束调剂，过于依赖局部特征如几何情况/边缘等

论文：
1. Tactile Mapping and Localization from High-Resolution Tractile Imprints

2. Fast Model-based contact patch and pose estimation for highly deformable dense-geometry tactile sensors

# 5. shear/slip feedback control 


# 6. geometry driven tactile control 

Dense Articulated realtime tracking (DART) an optimization based approach for depth based pose estimation wrapped in an EKF-style tracker

comebine vision and touch


# 7. softness and tactileness

# 8. can we simulate tactile sensing

