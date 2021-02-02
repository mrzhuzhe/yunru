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

