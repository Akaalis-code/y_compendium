import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#import matplotlib
#matplotlib.use('TkAgg')

# Initialize the same data for both axes
data = np.random.randint(0, 100, size=50)

# Create copies of the data for both subplots
data1 = data.copy()
data2 = data.copy()

# Setup figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2)
bars1 = ax1.bar(range(len(data1)), data1, align="edge")
bars2 = ax2.bar(range(len(data2)), data2, align="edge")

ax1.set_xlim(0, len(data1))
ax1.set_ylim(0, int(1.1 * max(data1)))
text1 = ax1.text(0.02, 0.95, "", transform=ax1.transAxes)

ax2.set_xlim(0, len(data2))
ax2.set_ylim(0, int(1.1 * max(data2)))
text2 = ax2.text(0.02, 0.95, "", transform=ax2.transAxes)

# Variables to keep track of sort completion
sorting_done1 = False
sorting_done2 = False

def bubble_sort1(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            yield data, j, j + 1, n - i - 1
    global sorting_done1
    sorting_done1 = True
    yield data, -1, -1, -1

def bubble_sort2(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 -i ):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            yield data, j, j + 1, n - i - 1
    global sorting_done2
    sorting_done2 = True
    yield data, -1, -1, -1

def update_plot(values):
    data1, idx1_1, idx1_2, sorted_idx1 = values[0]
    data2, idx2_1, idx2_2, sorted_idx2 = values[1]
    
    # Update bars for data1
    for rect, val, i in zip(bars1, data1, range(len(data1))):
        rect.set_height(val)
        if i == idx1_1 or i == idx1_2:
            rect.set_color('red')
        elif sorted_idx1 != -1 and i > sorted_idx1:
            rect.set_color('green')
        elif sorted_idx1 == -1 :
            rect.set_color('green')
        else:
            rect.set_color('blue')
    
    # Update bars for data2
    for rect, val, i in zip(bars2, data2, range(len(data2))):
        rect.set_height(val)
        if i == idx2_1 or i == idx2_2:
            rect.set_color('red')
        elif sorted_idx2 != -1 and i > sorted_idx2:
            rect.set_color('green')
        elif sorted_idx2 == -1 :
            rect.set_color('green')
        else:
            rect.set_color('blue')

    if sorting_done1 != True :
        update_plot.iter_count1 += 1
        text1.set_text("Iterations: {}".format(update_plot.iter_count1))
    else :
        text1.set_text("Iterations: {}".format(update_plot.iter_count1))
    
    if sorting_done2 != True :
        update_plot.iter_count2 += 1
        text2.set_text("Iterations: {}".format(update_plot.iter_count2))
    else :
        text2.set_text("Iterations: {}".format(update_plot.iter_count2))

update_plot.iter_count1 = 0
update_plot.iter_count2 = 0

def combined_bubble_sort(data1, data2):
    bubble_gen1 = bubble_sort1(data1)
    bubble_gen2 = bubble_sort2(data2)
    while not (sorting_done1 and sorting_done2):
        try:
            data1 = next(bubble_gen1)
        except:
            #data1 = (data1, -1, -1, -1)
            data1 = data1
        try:
            data2 = next(bubble_gen2)
        except:
            #data2 = (data2, -1, -1, -1)
            data2 = data2
        yield data1, data2

# Create animation
anim = FuncAnimation(fig, func=update_plot, frames=combined_bubble_sort(data1, data2), interval=0, repeat=False ,cache_frame_data=False)

# Display plot
fig.tight_layout()
plt.show()