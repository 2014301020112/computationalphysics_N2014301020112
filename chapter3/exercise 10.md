﻿#第十次作业

标签（空格分隔）： 

##the lorenz model and the billiard problem

###abstract
######understand the chaos in the lorentz model by solving this set of ODE numerically. Building model to deal with the extending billiard problem with various boundary shape.
###fundamental principle
######To further understand that in a system where exists chaos, even a slight initial condition change can lead to severe difference of result. We consider a more sophisticated system which is used in the prediction of the whether. the set of ODE is 
######![此处输入图片的描述][1]
######![此处输入图片的描述][2]
######![此处输入图片的描述][3]
######Since we adjust the parameter in these ODEs carefully can we find the chaos phonemon and strange attractor.
######for the billiard problem, we neglect the drag acting on the moving ball, and we assume every collision between the boundary and the ball is elastic and it obeys optical reflection. this means the speed component on the tangent remain the previous value, but the speed component on the normal reverse.
###the numerical result 
######first is the phase gragh is the different regime(in this result we let the sigma equals to 10.0,b=8/3 and r=25.0)
######![此处输入图片的描述][4]
######![此处输入图片的描述][5]
######![此处输入图片的描述][6]
######we can say the deviation of cross section of y-z is opposite to x-z.
######then we consider the circular stadium (r=1):
######![此处输入图片的描述][7]
######then the more realistic situation  with a little separarion (r=1,l=0.02):
######![此处输入图片的描述][8]
######then consider the more large separation:(r=1,l=0.2)
######![此处输入图片的描述][9]
######we now consider the more complex situation when the stadium is a elliptical (a=2,b=3)
######![此处输入图片的描述][10]
######for fun consider the stadium with a heart shape.
######![此处输入图片的描述][11]
######we can say clearly in the shape of the heart and big separation model there is no some internal machinism in it as the larger the running time, the more area is occpuied by the lines.
###Reference
######Computational Physics, Nicholas J. Giordano & Hisao Nakanishi

######《Python基础教程》

  [1]: http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdx%7D%7Bdt%7D=%5Csigma%28y-x%29
  [2]: http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdy%7D%7Bdt%7D=-xz&plus;rz-y
  [3]: http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdz%7D%7Bdt%7D=-xy-bz
  [4]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/phase1,0.png
  [5]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/phase2.png
  [6]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/phase3.png
  [7]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/circle.png
  [8]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/circle3.png
  [9]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/circle2.png
  [10]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/elliptical.png
  [11]: https://raw.githubusercontent.com/qqyyff/computationalphysics_N2013301020031/master/heart2.png
