#from  y_animation import points
import math
import numpy as np

points1 = np.array([[ 8, 73],[37, 71],[65,  9],[99,  8],[65, 49],[18, 39],[98, 28],[41, 74],[74, 87],[68, 74],[17, 29],[71, 71],[ 0, 50],[51, 84],[76, 98],[62, 31],[35, 13],[47,  5],[64, 87],[63, 41]])
points2 = np.array([[37, 71],[ 8, 73],[65,  9],[99,  8],[65, 49],[18, 39],[98, 28],[41, 74],[74, 87],[68, 74],[17, 29],[71, 71],[ 0, 50],[51, 84],[76, 98],[62, 31],[35, 13],[47,  5],[64, 87],[63, 41]])


def mth_fitness_function(point):
    lcl_fitness_val = 0
    for i in range(0,(len(point)-1)):
        lcl_dist_between_two_points = math.sqrt( (point[i+1,0] - point[i,0])**2 + (point[i+1,1] - point[i,1])**2 )
        lcl_fitness_val = lcl_fitness_val + lcl_dist_between_two_points
    return lcl_fitness_val

print(mth_fitness_function(points1))
print(mth_fitness_function(points2))