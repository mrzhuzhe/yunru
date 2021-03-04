# trajectory optimization

> http://underactuated.csail.mit.edu/trajopt.html

## big picture
![big picture](pic/lec10-1.jpeg)

## basic trajectory optimization

1. add x[] as extra decisiton variable 松弛变量
2. solve x[n] as func of x0, u[0], u[1], u[n-1]

![von der pol](pic/lec10-2.jpeg)


## 通用形式

![von der pol](pic/lec10-3.jpeg)