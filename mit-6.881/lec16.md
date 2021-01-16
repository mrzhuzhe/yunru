# Motion Planning 2

> slides: https://slides.com/russtedrake/fall20-lec16/

> trajectory: https://colab.research.google.com/github/RussTedrake/manipulation/blob/master/trajectories.ipynb


## IK 的 collab 演示
增加一个柱子 non-linear constraints
竖着的 横着的


## kinematic trajectory optimization

15:00 有个不错的图 演示了如何回避限制条件

Piecewise Polynomial or B-spline

## 增加参数并不会对复杂度产生指数级别的影响

## major limitation: local minima

Alrernative : Sample - based motion planning 

## Probabilistic RoadMap (PRM)

这里提供了好几篇论文 nancy amato

见ppt第三页

## 这里给了ik的几何流形表示但是我完全没看懂

## rapidly-exploring random trees （RRTs）

这里一个反向钻洞的例子我也想过

https://slides.com/russtedrake/fall20-lec16#/10

https://slides.com/russtedrake/fall20-lec16#/12

http://www.kuffner.org/james/plan

Voronoi-bias

explore space very quickly
go back and fill small region

## Open Motion Planning Library (OMPL)
google: drake + ompl 

## What is the sample space q ?

q = [qrobot, qobj]

in trajectory optimization

min |qrobot - qrobot_desired|^2
s.t: IK(q[i])
G^X^o = c i in [5, 15]


## sample-based 
vs trajectory optimization + only require boolen collision checking 
vs distances (SDF) + gradients + dont have to predetermine # of points on trajectory or the connectivity

ppt 第 4/5 页

## each IK problem is independent

Principle of robot motion: theory algorithems and implementation

sample-base with optimization 

```
+ probabilistic completeness
 if a trajectory exists, I will eventually find it

- dont know when infeasible + can combine heuristics , optimization for sampling ,etc to improve performace

- scaling
- need post-proccessing
+ multi-query
+ optimizing planners ( RRT / PRM )

```

## soft skin
ppt 16页 


## reducing reliance on collision-free planning with contact-awre control

## question:
initial tree