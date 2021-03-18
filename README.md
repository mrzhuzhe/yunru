# Yunru

> Perceptions, Comprehension and Control

Note for MIT 6.881 & 6.832 & Realsense & RL & nonlinear control 

##  笔记

    1. /mit-6.881 制造业机器人的笔记 http://manipulation.csail.mit.edu/Fall2020/index.html 
    2. /mit-6.832 非确定情况机器人的笔记 
    http://manipulation.csail.mit.edu/Fall2020/index.html

## vision

- opencv

        1. /opemcv/contour.py 把照片上等高线用 rectangle 框出来

- realsense

1. 总入口 /realsense/run_system.py 

        运行分为四个步骤 debug_mode为中途可视化[详细说明](!/realsense/note/open3d.md)

        第一步，临近帧拼合：pythonw run_system.py config/realsense.json --make --debug_mode --reset_files

        第二步，相邻姿态估算角度：pythonw run_system.py config/realsense.json --register --debug_mode 

        第三步，用彩色帧优化拼合：pythonw run_system.py config/realsense.json --refine --debug_mode 

        第四步，转化为网格：pythonw run_system.py config/realsense.json --integrate --debug_mode 

2. mamual 常用功能

        /realsense/manual

        1)  camera 打开摄像头录制  

        2)  readbag 预览录制好的内容

        3)  readframe 读取单独一帧

        4)   PLYvisualizer 可视化点云

        5)  crop 裁剪点云

        6)  pt2pl 平面分割

        7)  cluseter 聚类

## Nonliner Control

[数学基础整体路径](./roadmap/README.md)

## resources
discuss:
1. https://www.yuque.com/ubvfdh/qw4twg/eggzw2

refference:
1. https://www.yuque.com/ubvfdh/fzgpdd/mn7pzb
2. https://www.yuque.com/ubvfdh/ybnhg1/qylx6u
