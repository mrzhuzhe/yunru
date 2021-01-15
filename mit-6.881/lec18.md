# Reinforcement Learning 2

## slides 
https://slides.com/russtedrake/fall20-lec18

## Policy gradient approaches to RL

min L(theta) = E[g(theta)] ~ sum(g_i(theta))*1/N

黑盒法不用计算梯度

# 如果我们不想计算损失梯度

idea: finite differences 估计梯度 这里似乎用了局部估计梯度 近似微分的数值方法

讲了一下随机梯度下降 asynchronous update or "mini-batch"

在梯度预测中使用 sgd

# Embrace SGD in our policy gradient

这里讲了sgd的一些细节，简化计算 用分布来动态改变步长，最优步长等

actor-critic algorithms

A2C  A3C

In sequential optimization: 

advantage update

# 收敛率
signal to noise ratio 

signal: power of signal in direction of true gradient

noise power of orthogonal components

