# Reinforcement Learning 1

只有slides: https://slides.com/russtedrake/fall20-lec17

- learning dexterity
1. make the simulator
2. write cost function
3. deep policy gradient

from plans to policies

- Model predictive control (MPC)

measure current x[n]

make plan u[n] u[n+1] ....

excecute u[n]

throw away and replan at n + 1

- full-state-feedback:

u -> Plant MBP - y -> state Estimator (or cheat parts pose estimate) - x^ -> Full-stack Feedback (RRT MPC) -> u

- output-feedback:

u -> Plant - y -> Control(PI) -> Diff IK -> u

pixels-to-torques

- Optimal feedback Control: fint u = PI(y)

reinforcement Learning: model-free (no plant model required)


- whether search for policy or whether search for q function

policy search in RL
u = PI_theta(y) eg. deep net

opportunity to use latent representations from perceptron 

- 跳跃机器人
http://www.ai.mit.edu/projects/leglab/robots/robots.html

- visuomotor policies

levine finn JMLR 2016

boundary of model free


- how do we define our objective ?
g(x_0 , theta) simulation function that outputs cost / reward = ( deley params, initial conditions )

over initial condition , simulation params, noise / disturbances

- openai baseline

domain randomization 


- how do we optimize that objective
two cases that we really understand
1. tabular markov decision proccess (MDP), 只有一小部分离散的状态，action，离散时间 policy iteration
2. linear gaussian ( e.g quadratic cost )
g(x_0. theta) = integral( x^T * Q * x + u^T * R * u ) * dt

policy gradient: key-idea x(t) = integral(e^(a-bR) * x(0)) * dt

more general, cont compute E[g(theta)] explicetly

approximate it Monte-carlo: E[g(theta)] ~ 1/N * sum g_i(theta)

Policy gradient approx : 1/N * sum g_i(theta)

if "differentiable simulator"  

differentiable physics: differentiable rendering is still hard

- true gradient
1. monte carlo for E[] + true sim gradients
2. policy gradient RL (use gradient for policy but assume no plant model)
3. black-box optimization: toolbox: nevergrad(FAIR) 

covariant matrix https://en.wikipedia.org/wiki/CMA-ES

- Evolution strategies as a scalable alternative to reinforcement learning

- min E[g(u)] simulation function 

- policy - gradient trick: 

u - p_theta(u) neural network + gaussian

phi E[g(u)] / phi theta = E [g(u) * phi log(P_theta(u))]    gradient of log probability

