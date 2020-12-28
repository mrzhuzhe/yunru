# Basic pick and place 3

- review:
Differential Inverse kinematics

- Differential Inverse Kinematics as Optimization 
1. V_G = J_G(q) * v
spatial velocity = jacobian * joint velocities
2. v = persuade_inverse(J_G(q)) * V_G  把求伪逆转化为mse回归问题, 这部分似乎和 mls94 上内容不太符合
3. min ｜J_G（q） - V_G｜^2 
st： Vmin <= V && V <= Vmax
joint limits: dont exceed joint limits in next h seconds
qmin <= q + h * v && q + h * v <= qmax
4. 这部分的 notebook 是可视化二项式规划 

- null space of the jacobian 
min | J_G(q) * v - V_G | ^2 + | P(q) ( v - k*(q0 -q))|
st: Vmin <= V <= Vmax

- differential IK Integrator
min | J_G*v - V_G|^2
st: J*v = a*V_G ;  0 <= a <= 1
