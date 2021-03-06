# Simple model of walking

> http://underactuated.csail.mit.edu/simple_legs.html 

passive dynamic walking

key ideas:
 - contact mechanics (non-smooth mechanics)
 - limit cycle stablility
 
Example (w/s impacts) von dor pol oscillator

q'' + u * (q^2-1) * q' + q = 0, u > 0

linear spring mass model

无阻尼系统就会发散

有阻尼系统会慢慢以圆形回归原点

von der pol

先从原点向外扩散，再呈现一个矩形的周期

## stablity of a trajectory

lim | x(t) - x^*(t) | -> 0

limit cycle stability

a peredric trajectory 

for t > 0 x(t) = x(t + T)

limit cycle stable iff 

min |x(t) - x^*(t)| -> 0

- orbital stability

surface of section 

section is transerevse to the flow all trajectories return to the section 


## poincare Maps 

好像是把下一步和当前步骤映射起来，方便看不动点

fix point x^* = P(x^*)

localstablity via linearization

d(p) / d(x)  x[n+1] = A * x[n]

这里有两个非常重要的图

![步行轨迹循环](http://underactuated.csail.mit.edu/figures/rimless_wheel_phase.svg)

![轨迹事件循环](http://underactuated.csail.mit.edu/figures/kwLimitCycle.svg)


## contact model

刚体柔性接触-弹簧系统

刚体非侵入接触

非弹性碰撞： all energy into ground is lost angular momentum around pt of collision is conserved 



