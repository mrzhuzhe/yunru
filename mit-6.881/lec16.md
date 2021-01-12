# Motion Planning 2

- IK 的 collab 演示
增加一个柱子 non-linear constraints
竖着的 横着的


- kinematic trajectory optimization

15:00 有个不错的图 演示了如何回避限制条件

Piecewise Polynomial or B-spline

- 增加参数并不会对复杂度产生指数级别的影响

- major limitation: local minima

Alrernative : Sample - based motion planning 

- Probabilistic RoadMap (PRM)

这里提供了好几篇论文 nancy amato

- 这里给了ik的几何流形表示但是我完全没看懂

- rapidly-exploring random trees （RRTs）

这里一个反向钻洞的例子我也想过

http://www.kuffner.org/james/plan

Voronoi-bias

explore space very quickly
go back and fill small region

- Open Motion Planning Library (OMPL)
google: drake + ompl 

- What is the sample space q ?
