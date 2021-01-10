# Category-level Manipulation

3d创建：https://slides.com/russtedrake/fall20-lec14#/10
3d创建和分割：https://slides.com/russtedrake/fall20-lec14#/18
迁移学习：https://slides.com/russtedrake/fall20-lec14#/33


这一课只有ppt，没有文档
ppt里有一大堆论文可看
xcon
gym for drake? 

- state presentation

sensors -> perceptron -> uav in forest : pos vel oir speed where are the trees -> planning / control -> actuator com

系鞋带，切洋葱，涂奶油

- 具体方法
sensors -> NN -> Plan

NN:

image -> perceptron NN -> NN -> plan

- how dowe even specify the task ?
 what the cost function ?

 pose ( canonical ) : point clouds
 masks ( segmentation ) : bounding boxes (axis -aligned / oriented )
 shape <- shape completion

scence graph ( computer graphics )

- “Normalized Object Coordinate Space for Category-Level 6D Object Pose and Size Estimation,” in 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)

https://slides.com/russtedrake/fall20-lec14#/10

keypointnet.github.io
- keypoint network
convolutional pose machine (PRN)

Image -> NN -> 1 heatmap per keypoint

ground truth can be for any visible keypoints or occluded keypoints

3D keypoints provide rich, class-general semantics (open pose isrr 2019)

keypoint "semantics" + dense 3d geometry

两种方式 1. 对实例采用对立方式  2. 对模型建立度量自动产生方案

- 试验： 把鞋子挂架子上
训练集 测试集 trails 准确率

shape completion network（kPAM-SC）to include collision-avoidance constraints

- 演示
3D reconstruction: single view reconstruction learning achitecture pointSDF 
graps Metric: incorporate PointSDF for geometry-aware learned grasp success probability
grasp synthesis: formulate grasp synthesis as constrained optimization where we constrain to avoid collision

- force control 
peg in hole 乐高 usb 

- 在目前情况中关键节点（mug handle，front toe of shoe ）是几何化和语义化的，需要人工标注

如果我们放弃语义，关键节点是否可以自监督产生

KETO learning keypoint representations for tool manipulation 

- dense object nets
dense 3d reconstruction + pixelwise contrastive loss

- Dense Object Nets in visuomotor Imitation Learning 


- standard "behavior-cloning" Objective + data augmentation

policy is a small LSTM LSTM network

https://sites.google.com/view/visuomotor-correspondence

中途打断扰乱的处理 可见slide 33-36

这个感觉可以用openai的gym来处理

- 更加的推广化

dense object nets for model-predictve control (MPC)

learn descriptor keypoint dynamics + trajectory MPC

Question: 
