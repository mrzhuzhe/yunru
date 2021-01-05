# Geometric Perception

ICP 就是 NN算法 用kd树做的  nn算法天然就有很多处理outliner的法子吧
物体分割库 labelfusion http://labelfusion.csail.mit.edu/

广义对应关系，软对应关系

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
ponits with large distance on others

- ransac (random sample consensus)
在下采样后获取大部分都是线性点

- 我们是否可以判定哪些点在旋转后是不变的
Y： pairwise distances between points
if dij is same points is dissimiler to all 
dij in model points , then either i or  is a outlier or both

max clique in graph of pairwise distances


- generalizing correspondence

min sum sum Cij * | X_o * P_mj - P_si | ^2
Cij = {0,1} Ns * Nm

coherent point drift (CPD)

Cij = [0, 1] Ns * Nm
probility of scene i corresponding to model j 

Cij = 1 / ai * e ^ -1/2 * | Xp_mj * P_si / phi^2|

MIP： mixed - integer program
SDP： relaxtion semi-definite program



