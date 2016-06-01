﻿# 第九次作业

标签（空格分隔）： 未分类

---

#the chaos
###Abstract
######To say when we adjust some parameters in our model, the model's behavior will change severely. In that case, the chaos appears. Chaos exists in many nonliear systems. Here we only use a dirving force pendulum to illustrate.
###basic principle
######the nonliear pendulum's ODE is:![此处输入图片的描述][1]
######Now we focus our attention on the parameter Fd, the amplitude of the driving force. It is easy to say when we increase Fd, the pendulum's oscillation model changes. When Fd is small, the final osdillation is just like the linear harmonic pendulum, but as we increase, the oscillation model becomes more complex and the period changes. 
######The chaos is that the results can be determined if we know the initial conditions clearly,but once we change the initial coniditions even slightly, the result will be totally different with the previous results.
######For a harmonic pendulum we can say that at each point satisfing this condition will have the same angular velocity,so the graph for these angles and angular velocity is a horizontal line. But if we draw this graph for the dirving force nonlinear pendulum model. the situation will be more complex, this will lead to some term called strange attractor. The graph is not only seeming complicate but also it has precise structure in detail. The situation fractal also exists.
###the computation results
######the initial condition influence(fd=1.2)
![此处输入图片的描述][2]
######fd=1.4
![此处输入图片的描述][3]
######the phase space(fd=0.5)
![此处输入图片的描述][4]
######fd=1.2
![此处输入图片的描述][5]
######the strange attractor(fd=1.2,x0=0.1,frequency=2/3)
![此处输入图片的描述][6]
######the strange attractor(fd=1.2,x0=3.0,frequency=2/3)
![此处输入图片的描述][7]
######the strange attractor(fd=1.2,x0=0.1,frequency=1/3)
![此处输入图片的描述][8]
######the strange attractor(fd=1.2,x0=0.1,frequency=2/3)(at \pi/4)
![此处输入图片的描述][9]
######the bifurcation(x0=0.1,frequency=2/3)
![此处输入图片的描述][10]


  [1]: http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2%5Ctheta%7D%7Bdt%5E2%7D=-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta-q%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D&plus;F_%7BD%7Dsin%28%5COmega_%7BD%7Dt%29
  [2]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/chaos%20initial1.png
  [3]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/chaos%20initial2.png
  [4]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/the%20angle%20velocity.png
  [5]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/the%20angle%20velocity2.png
  [6]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/chaos33.png
  [7]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/chaos%201.2%202.0.png
  [8]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/chaos%20with%20frequency1%283%29.png
  [9]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/chaos44.png
  [10]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/bifurcation.png
