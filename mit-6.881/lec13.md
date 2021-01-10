# Force Control 2

TD learning
多种控制方式的不同的演示:
https://slides.com/russtedrake/fall20-lec13#/12


- colab 演示
flip a box
edge following 这里有一篇论文

- Direct force control vs Indirect force control

act like a mechanical system that applies forces

m * x'' + b * x' + k * ( x - x0 ) = f_c

"stiffness control"

f_c = 0;

"positivity theory" ( Port - Hamiltonion system )

- 这里演示了通过两个手指（点）接触盒子让盒子翻转的受力情况力矩的演示

known nothing about the box

- Impedance Control 阻尼控制
can also change the effective mass
可以精确控制执行器等的速度

using compliance in lieu of sensory feedback for automatic assembly by samuel hunt drake

- peg in hole

"remote center of compliance" RCC

Q: what is the best center of compliance ?

这个地方讲了一个机器人做沙拉的例子

- how do you do stiffness / impedance control manipulator

one joint: 将系统建模成 spring mass damper system

ma  = gravity + control input +  contact force

这里有两个视频演示
1. Joint Impedance control:
2. end-effector Impedance control
change coordinates from q -> xee

补偿阻力 补偿重力

- 为何要做更精确的阻尼控制，而不是末端执行器控制？

you assume that you know where the contact is happening！

- how joint impediance control robot different from pd control

soft 

- summary

mechanic control 
impediance control

