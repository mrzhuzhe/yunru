# Dexterous Manipulation

> https://slides.com/russtedrake/fall20-lec21#/1

## 为啥要用RL
并不是因为 dont have good model/ too hard to simulate 

Planning / control though contact 

Recall : Motion planning as IK

For actual manipulation, so far "Multiple shootting"

predetermined "contact mode sequence"

now: need to solve for sequence + trojectory

option 1) optimize robot commands only run a simulation mabe take gradients 

option 2) add contact decision as decision variables

what do gradients look like though contact 

Imagine the box flipping problem

31分钟时有图解, 向墙扔球

我们需要计算接触时间 接触位置 和 感知接触事件的发生 感知事件的“梯度”

实际上 计算复杂的机械手 ：连续时间模型中 只计算刚体stiff spring模型 或者time step 模型

刚体弹簧模型 result in "stiff" ODEs  very expensive dangerously inaccurate sims

时间片模型 可以算梯度 but take some wark

all of complexity of collision geometry gradients 

难以模拟

# 我们如何解决 这种混合模型 复杂度的问题

 Foundamentel: we can change our objective 

 min_u sum_n g(x[n], u[n])

 min E(sum_n g(x[n], u[n]))

 our initial conditiond box side, inertias zebra texture maps

 使用大量的蒙特卡洛法

 RL is often searching for policy, not trajectorys

 there ia difference to optimizing closed-loop vs open loop trajecties

 Difference betwwen troj of full feedback parameterizations 

另一条路线：

告诉优化器 descant inertie 下降惯性

例如： 增加接触力度 as 决策变量 + complementarly constraints  force >=0, contact distance >=0 , force * distance = 0


- need more contact touch

For changes in parameters that do not make or beak new contact, gradients could be well behaved; but it comes down to numerics

## 问题环境

-  为啥说优化方法还很欠缺



