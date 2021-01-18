# Parameter Estimate and adaptive control

> 这部分似乎是在rew project 

> ppt: https://slides.com/russtedrake/fall20-lec19


# 投掷机器人

不需要抓取物体的中心，但是考虑重力加速度，且向物体施加横向速度

ACC 1991 视觉控制 抓球机器人

简单双摆：https://underactuated-r1.csail.mit.edu/multibody.html#manipulator_equation_double_pendulum

弹道：Trajectory depends on initial velocity of center of mass 

need com relative to the hand

# multibody parameter estimation

key idea: Inverse dynamics are linear in the (lumped
) parameters

Ex: simple pendulum

m * l^2 * theta'' + b * theta' + m * g * l * sintheta = Tao

[theta'', theta' sin(theta)] * p = tao

p = [m*l^2, b, m * g * l]^T

Observation Matrix
W = [[theta(t1)'', theta(t1)' , sin(theta(t1))],..., [theta(tn)'', theta(tn)' , sin(theta(tn))]]

can solve for lumped parameters using least-square

W * p = c

m * x'' = 0

m * x'' = 0

Identification requires
"sufficiently" rich trajectorics"

what w to be ideally full column rank

"identifiable" lumped parameters from SVD on the data matrix

Multibody case:

M(q) * v' + C(q, v) * v = Tao_q(q) + u + damping ...

完整公示见此处：https://slides.com/russtedrake/fall20-lec19#/7

v' = m^-1(q) * [u + Tap_q(q) - C]


