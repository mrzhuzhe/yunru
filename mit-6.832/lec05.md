# Acrobots, Cart-poles, and Quadrotors I

> http://underactuated.csail.mit.edu/acrobot.html

Mnipulator Eqs Feedback linearization Optimal control Value iteration

# Model underractuated systems: 

cart-pole System / acrobot / pendubot / furuta pendulum / reaction - wheel pendulum / ball - and - bean 

Planner VTOL (quadratic)

havercrafl

Bicycle models

acrobot with no motor in shoulder

Eqs for motion for both 

- Acrobot

m(q) * q'' + C(q,q') * q' = T(g) + B * u 

q = [theta1, theta2] 

u = T_elbow, |u| < u_max

B = [0, 1]

- cart - pole

q = [xcart, theta_pole] 

u = f_cart

B = [1, 0]

|u| < u_max |x_cart| <= x_max

# Linear Quadratic Regulator 

x = A * x + B * u

J = F(x^T * Q * x) + U^T * R * u

J = x^T * S * x, u = -k * x 

x' = f(x, u)

local linear approximation around (x0, u0)

泰勒展开

x' = f(x0, u0) + df/dx (x - x0) + df/du (x - u0)

x' - x0' = A(x - x0) + b(u - u0)

change coordinates 坐标转换

x' = x - x0

u' = u - u0

u = m * l^2 * theta + b * theta' + m * g * l *sin(theta)

Linearize around theta = PI, theta' = 0, u = 0

x' = [theta', 1/m*l * (T - b * theta - m * g * l *sin(theta))]

28:00 有向量化的完整公式 和 函数图形

对图像做特征分析： 这个图像似乎是个负定图像 是 “反闭包” 

[K, S] = LQR(A, B, Q, R)

x' = (A - B * k) * x is stable

can be very hard to tune K directly

A - B * k = [[-1, k2], [k1, -1]]

for any

Q = Q^T >= 0

R = R^T > 0

will return a stablizing k

可控制系统（可取得动量平衡的系统） 和 欠定系统

linearizing the manipulator eqs

为何我们可以线性控制非线性系统