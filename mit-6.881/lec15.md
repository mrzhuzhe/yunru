Motion Planning 1

ppt：https://slides.com/russtedrake/fall20-lec15#/10
运动规划（完成度很低）：http://manipulation.csail.mit.edu/trajectories.htmlß

- motivation
bump into
avoid collision

- kinematic Trajectory
inverse kinematics (IK)
X^G = f_kin(q)
"differential kinematics"  J = phi f / phi q
IK: f_kin^-1 : X^G -> q
kinematics are polynomial 
sin(theta) cos(theta)

- 2D rigid body
x y theta 3 variables for 2d pose

|p1-p2|^2 = const
17:38 3轴2d机器人

special case: 6 DOF robot, desired spatial pose ( 6 constraints )

IKfost: closed form "numerical" solutions

Inverse kinematics as constrained optimization

closed form: only equality constraints

inequality constraints: qmin <= q <-qmax

collision avoidance sdf(q) >= 0.01

nonlinear inequality constaints => nolinear optimization

minimal cost function, eq, joint centering

min|q - q0|^2

- four-bar linkage
用到了同形 Numberical algebraic geometry and algebraic kinematics

- inverse kinematics as an optimization 

min|q - q_desired|
subject to 
1. rich end-effector constraints
2. joint limits
3. collision avoidance 
4. gaze constraints 
5. feet stay put 
6. balance (center of mass)

- drake 中对限制条件做了封装实现，包括上面这些限制

- nonlinear solver of gradient descent
SNOPT: nonlinear optimization solver
sequential quadratics optimization

1. SNOPT: https://web.stanford.edu/group/SOL/snopt.htm

2. Alternative to SQP
Augumented lagrangian is an approach for adding constraints to objective

3. reinforce learning

- graps planning as IK

Mug reorientation problem : Two IK problems 
min (q[0] - qnom)^2
st: mug in graps antipodal

min (q(t_f) - qnom) ^ 2
st: mug goal position is grasp

what connects the two optimizations?
g^X^o = f(q, x^o) 
f(q[0], x^o[0]) = f(q[t_f], x^o[t_f])

must solve jointly:
min |q[0]-qnom |^2 + |q[t_f] - qnom |^2
st: f(q[0], x^o[0]) = f(q[t_f], x^o[t_f])

- how to write constraints 
check yourself：
把圆棒子捡起来

有哪些限制

Kinematic trojectory optimization：
parameterize q(t) e.g a spline

Add IK constranist at sample points:
t0 t1 t2 ... tn

two common choices for q(t)
Piecewise Polynomials : q(t) = sum alphai(t -t_k)^i

often cubiz polynomial

Piecewise Polynomials:
B-splines: 

position / velocity / torque / mass  / dynamics limit constraints

- key-points only needs for perception systems

- question
1. dynamic or torque optimizaion faster in practice：
增加动量和阻尼限制对最优化器运行时间影响并不大

2. 如果违反了torque或者加速度限制会怎么办

3. 解的存在与否