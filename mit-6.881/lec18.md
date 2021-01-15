# Reinforcement Learning 2

## slides 
https://slides.com/russtedrake/fall20-lec18

## Policy gradient approaches to RL

min L(theta) = E[g(theta)] ~ sum(g_i(theta))*1/N

黑盒法不用计算梯度

# 如果我们不想计算损失梯度

idea: finite differences 估计梯度 这里似乎用了局部估计梯度 近似微分的数值方法