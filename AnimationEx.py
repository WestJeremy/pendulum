import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata=(frame)
    ydata= (np.sin(frame))
    ln.set_data(xdata, ydata)
    print(ln)
    return ln,

ani = FuncAnimation(fig, update, frames=10,
                    init_func=init, blit=True)
plt.show()