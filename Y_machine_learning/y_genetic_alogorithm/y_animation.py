import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

plt.style.use('fivethirtyeight')

# Available values for GENES , that is list of all locations
points = array_2d = np.array([[ 8, 73],[37, 71],[65,  9],[99,  8],[65, 49],[18, 39],[98, 28],[41, 74],[74, 87],[68, 74],[17, 29],[71, 71],[ 0, 50],[51, 84],[76, 98],[62, 31],[35, 13],[47,  5],[64, 87],[63, 41]])
# Generate 10 random points
#points = np.random.randint(0, 100, (20, 2))

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Scatter plot of the points
sc = ax.scatter(points[:, 0], points[:, 1], c='red', s=50)

# Initialize the lines to be animated
lines = []

# Function to initialize the animation
def init():
    for _ in range(19):
        line, = ax.plot([], [], c='blue')
        lines.append(line)
    return lines

# Function to update the animation
def update(frame):
    xdata = [points[frame, 0], points[frame + 1, 0]]
    ydata = [points[frame, 1], points[frame + 1, 1]]
    lines[frame].set_data(xdata, ydata)
    return lines

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(19), init_func=init, blit=True)

# for doing full screen of plot
mng = plt.get_current_fig_manager().full_screen_toggle()

# Display the animation
plt.show()
