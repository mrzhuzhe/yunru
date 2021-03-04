# lyapunov 2 compute lyapunov functions 

> http://underactuated.csail.mit.edu/lyapunov.html

## swimup and balance control

稳定点附近讲非线性转化为线性, 是求优化问题前将问题转化为(线性规划的)凸问题的前置步骤

## optimization crash course 

min f(x) s.t g_i(x) <= 0

convex optimization  f(x) is convex  x in g(x) forms a convex set 

例如: min[g(x, u), ...]  convex quadratic cost    c^T * x s.t: |x|<=1

目标： search lyapunov function in convex set 

## conputing lyapunov function w/ linear programming 

idea：parameterize lyapunov candidate x' = f(x)

V(x) = sum[a_i * nonlinear_Basis_function_i(x)]= a^T * nonlinear_Basis_function_i(x)

V'(x) = a^T * d(nonlinear_Basis_function_i(x)) / d(x)

李亚普诺夫的优化形式 

find a （目标只是发现a不用优化什么）

s.t 

V(0) = 0,  x neq= 0 V(x) >= 0

V'(0) = 0, x neq= 0 V(x) < 0 

sample many pts, x_i 

linear constraints: 因为李亚普诺夫决策函数为线性，所以一定为线性规划

V(x) = a^T * VF(x) > 0

V'(x) = a^T * d(VF(x)) / d(x) > 0

注意： 这里 VF 指 lyapunov 待选函数

例：

f(x) is pendulum 

m * l^2 * theta'' + b * theta' + m * g *l * sin(theta) = 0

待选函数：VF = [1, cos(theta), sin(theta), theta', cos(theta), sin(theta)*cos(theta), theta*sin(theta), theta'*cos(theta), theta'^2]

V(x) = a^T * VF(x)

x_i neq 0 

V(x_i) >= e * x_i^2,  V(0) = 0

V(x_i)' <= -e * x_i^2 * sin^2(theta), V'(0) = 0 

> 这里没明白为啥要做pairwise的对比呢，这里做了drake 求解器的演示，这里明显在最开始构建差值等式时有筛选出线性差值的筛选过程

## 是不是所有 x 都有最优解

idea: V(x) = sum[a_i * VF^2(x)] V_i >= 0 positive by constraction

important generalization: V(x) = [VF1(x), ... VF_k(x)] * [[a11, a12, ....], [a12, ...], ...] * [VF1(x), ... VF_k(x)]^T

Q = Q ^T > 0 (PSD, 正定) x^T * Q * x >= 0 , VF^T(x) * Q * VF(x) >= 0

## 李亚普诺夫SDP

x' = A * x 是稳定点么

V(x) = x^T * P * x

F(x^T * theta * x)dt = Inge(e^(A*t))'*Q*e^(A*t)*x(0) dt

V'(x) = x^T * A^T * P * x^T * P * A * x = x^T * (A^T*P + P*A)*x

find P : st: P > 0, A^T*P + P * A < 0

# common lyapunov functions for Robust stability

x' = A * x elements of A are bounded but unvertain

A = Sum [Beta_i * A_i], 0 <= Beta_i <= 1, Sum(Beta_i) = 1

find p: P > 0, i in P*A_i + A_i^T*P < 0  => P(Sum(Beta_i * A_i)) + Sum(Beta_i * A_i^T * P < 0

## pydrake sum of square 演示





