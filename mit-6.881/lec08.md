# Geometric perception 3
- review : 
Day1 : clean point clouds / registration (ICP)
Day2 : messy point clouds: Geomssian noise outliers / drop-out generalized correspondances CPD

Today: add constraints: non-penetration free space constraints

min sum Cij ｜R *（o_P_mj - o_P_m'）- (P_si - P_s')｜ ^ 2
st: X_o * o_P_mi <= b , w_P_mj >= 0
R^T * R = I , det(R) = 1

now write pose estimation
sum Cij| R(o_P_mj - o_P_m') - (P_si - P_s')| ^2
st: a^2 + b^2 <= 1 , R * o_P_mi >= 0

prog = mathematical program ()
[a, b] = prog New ()
R = [[a, b], [-b, a]]
prog add cost ()
prog add lornez-cone constraint ()
(SOCP)

In 3D conv(SO(3)) requires schur component + SDP

min sum Cij ｜ R * ( ( o_P_mi - o_P_m') - (P_si - P_s') )｜ ^ 2

Pose estimation / nonlinear optimization

“sequential quadratic programming” SQP

2D: min sum Cij ｜ [[cos(theta), sin(theta)], [ -sin(theta), cos(theta)]] * ( ( o_P_mi - o_P_m') - (P_si - P_s') )｜ ^ 2

more complex objective, but unconstrained

3D: Euler angles:

another major advantage: solve jointly for C, R

sum Cij ｜Xp...｜ ^ 2
loss function: sum l（｜Xp1...ps｜）

Precompute all of our distances if we do “closest points”
sum L min | X * P_mi - P_Si |

distance fields ( aka level sets) signed distance function (SDF)

Last big idea : Free space constraints

non-penetration constraint

DACT: by Tomer Schmidt et. al 2015

SDF for models but also for "observation SDF"

- Summery for Geometric Perception Is
1. point cloud regristration as (inverse) kinematics
2. To get all of the benefits of 
 robust outlier objectives / non-penetration / free space constraints / nonlinear optimization / but no garantees 

 - question
 extact local features