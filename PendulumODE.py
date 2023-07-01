import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Pendulum:
    def __init__(self,tai,tvi,tpi,u,g,L,timestep):
        self.u=u
        self.g=g
        self.L=L
        self.t=timestep
        self.tv=tvi
        self.tp=tpi
        self.ta= tai
        self.fstate=[[],[],[]]

    def geta(self):
       self.ta = (-self.u*self.tv-(self.g/self.L*np.sin(self.tp)))
       #print(f'acceleration is: {self.ta}')
       #self.fstate[0]=(-self.u*self.tv-(self.g/self.L*np.sin(self.tp)))
       return self.ta

    def getv(self):
        self.tv = self.ta*self.t + self.tv

        #self.fstate[1]=self.ta*self.t + self.tv
        return self.tv

    def getp(self):
        self.tp = 0.5*self.ta*self.t**2 + self.tv*self.t+self.tp

        #self.fstate[2]=0.5*self.ta*self.t**2 + self.tv*self.t+self.tp
        return self.tp
    
    def poststate(self):
        self.geta()
        self.getv()
        self.getp()
        # print(self.fstate)
        # self.ta,self.tv,self.tp=self.fstate

    def theta2xy(self):
        X=np.sin(self.df['angle'])*self.L
        Y=np.cos(self.df['angle'])*self.L
        self.df.insert(1, 'X', X, True)
        self.df.insert(2, 'Y', -Y, True)

    def runsim(self,Time):
        TA=np.arange(0,Time+self.t,self.t)
        data=[TA,[1],[2],[3]]
        print(data)
        
        for T in TA:
            data[1].append(self.geta())
            data[2].append(self.getv())
            data[3].append(self.getp())
            # data[1].append(self.ta)
            # data[2].append(self.tv)
            # data[3].append(self.tp)
            # self.poststate()
            
        print(data)
        self.df = pd.DataFrame(np.transpose(data),columns=['Time','acceleration', 'velocity', 'angle'])
        
        self.theta2xy()
        print(self.df)

class Anim:
    def __init__(self,Pend):
        
        self.P=Pend
        self.L=self.P.L*1.125
        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.ax.set_xlim(-self.L, self.L)
        self.ax.set_ylim(ymin=-self.L, ymax=self.L)
        self.ax.axis('equal')

    def update(self,i):
            #print(f'i is {i}')
            x=self.P.df['X'][i]
            y=self.P.df['Y'][i]
            self.ln.set_data([0,x],[0,y])
            self.Pos.set_data(x, y)
            self.acc.set_data([0,self.P.df['acceleration'][i]],[0,0])
            plt.title(f"Time:{np.round(self.P.df['Time'][i],3)} Angle:{np.round(self.P.df['angle'][i],3)}")
            

    def plotinit(self):
        self.ln, = self.ax.plot([], [],'k-')
        self.Pos, = self.ax.plot([], [], 'ro')
        self.acc, = self.ax.plot([], [], 'b-')

    def playsim(self):
        ani = FuncAnimation(self.fig, self.update, frames=len(self.P.df),
                            init_func=self.plotinit, blit=False)
        plt.show()
    



P1=Pendulum(0,6.1,5,.1,9.8,1,.025)
P2=Pendulum(0,0,1,0.0,9.8,1,1)

P2.runsim(2)
A1=Anim(P2)
A1.playsim()

