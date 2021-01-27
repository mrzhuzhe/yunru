# Planning Under Uncertainty

> https://slides.com/russtedrake/fall20-lec22

## planning though contact

stochastic optimization encode robustness/ use expected value as robustness

john doyle three words abstract
https://scholar.google.com/citations?user=C6DtGmMAAAAJ&hl=en


## pick a book

Expected value not sufficient, risk-senstive Rl , analysis distribution of trajectory

Ramdom initial conditions/ Random friction behavior

how can we interface this with perceptron

Depth image -> Pose Estimate -> ^wX^o

RGB -> CNN -> ^wX^o

RGB -> CNN -> E(X^o) | Var(X^o)

RGB -> CNN -> X^o -> kalman filter -> E(X^o) | Var(X^o)

vision as a noisy sensor

- get distribution of pose/ keypoints /etc  from perceptron

- If we addtionally model the sensors for perception need a model of how E(x) var[x] evolve

- KOSNet: a unified keypoint, Orientation and scale Network for Probabilistic 6D pose Estimation

azimuth 方位角问题

then 

- planning though perceptron "belief space planning" 

例如 "light/dark" domain Rob Pktt

问题：信念网络 和 统计情况计划 类似于 policy planning 和 trajectory planning

问题：belief space equal probabilistic DP / POMDP partially observable markov decision processes


## course wrap-up (what did learn ? what are the frontiers? )

Hardware/ low-level control / parameter estimate / perceptron / DLearning control / RL 

First draft on trying to make a curriculum/ system frame work

RGB -> Pose -> Planning

- Hardware: Position / Force torque control (Torque sensing)   cameras / depth cameras 

- kinematics / Jacobians kinrmatic frame 

- Geometric Perceptron vs Deep Percepton  pose? keypoints? dense descriptors? 

-  Pick and Place more complex ( more clutter, objects to grasp, more dynamics of the objects )

- Force control motion planning / stochastic motuib planning /  RL

trajectory optimization scales very well but subject to local minima 

sample-based motion planning can solve more global problems(trajectories), but in lower dimensions

RL searching / func approximations in policies/ Q functions 

Rl do better in stochastic obejective , distribution over tasks/environments, search for approx, optimal controllers, model free ( inefficient ) / black box optm


- mostly about rigid objects / but much more

collision free (wrong) motion planning

- understanding RL (L4DC) what are the right parameters for a policy Q-function

can we formulize robutstness? for any system / ML components 

distributional robustness

more rigrous specifications for distribution over environments

big data / fleet learning 

## state representation / intuitive physics 

直觉物理学

Task-level planning / task motion planning

## what is actually work

## qustions

domain optimization 
robustness control / online learning VS adaptive control


## 课程结束于12月3日


