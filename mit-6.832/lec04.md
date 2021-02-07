# continue dynamic programming

> http://underactuated.csail.mit.edu/dp.html

HJB sufficiency theorem

## 回顾

Pi(s) = argmin[g(s, a) - J^asterik * (f(s, a))]
 
Hamilton - jacobian - bellman EQ


## linear Quadratic regulator 

x - A * x + B * u

x = [[0 , 0], [1, 0]] * x + [0, 1] * u 

g(x, u) = x^T * Q * x + u^T * R * u

Q R 正定


0 = min [g(x, u)+ thetaJf(x,u)/thetax] = min [x^T * Q * x + u^T * R * u + 2*x^T*S*(A*x + B*u)]

# Numerical approach to continuous actions 


