# Reinforcement Learning 2

> slides https://slides.com/russtedrake/fall20-lec18

>https://openai.com/blog/openai-baselines-ppo/

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

信号 真实梯度的信号

噪声 正交项

counting game

# Rl中更新梯度的几种进阶方式 TRPO policy gradient 法

Deep nets have a lot of parameters of the net instead , and use backprop to change theta  , evaluate policy many times for each L(theta)

dim(w) = #timesteps x #policy outputs

"episodic reinforce" in reinforce algorithm William 92

Important idea from optimization: Trust Region （TRPO)

Trust Region Policy Search (TRPS) 2012 American Control Conference (ACC) / ICML2015 

用confience 更新 hessien 矩阵

openai baseline "ppo" "dpg"

# 1.20:00 这里应该是讲得概率采样法的实现细节

还是使用对数函数对模型建模，再继续使用之前的sequential 优化算法，这里都是手写公示，不过内容和机器学习的内容比较重合

# 问答
- 增加扰动提升健壮性 和 dpg paper 要输出policy尽可能确定的矛盾

- 现在已经不用延迟reward了

- openai paper  KL散度 和 概率 居多 忽视了直觉理解