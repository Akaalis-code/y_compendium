#from  y_animation import points
import math
import numpy as np

points1 = np.array([[ 8, 73],[37, 71],[65,  9],[99,  8],[65, 49],[18, 39],[98, 28],[41, 74],[74, 87],[68, 74],[17, 29],[71, 71],[ 0, 50],[51, 84],[76, 98],[62, 31],[35, 13],[47,  5],[64, 87],[63, 41]])
points2 = np.array([[37, 71],[ 8, 73],[65,  9],[99,  8],[65, 49],[18, 39],[98, 28],[41, 74],[74, 87],[68, 74],[17, 29],[71, 71],[ 0, 50],[51, 84],[76, 98],[62, 31],[35, 13],[47,  5],[64, 87],[63, 41]])


def mth_sequencer(para_dna_index) :
    rtn_child = []
    for i in para_dna_index :
        rtn_child.append(points1[i])
    rtn_child = np.array(rtn_child)
    return rtn_child

def mth_fitness_function(para_dna):
    lcl_fitness_val = 0
    for i in range(0,(len(para_dna)-1)):
        lcl_dist_between_two_points = math.sqrt( (para_dna[i+1,0] - para_dna[i,0])**2 + (para_dna[i+1,1] - para_dna[i,1])**2 )
        lcl_fitness_val = lcl_fitness_val + lcl_dist_between_two_points
    return lcl_fitness_val

# print(mth_fitness_function(points1))
# print(mth_fitness_function(points2))