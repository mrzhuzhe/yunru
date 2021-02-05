# Dynamic Programming 

- Control as optimization
- Ex: Double integrator
- Dynamic Programming algorithm
- numerical optimal control of predulum

m * l^2 * theta'' + b * theta' + m * g * L *sin(theta) = u

Feedback Linearization

u = 2 * m * g * L *sin(theta)

Invert gravity 

m * l^2 * theta'' + b * theta' - m * g * L *sin(theta) = 0

Q Stablizae the unstable fixed pt if |u| <= m * g * l/4

u = sat_(m*g*l/4) (2 * m * g * l * sin(theta))
 = m * g * l * sin(theta)
 = m * g * l / 4
 = - m * g * l / 4

## big Idea Formulate control design as an optimization 

given a trajectory 

x(.) u(.) 

x(.) t in [0, inf] x(t)

assign a score ( scalar )

Potentially, also set constraints |u(t)| <=1  x(t_f) = x_goal

Goal find "policy"  u = Pi(t, x)
which optimizes (minimize) the cost ideally for all t, x

Numerical approx.

Example: minimum time problem for the double integrator

q'' = u |u|<= 1

get to q' = q = 0 in min time

acclerate （full throttle）then slam on the brakes 

q'' = u   u = -1  q'(t) = q'(0) - t

q'(t) = q(0) - t

q(t) = q(0) + t * q'(0) - 1/2 * t^2


## min time is closely related to shortest path problems

shorest path via dynamic programming 

discrete 
    states s_c in S
    actions a_i in A
    dynamics s[n+1] = f(s[n], a[n])

cost function:
    one-step cost g(s, a)
    total cost sumg g(s[n], a[n])


key idea addtive cost. 
F[dt * g(x(t), u(t))]

Reccursive form 

J(s_i) = min sum g(s[n], a[n])

Pi(s_i) =  min [g(s, a) + J(f(s_i, a))]

single-time step one-step + cost-to-go from the next state

随机初始化 value iteration or dynamic programming infinite horizon

guarantee to converge to J^asterisk even asynchronous

## limitation 

- accouacy for continuous systems discretization error

- scale curse of dimensionally

- Deeper assume full state information 


