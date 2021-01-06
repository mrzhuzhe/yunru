# Force Control 

- geometric coefficient friction:
manever: flip box off

multi body plan:  MBP
Eqs： m(q) * v' + c(q * v) * v = Lg(q) + B * u + sum J^T * f_Gi 

M_g(q) * v' = M_g(q) * v_d + sum J^T*f_c

if there are no contact 

v' = k_p * ( q_d - q) + ki * Intergrate(k_i (q_d * q)) dt  + kd (q_d' - q')