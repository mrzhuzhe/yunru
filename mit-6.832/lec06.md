# Acrobots, Cart-poles, and Quadrotors II

## topic 

- stability analysis w / lyapunov functions + control design

- energy shaping

- portial feedback linearization

- throw-back to "hand-designed control"

Stability of the damped pendulum

m * l * theta - m * g * l * sin theta = -b * theta'


## lyapunov functions

x = f(x)

prove x = 0 is a stable fixed point 

produce V(x) V(x) > 0 V(0) = 0

Lyapnov function V(x)' = dV/dx V'(x) < 0 V(0)' = 0

radially inbounded V(x) -> inf as |x| -> inf 

t -> inf V -> 0 x -> 0

"global asymptotic stability"

 Global exponiential stablity

 V(x)' < - alpha V(x) alpha > 0

V(x(t)) <= V(x(0)) * e^-alpha*t

V(x(0)) = c  V(x(t)) <= C

|| x(0) - x^* || < ro => || x(t) - x^* || < e

local stability 
    only V < 0 in some e-ball B around X^*

Glow v < 0 everywhere

Reginal stability V' < 0 over an invariant set

## relationship to DP

0 = min [g(x, u) + dJ * (f(x, u)) / dx]

for u^* = PI^*(x)

dJ^*/dt = -g(x, u^*)  hard-solve PDE

dV/dt <= 0  can often guess a simple solve

Swing - up for pendulum

homochiiz or bit 

Goal swing up to upright, w/ small torques 

Idea Due to homoclinie orbit 

E = m * g * l 

Driven pendulum : m * l^2 * theta + m * g * l * sintheta = u 

E' = u * theta torque velocity

V(x) = 1/2 (E(x) - E^d)^2

V(x)' = E(E(x) - E^d) = u * theta' * E_hat

u = - k * theta * E_hat

V(x)' = -k * theta'^2 * E_hat^2

## cart - pole 

这一段有个问题，这个不是都是吧”稳态“，连立成微分方程的线性系统么， 这个有啥“欠定”？

can also control theta''

choose f = (c-2/c) * theta'' - 2 * tantheta - theta'^2 * s

