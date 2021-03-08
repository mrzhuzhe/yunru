# Running

## 奔跑系统和走路系统的差别

1. 存在空中阶段
2. 存在能量的交换 弹簧系统 惯性钟摆

## 为何要使用简单模型

1. 可追溯
2. 简单机械结构
3. 抽象胜负结构 数据不变性 基础原则
4. 高维dof的模版

弹簧惯性模型

假设
1. 无重力腿
2. 完美弹性碰撞
3. 能量总是被内部保持 倾向于稳定

## poincaremap 

apex2apex map 

x = [x, y, theta, x', y', theta']

y' = 0

y[n+1] = P(y[n])

空中阶段

X = [x, y]

X'' = [0, g]

地面阶段

x = [r, theta, r', theta']

最小角度

y(t_touchdown) = l*cos(theta_touchdown)

m*r'' - m*r*theta'^2 + m*g*cos(theta) - k*(r0-r) = 0

m*r^2*theta'' + 2*m*r*r'*theta' - m*g*sin(theta)*r = 0

harmut geyen gave us linearized about small angles 

take off to aerial x(0), y(0) to y(torque) = 0 + energy correction at apex

slip approximate apex to apex map 

## 设计 u[n] = pi(y[n]) 让y^d稳定

y[n+1] = P(y[n], u[n])

ides1: find u* st y^d = P(y^d, u^*) 在 (y^d, u^d) 附近线性化 并做离散LQR

## deadbeat control

if P is invertiable u[n] = P^-1(y^d, y[n]) 设置和地面接触的角度

## 例子

蟑螂开炮

轮式奔跑机器人

robert hooper

1. hooping height (push to toe off)
2. foot touchdown to regulate speed
3. stabilize attitude doing stance

