#Basic Pick and Place Part 2

review: 
1. kinematic frames / spatial algebra
2. gripper frame plan "sketch"
3. forward kinematic iiwa + wsg

mainline
- diffiential kinematics
1. how do changes in q relate to change in X^G
2. spatial velocity
- from keyframes to trojectories

- rotation representations
1. 3 x 3 matrices composition is just matrix multiply
2. unit quaternains (4 num) ·重点查一下·
3. roll pitch yaw ( euler angles ) (3 num)
4. axis angle (3 num)

- time derivative of rotation 
1. angular velocity [ delta_x, delta_y, delta_z ]^T  magnitude 量纲
2. "gimbal lock" 三个参数不足以表示旋转， 但是足以表示旋转率
3. unit quaternains [ sin(delta) * x, sin(delta) * y, sin(delta) * z, cos(delta) ]

- angular velocity 
1. 这一段可以去threejs中测试一下，就用 exludeshape 测， 可以看看threejs中的实现
2. 对于 iiwa q 是 7 joint angles 
3. 对于 brick q 是 7 element pose 
