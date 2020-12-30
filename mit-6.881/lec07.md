# Geometric Perception

- robust version of messy point clouds
- review : Robust Point Cloud Regastration
as Least-squares IK
model points m_i o_P_m_i
scence points s_i w_P_s_i

Geol: Estimate w_X_o
"correspondences" c_j = j says same point i matures model pt j

case 1: known correspondances:

relation points are invariant to P
m‘ s’ are central points

P_s' = sum P_si / Ns 
o_P_m1 = sum 0_P_mci / Ns

sum |R (o_P_mci - o_P_m1) - (P_si -P_s') | ^2

st: R^T*R=I, det(R)=I

- notebook （ICP）演示
已知点之间的对应关系，把实际物体和模型的映射关系对应上
1. 如果增加一些高斯噪声会如何 29‘
2. 如果有一些离群远点，情况会很差
3. 最小二乘是正确的损失函数么？


- ICP part2 use "closest points" to determine correspondances

other ways point clouds on messy

- Dropout / missed returns
- never same points twice
- detecting outliers
sum ｜ X_o * o_P_mi - P_si | ^2