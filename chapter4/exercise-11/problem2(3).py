import numpy as np
import matplotlib.pyplot as plt
import math
def orbits(x0,vy10,a,tt):
    au=149597870700.0
    yr=31558150.0
    G=6.67*10**(-11)
    Ms=1.989*10**(30)
    K=G*Ms
    x1=[]
    y1=[]
    vx1=[]
    vy1=[]
    vx1.append(0)
    vy1.append(vy10)
    x1.append(x0)
    y1.append(0)
    t=[]
    t.append(0)
    tau=0.00001
    t1=[]
    the=[]
    x2=[]
    y2=[]
    for i in range(tt):
        x1.append(x1[-1]+vx1[-1]*tau)
        y1.append(y1[-1]+vy1[-1]*tau)
        r1=math.sqrt((x1[-1])**2+(y1[-1])**2)
        vx1.append(vx1[-1]-4*math.pi**2*(x1[-1])*(1/r1**3+a/r1**5)*tau)
        vy1.append(vy1[-1]-4*math.pi**2*(y1[-1])*(1/r1**3+a/r1**5)*tau)
        t.append(t[-1]+tau)
        if abs(r1-x0)<0.000000005:
            t1.append(t[-1])
            the.append(math.asin(y1[-1]/r1))
    return x1,y1,t1,the
def fit(x,y):
  if len(x)!=len(y):
    return 0,0
  else:
    xx=0
    yy=0
    xy=0
    x22=0
    for i in range(len(x)):
        xx=xx+x[i]
        yy=yy+y[i]
        xy=xy+x[i]*y[i]
        x22=x22+x[i]**2
    xx=xx/len(x)
    yy=yy/len(x)
    xy=xy/len(x)
    x22=x22/len(x)
    ta=(xx*yy-len(x)*xy)/(xx**2-len(x)*x22)
    tb=(xx*xy-x22*yy)/(xx**2-len(x)*x22)
    return ta,tb
x,y,t,tte=orbits(0.47,8.2,0.0008,200000)
tx,ty=fit(t,tte)
p=[]
for i in t:
    p.append(tx*i+ty)
plt.plot(t,p)
for k in range(len(t)):
    plt.scatter([t[k],],[tte[k],], 5, color ='red')
plt.xlim(0,)
plt.ylim(0,)
plt.xlabel('time(yr)')
plt.ylabel('theta(degrees)')
plt.title('orbit orientation versus time(a=0.0008)')
plt.show()

"""
tr=[0,0.0004,0.0008,0.001,0.002,0.003,0.0035]
tc=[]
for i in tr:
    x,y,t,tte=orbits(0.47,8.2,i,200000)
    tx,ty=fit(t,tte)
    tc.append(tx)
ta,tb=fit(tr,tc)
p=[]
for i in tr:
    p.append(ta*i+tb)
plt.plot(tr,p)
for k in range(len(tr)):
    plt.scatter([tr[k],],[tc[k],], 7, color ='red')
plt.xlim(0,)
plt.ylim(0,)
plt.xlabel('time(yr)')
plt.ylabel('angular speed(degrees/yr)')
plt.title('procession rate versus a')
plt.show()
