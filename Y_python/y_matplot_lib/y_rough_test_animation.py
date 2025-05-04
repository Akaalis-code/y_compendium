from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Initialize the figure and axes
fig, (Axes1, Axes2) = plt.subplots(1, 2)

# Setting the x and y limits for each subplot
Axes1.set_xlim(0, 10)
Axes1.set_ylim(-2, 2)
Axes2.set_xlim(0, 4)
Axes2.set_ylim(-2, 2)

# Initializing line variables for the animation
line1, = Axes1.plot([], [], lw=3)
line2, = Axes2.plot([], [], lw=3)

# Data initialization function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Animation function
def animate(i):
    x1 = np.linspace(0, 10, 1000)
    y1 = np.sin(2 * np.pi * (x1 - 0.01 * i))
    line1.set_data(x1, y1)
    
    x2 = np.linspace(0, 4, 1000)
    y2 = np.cos(2 * np.pi * (x2 - 0.01 * i))
    line2.set_data(x2, y2)
    
    return line1, line2

# Creating the animation
anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

# To save the animation into a video format
#anim.save('continuousSineWave.mp4',writer = 'ffmpeg', fps = 30) 
# Displaying the plot
plt.show()
