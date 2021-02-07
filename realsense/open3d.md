# open3d

> 主要是英特尔官方自带的


> http://www.open3d.org/docs/release/getting_started.html


- 其实我也下载了labelfusion 和 eslaticfusion

- 还看了opencv的3d库

- 但是看起来这个库似乎更新更官方

## 问题记录
- 装依赖
1. pyrealsense2 似乎不支持，一直报错，但是似乎其实并不需要这么底层的api

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

## 目标
1. 物体匹配
2. 点云合并