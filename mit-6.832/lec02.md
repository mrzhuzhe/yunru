# Graphical analysis & Goal Build intuition

> 书 nonlinear Dynamics and chaos - steven H strongatz

## simple Pendulum 悬垂钟摆

T = 1/2 * m * L ^ 2 * theta ^ 2 

u = - m * g * l * cos(theta)

L = T - u

Q = m * l^2 * theta'' + m * g * l * sin(theta) = - b * theta' + u

Given Theta(0) , Theta'(0)

solve Theta(t)

what happen as t -> infinite

1. linearization 
2. Graphical analysis

Even simpler:

u = 0,  b large 

m * l^2 * theta  is k * g * m^2 / s^2

b * theta' >> m * l^2 * theta''

"dimensional analysis"

b k * g * m^2 / s  

b * sqrt(l/g) >> m * l^2

m * l^2 * theta'' + b * theta' simi= b * theta' + m* g *l * sin(theta) = 0

b * x' + m * g * l * sinx = 0

24:00 有图解

![x和x'](pic/fixpoint.png)

region of attraction / sepratrix 

Autapse (shallow neural network)

## 活着的神经元

The Autapse: a simple illustration of short-term analog memory storage by tuned synaptic feedback

神经元和记忆的关系 

记忆门：x' = -x + tanh(w * x + u) 的图形

忘记门：x' = (f-1) * x + tanh(w * x + u)

## Tracking fixed points "biforcation analysis"
