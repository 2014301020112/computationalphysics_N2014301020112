import math
import matplotlib.pyplot as plt
# import modules
g=9.8
# set constants
class cannon0:
    "the simplest model with no air drag, no air density variance, no probability distribution"
    def __init__(self,v0,theta):
        self.x0=0
        self.y0=0
        self.v0=v0
        self.theta=theta*math.pi/180
        self.vx0=self.v0*math.cos(self.theta)
        self.vy0=self.v0*math.sin(self.theta)
        self.dt=0.01        
        return None
        
    def fly(self):
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        while not(self.Y[-1]<0):
            newVx=self.Vx[-1]
            newVy=self.Vy[-1]-g*self.dt
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            meanVx=0.5*(self.Vx[-1]+self.Vx[-2])
            meanVy=0.5*(self.Vy[-1]+self.Vy[-2])
#            meanV=math.sqrt(meanVx**2+meanVy**2) #not used in Cannon0 because there is no air drag
            newX=self.X[-1]+meanVx*self.dt
            newY=self.Y[-1]+meanVy*self.dt
            self.X.append(newX)
            self.Y.append(newY)
        r=-self.Y[-2]/self.Y[-1]
        self.X[-1]=(self.X[-2]+r*self.X[-1])/(r+1)
        self.Y[-1]=0
        return 0
        
    def plot(self, color):
#        col=str(color)
#        plt.plot(X,Y)
        plt.plot(self.X,self.Y,color,label="$v_0$=%d,$theta$=%d degrees"%(self.v0,self.theta))
        return 0

class cannon1(cannon0):
    "the second simplest model with air drag independent with air pressure"
    def fly(self):
        
        return 0

# Definition of Classes and 

A=cannon0(20,45)
A.fly()
A.plot('blue')
