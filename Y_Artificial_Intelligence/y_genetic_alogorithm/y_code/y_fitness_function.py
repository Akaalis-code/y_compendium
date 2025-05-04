#from  y_animation import points
import math
import numpy as np
import os

var_prime_dna = 'dummy_initialization'
try :
    var_my_home_fldr = os.getenv('my_home_fldr')
except :
    print("You need to create a variable in .bashrc file with variable name my_home_fldr and add whatever path that is equivalent to ~")
var_directory = var_my_home_fldr+'/Documents/y_population/y_starting_point'
with open(var_directory+'/y_initial_population.txt', 'r') as var_file:
    var_prime_dna = var_file.read()

var_prime_dna_lst =  list(var_prime_dna)
print(var_prime_dna_lst[3])

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