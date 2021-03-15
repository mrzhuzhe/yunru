# Lec15 feedback lyapunov through contact

last time 

minimal coordinates 

## trajectory optimization mode sequence

- mode 1 

x' = f(x, u, i)

contact constraint forces

- mode 2

x = f(x, u, i)

g2(x, u, i) = 0

d_foot(q, q') / d(t) = 0

g2(x, u, i) * d_foot^2(q, q', u, i) / d(t) = 0

soft contact i = -k_foot(q)

## maximal coordinates ( complementory )

x' = f(x, u, i)

Lyap(q) >= 0 x >= 0

Lyap(q) - i = 0 (either Lyap(q) = 0, or i = 0)

very prectical works well

soft contact 

i = [0, k]


## sum of square for lyapunov analysis though contact 

m(q)*q + C(q, q')*q' = T_g(q) + B * u + sum J^T(q) * i

s = sin(theta)

c = cos(theta)

s^2 + c^2 = 1

V(q, q') >= 0

V(q, q') > P, i >=0, Lyap(q) >= 0

转为拉格朗日灯饰 Lyap(q)*i=0, also polynomial

reffernce: <<stablity Analysis and control of rigid-body system with impacts and friction>>

stabilize a fixed pt though contact

ex: compass gait balancing

1. LQR works minimal coordinate 

2. minimal floating coordinate 

x' = f(x, u, i)

g(x, u, i) = 0 = foot()q

can solve for i => x' = f(x, u) = A * x + B * u 

L, P MPC will succeed from valid X (w/foot LQR(A, B, Q, R))

constraint LQR

x' = A*x + B*u

know additionally that G*x = 0

local stabilization across modes as a mixed-integer optimization 

min sum(x^T * Q * x) + u^T * R * u 

s.t x[n+1] = A * x + B * u, x[0] = x0, x[n] = x_goal

x[n+1] = Ai*x[n] + bi*u[n] + Ci

Di*x + Fi*u <= 0

min x[] u[] i[]

x[n+1] = A*x[n] + B*u[n] + Bi*x[n] + C, i >= 0, G[] >= 0 

Ii[n] <= biM, Gi * x[n] <= (1-bi)*M, bi in {0, 1}

A computational bottenneck

"mixed integer optimization"
 
