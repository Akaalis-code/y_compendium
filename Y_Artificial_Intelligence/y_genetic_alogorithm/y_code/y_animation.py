import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

plt.style.use('fivethirtyeight')

# Available values for GENES , that is list of all locations
points = np.array([[ 8, 73],[37, 71],[65,  9],[99,  8],[65, 49],[18, 39],[98, 28],[41, 74],[74, 87],[68, 74],[17, 29],[71, 71],[ 0, 50],[51, 84],[76, 98],[62, 31],[35, 13],[47,  5],[64, 87],[63, 41]])
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

y_test_frames = [12, 0, 10, 1, 13, 4, 11, 7, 6, 14, 8, 9, 15, 18, 19, 17, 5, 3, 2, 16]
var_clone = []
for i in y_test_frames :
    var_clone.append(points[i])
var_clone= np.array(var_clone)
def update(frame):
    frame = frame
    xdata = [var_clone[frame, 0], var_clone[frame + 1, 0]]
    ydata = [var_clone[frame, 1], var_clone[frame + 1, 1]]
    lines[frame].set_data(xdata, ydata)
    return lines

# Create the animation

ani = animation.FuncAnimation(fig, update, frames=range(19), init_func=init, blit=True ,repeat=True)




# for doing full screen of plot
mng = plt.get_current_fig_manager().full_screen_toggle()

# Display the animation
plt.show()
