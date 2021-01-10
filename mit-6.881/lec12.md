# Force Control 

iiwa上的具体实现
https://frankaemika.github.io/docs/overview.html
翻转：
https://colab.research.google.com/github/RussTedrake/manipulation/blob/master/force.ipynb#scrollTo=eeMrMI0-1Dhu

混合力度控制：（用问题）
https://colab.research.google.com/github/RussTedrake/manipulation/blob/master/exercises/force/hybrid_force_position.ipynb#scrollTo=7FZmK21O-JI_

- geometric coefficient friction:
manever: flip box off

multi body plan:  MBP
Eqs： m(q) * v' + c(q * v) * v = Lg(q) + B * u + sum J^T * f_Gi 

M_g(q) * v' = M_g(q) * v_d + sum J^T*f_c

if there are no contact 

v' = k_p * ( q_d - q) + ki * Intergrate(k_i (q_d * q)) dt  + kd (q_d' - q')

joint sliders -> PID -> In Dy -> force sliders -> plant -> x 

f_1_wz + f_2_wz = - mg - f_2_wz
f_1_wx <=  u * f_1_wz
f_2_wx <= u * f_2_wz

f_1_wx + f_2_wx  <= u * ( f_1_wz + f_2_wz )

u_b <- coefficient of static friction betwwen bar & bin

u_g <- box & gripper

- 这里画了几个刚体受力的图，都是一个方块卡墙壁边上受力的情况

f_A_w in friction cone
f_c_c in friction cone 

f_A_wz <= u * f_A_wx

w_R_c
ask perceptron for orientation of box 

f_A_wx = -f_c_wx
f_A_wz + f_c_wz >= -mg

- 阻尼控制和受力情况的collab演示

- how do we implement this on the kuka

ideal: force sensor at the point of contact

ideal: force sensor at the point of contact -> servo desired forces

more common: force / torque sensor at the wrist

model base approach: 

m(q) * v' + C(q, v) * v = Lg(q) + B*u + sum J^T * f_c

If quasi-static the v = v' = 0

- question
how much newtown in contact force thehold