# lyapunov Analysis I

- strong intertial coupling 强惯性耦合

- energy-shaping 能量整形

- Differential Flatness 微分平滑

> 一个不错的博客，讲里亚普诺夫，拉萨尔不变点原理 https://zhuanlan.zhihu.com/p/31925435

## rewiew

non collocated PFL for cart-pole system

applied nonlinear control 

目标：将非线性系统分解为多个线性系统，一般以起始点为起始 稳定点为目标，得出将状态由一个初始状态（可能是平衡点）转换到另一个平衡点的平滑一阶微分或二阶微分路径

RAW： PLFL of cart - pole 

x'' = x''^d  theta' = nonlinear collocated PFL

non-collorated PFL theta'' = theta''^d  x'' = nonlinear

m(q)*q + C(q,q') = T_q(q) + B * u

B in R[m, n] n -> number of dof m -> num of actuators

q = [q1, q2]  = [passive, actuator]

m(q) = [[m11, m12], [m21, m22]] 

m11 * q1'' + m12 * q2'' = T1

m21 * q1'' + m22 * q2'' = T2 + u

q2'' = m12^# (T1 - m11*q1')

## one - leg hopper

Task - space "output"

z = h(q) = - L * cos(theta)

H = d(h) / d(q)  H^hat = H2 - H1 * M11^-1 * M12

inertial coupling rank(H^hat) = n - m

## Energy shapping for the cart - pole

idea: regulate pole to it's homecline(均线) orbit useing collocated PFL

x'' = u   theta'' = -u*c - s  

E = 1/2 * theta'^2 - cose(theta)  E = 1 

V(x) = 1/2(E - E_desire)^2 = 1/2(theta' * theta'' + theta'*s)^2 = theta' * (-u*c-s) + theta' * s = -theta' * u * cos(theta)

因此 : choose u = k cose(theta) * theta' * E^hat

V' = - k * theta'^2 * cose(theta)^2*E_hat^2

这一段的意思是不是用线性拟合非线性时做功的多少可以用轨迹所需能量平均值来近似

> ps: 看到这里时看 rl 找到了 agent-ml 这个库

## differenial flatness

m * x'' = -(u1+u2) * sin(theta)

m' * y'' = (u1+u2) * cos(theta) - m * g

I * theta = r * (u1 - u2)

z = h(q)  z = [x, y]

x in [l0, l1]

z = (x(t), u(t))

-m*x'' / (m*y'' + m*g) = (u1 + u2)*sin(theta) / (u1+u2) * cos(theta) - tan(theta)

theta = tan^-1 (-x''/g)

3d version z = [x, y, z, theta_yaw]

## 目标 minimize shap trajectory generation and control for quadrotars 

position -> velocity -> acceleration -> jerk -> snap -> crackle -> pop

