# lec16 humandroid

这一课暂无阅读 

查了一下 PGP 加密  `https://www.openpgp.org/`

本周恢复网站，转为 next graphql 架构

晚上看了 plc 的情况 ，用的是西门子的， 在考虑工控分工的问题

还有时间分配

## rew

traj, LQR, SOS

## 动量系统

m * x'' = sum(Fi)

m * z'' = sum(Fjz) - m * g

TQ'' * sum[Ci * Fi] = sum(r_i * f_i_theta - r_i * F_x)

Fiz >=0, |Fiz| <= u * Fiz

有许多推进器， 其中 Fi 都很小， ｜r'｜ 要遵守速度限制 , r'|f| = 0 动量系统要一直平衡 但是 突然会有很大的力量在预固的定位置

会出现不稳定步态

## 不需要做成无重力腿

X_com(q) + total angular momentum around Com

I * theta'' = sum (r_iz * F - r_i_theta * F_i_theta)

r_i = P_i - [i, q]

重力中心： X_com = sum (Xi * mi ) / sum (mi)

压力中心: X_cop = sum(Pi * Fiz) / sum(Fiz) 

r_i = P_i - [x, z]

( m * z'' + m * g ) * ( Xcop - x ) = ( Zcop - Z ) * m * x' - I * theta'

## 零动量点

在平地上 X_com 是凌动量点

time stage walking plan/control 

1. foot step planning 
2. plan Com/Cop
3. fill in the details (q, q')

后面有很酷的脚步规划的演示
