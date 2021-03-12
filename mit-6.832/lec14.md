# computational method for leg rotation

## review

1. rimless wheel
2. compass gait
3. slip
4. limit cycle
5. fixed points/local stability
6. local stabilization leg LQR
7. lyapunov analysis
8. trajectory optimization

## hybrid dynamics of contact 

目标：
1. 求最近稳定点
2. 求稳定状态之间最小转动
3. 求周期性稳定状态解

## smooth system 找不动点

x' = f(x), fixed pt is f(x^*)=0, find x s.t f(x^*) = 0， 求周期性解

- 例：von der pol 震荡

find x(t)' = f(x)  x(0) = x(t_f)


- 例: rw cycle w/dorcol 

m*l^2*theta - m*g*l*sin(theta) = 0

theta'^T = cos(2*alpha)*theta'

find s.t x' = f(x)

theta(0) = ro - alpha

theta(t_f) = ro + alpha

theta(0) = cos(2*alpha)*theta(t_f)'

- 目标：computer optimization of a minimal piped model discovers walking and running

## more general (autonomous hybrid system)

正 model1  待选函数大于0

x1' = f1(x1, u)

反 model2 待选函数小于0

x2' = f2(x2, u)

witness function 

- 步骤分解

1. 脚悬空
2. 脚跟着地
3. 脚旋转
4. 脚尖着地

## 如果我们预先确定一个动作步骤

x[0], ... x[k] , x[n+1] = f(x[n], u[n])

x[k+1], x[], x[n+1] = f2(x[n], u[n])

x[k+1] = delta(x[k])

总体来说 这里还是根据一阶导正 和二阶导负 确定稳定区域 和 limit cycle 来做同型动作

## 最小角度

m(q) * q'' + C(q, q') * q' = Tao(q') + B*u +sumJ^T(q)*F_i

contact jacobian , contact_forces

if phi(q) > 0 , f_i = 0

if phi(q) = 0, phi(q)' = 0, phi(q)'' = 0

Idea1: soft contact F_i = soft.spring.model(x) = -K*phi(x) - damping

可以看一下视频1分08秒的内容 

Idea2: time - stepping approach 

x[n+1] = f(x[n], u[n], i(n))

反向欧拉法 x[n+1] = x[n] + d(t) * f(x, u)

phi(q) >=0 , i[n] > 0

