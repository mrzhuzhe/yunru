# lec17 "compute" planning 

ai 图搜索， 目标：计算去发现全局最优解（如果存在），来产生最优计划

1. 拆解非凸问题，然后在拆解后的问题中搜索
2. 随机运动搜索

最小化 sum(x[n] - x_goal)^T * Q * (...) 

s.t: x[n+1] = A * x[n] + B * u[n]

## 多边形线性约束 

{ x | A*x <= b }

## disjunction constraints w/integer variables (binary) Ci[n] in {0, 1}

ai * x[n] >= b - Ci[n] * M,  sum(Ci[n]) >= 1

## 凸分割 IRIS

## random motion planning

采样计划 RTT 随机树， 这一部分在 6.881 中有 这里就不重复写了

voronum bias 随机树搜索法

1. 更好的采样分布欧： 用周围的节点来引导
2. 更好的分布度量
3. better extent 例如 轨迹优化

<< real time motion planning for aglie autonomous velchicles >>





