# motivate

## why study dynamics

1. non-linear dynamics
2. optimization and planning
3. linear algebra ODEs 

Underactuated:

Nonlinear Differential eqs:

x' = f(x, u)

Mechanical systems:

second-order F = m * a

q Position vector
q' velocity vector

q'' = f(q, q', u) = f1(q, q') + f2(q, q') * u

control affine


## a system is fully actuated in state (q, q') if f2(q, q') is full row rank

dim(q) = n

dim(u) = m

f2(q, q') in R^'(m*n)

欠定系统 ：
rank[f2(q, q')] <= n

x' = A * x + B * u
q' = f1(q, q') + f2(q, q') * u

Feedback linearization

q''_d desired accelerations

u = f2^-1(q, q') * ( q''_d - f1(q, q'))

q'' = q''_d

other causes of underactuated 
- input saturation
- state constraints (joint limit)
- model uncertainty / state estimation


Eqs of motion 

有个图展示摆臂

q = [theta1, theta2]^T

P1 = [l1 * sin(theta1), -l1 * cos(theta1)] = [L1 * s1, -l1 * c1]

P2 = P1 + [l2*sin(theta1 + theta2), -l2*cos(theta1+ theta2)]

P1 + l2[si+2, -ci+2]

P1' = l1 * theta1 * [c1, s1]

Kinetic energy:  T = 1/2 * m1 * P1^T * P1 + 1/2 *m2 * P2^T * P2

Potential energy: u = m1 * g * y1 + m2 * g * y2

L = T - u 

1.05 有general force 的完整公示

## the manipulator eqs

M(q) * q'' + C(q, q') * q' = Tao_g(q) + B * u

mass matrix + contacts terms = gravatational torque + maps inputs to generalized force * control input (force torque) 

T = 1/2 * q'^T * M(q) * q' >= 0
m(q) > 0

q'' = m^-1(q) * [ Tao_g(q) + B * u - C(q, q') * q' ]

underactuated iff rank[B] < dim(q)