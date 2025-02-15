import numpy as np
import os

var_locations = np.array([[8, 73],[37, 71],[65,  9],[99,  8],[65, 49],[18, 39],[98, 28],[41, 74],[74, 87],[68, 74],[17, 29],[71, 71],[ 0, 50],[51, 84],[76, 98],[62, 31],[35, 13],[47,  5],[64, 87],[63, 41]])


try :
    var_my_home_fldr = os.getenv('my_home_fldr')
except :
    print("You need to create a variable in .bashrc file with variable name my_home_fldr and add whatever path that is equivalent to ~")

var_directory = var_my_home_fldr+'/Documents/y_population/y_starting_point'
if not os.path.exists(var_directory):
    print(" y_log : Path doesnt exist , creating now ")
    os.makedirs(var_directory)
    
with open(var_directory+'/y_initial_population.txt', 'w') as var_file:
    var_file.write(str(var_locations))


    