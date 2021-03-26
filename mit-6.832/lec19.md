# 基于统计的模型

## rew 

本周试了一下树莓派的gpio

## 基本概念

x' = f(x, u),  x[n+1] = f(x[n], u[n])

x = f(x, u, w),  x[n+1] = f(x[n], u[n], w[n])

w[n] an output of some random process 

- 分布 
- 模拟不确定性

加性噪声  x[n+1] = f(x[n], u[n]) + B * w[n]

## 例如： 布朗运动

悬垂一样的分布

u(x) = 1/2 * alpha * x^2

x[n+1] - x[n] = - d(u) / d(x) + w[n]

w = 0

fixed pt x^* = 0

## 高斯噪声

Px[n](w) = 1 / sqrt(2*Pi*ro) * e ^(-w^2/2*ro^2)

这里有一张高斯噪声分布的图

## "escape attempts"

这里画了加了噪声的 `von del pol 分布`

`无环轮的图`

其实应该是想表达，摄动噪声对于里亚普诺夫分析的关系


## 最坏情况赊借和分析

有准确边时有效

有限作用域 

公用李雅普诺夫函数

统计控制 

期望值预警控制

J = Sum(g(x,u))

这里有张图表示`统计分布和期望的对比`

## 统计LQR

x[n+1] = A * x[n] + B * u[n] + Gaussian

min E[sum(x^T*Q*x) + u^T*R*u],  u = -k * x

## UAV 

LPF -> UAV <--> control 

统计 LQR “whetering fitter” 

reffer: <guranteed margins for LQG regulators>


