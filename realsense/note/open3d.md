# open3d

> 主要是英特尔官方自带的


> http://www.open3d.org/docs/release/getting_started.html


- 其实我也下载了labelfusion 和 eslaticfusion

- 还看了opencv的3d库

- 但是看起来这个库似乎更新更官方

## 问题记录
- 装依赖
1. pyrealsense2 似乎不支持，一直报错，但是似乎其实并不需要这么底层的api
2. 运行时似乎还是在走gpu，看是否能切换到cpu

- 图片的两种格式
1. rgbd图片格式 似乎分为两种 普通图片 和 tensor 图片
2. tensor 图片会在转化为点云时报一个 INTEL MKL 的错

- 可视化
1. 图片visualizer 中的角度不对
2. 广义变化  旋转矩阵 transform

- 数据结构
1. 点云可以转为kd树的结构存储
2. 点云 mesh 体素
3. 重建表面的算法大多需要法向量
4. xyz可直接转点云，点云可以用 asarray 转 np数组

- icp
1. 强健icp抑制离群点
2. 多路合并重点看一下，这个真的不需要对齐么？ 为什么不需要对齐？ 
官方提到的reconstruct例子里做了batch 重点看看
inv -> pinv

3. 在 rgbd合并中为何要保存轨迹？轨迹从哪来？相机固有属性instrict.json么？
4. 拼合icp时可以可视化拼合过程

- reconstruction
1. 批处理和子进程是解决了
2. 
python run_system.py config/realsense.json --make --debug_mode 
python run_system.py config/realsense.json --register --debug_mode 
python run_system.py config/realsense.json --refine --debug_mode 
python run_system.py config/realsense.json --integrate --debug_mode 
这个命令还是不能正确执行
3. opencv 没有试

- tensor
1. cuda 设置？？？？？

## 目标
1. 物体匹配
2. 点云合并
3. 实时