# Basic Pick and Place Part 1

mainline

- representation: 
对应 mls94 第二章

注意一个问题：镜头frame到实际frame的转换
补充：四元数可视化 https://eater.net/quaternions
https://drake.mit.edu/
binder notebook

1. rotation matrix, quatern, axis angle. roll pitch (aka euler angler)
2. pose: position & oritation of a frame  
3. rotation multipy, frame adding
4. Basic pick and place notebook plan sketch

- question:
1. how I generate plan sketch
2. how will it work if move "initial" and "goal" around sink
3. display new frame 

- forward kinematic
对应 mls94 第三章#page104
1. joint position -> pose
2. inverse kinematic : end-effector pose -> joint angle
3. differential kinamatic d(frame) / d(q)
4. add constrain between two body
5. revolute joint 旋转接头
6. kinematic tree parent child

