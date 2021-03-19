# feedback motion planning

> http://underactuated.csail.mit.edu/feedback_motion_planning.html

博客上线后有一些问题

上网搜了工业控制系统 scada dcs plcs 控制变量 目标端点 等概念，也找到了一些课程

## rew 
 - plan away timestep 
 - roadmaps
 - RRT

 << sequential composition of dynamically dexierous robot behaviors >>

## 最简单的抛球模型，用一个垂直平板控制左右角度来抛球

假设:
- instantanous 
- 软碰撞
- 模仿洗漱

x = [b, r, b'], u = [r']

输入 r(t) = -k * b(t)

## LQR 树

回头查一下模型预测控制 和 LQR树

## probabilistic feedback coverage

1. 随着轨迹的里亚普诺夫函数

x_hat'(x) = A(t) * x_hat(t) + B*u_hat(t) => u_hat(t) = -k * i_hat(t)

J(x, t) = x_hat^T * S(t) * x_hat

2. 轨迹定义在 x_n(t) 有限离散步骤 t in { 0, t_f}

J(x) < p'(t)  J(x, t_f) <= p(t_f)

3. 稳定，有限时不变，这里还需要补充查一下

J(x, t) <= p(t) 稳定性

J(x, t) = p(t) 有限时不变

opt(t) <= J(x, t) <= p(t)

