# Bin Picking part 1

- a little taste of multibody dynamics

MBP -> 
q' = f(q, q', u) 
v'= f(q, v, u)

time step >= 0

v[n+1] = f(q[n], v[n], u[n])

M(q) * v' + C(q, v) * v = Cg(q) + ... + sum J^T(q) * F_ci
mass matrix             = gravity + joint friction actuator inputs + contact spatial Jacobian

contact forces 
find q v = 0， v'= 0
- Cg (q) = sum J^T(q) * F_ci

sum f_wi_ci = - mg
sum f_ci_wx = 0

contact friction:

f_c_cx - tangential from ( friction )
f_c_cz - normal force

|f_c_cx| <= u * |f_c_cz| 
coefficient of (state) friction

u_dynamic - sliding friction
LCP "time-stepping"
Penetrations happen

Optimization approach to static equilibarium

Cg(q) = - sumJ^T(q) * f_ci
| f_cx_ci | <= u * | f_ci_cz |

"complementprity constraints"
signed distance / penetration depth

- hydroelastic
1.04:22
rigidbodydynamics.jl
pov-ray