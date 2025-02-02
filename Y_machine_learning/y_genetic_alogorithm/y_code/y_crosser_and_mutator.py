#from pyspark import sparksession
import numpy as np
import random
import y_fitness_function
 

var_prometheus_gene_pool = np.array([[ 8, 73],[37, 71],[65,  9],[99,  8],[65, 49],[18, 39],[98, 28],[41, 74],[74, 87],[68, 74],[17, 29],[71, 71],[ 0, 50],[51, 84],[76, 98],[62, 31],[35, 13],[47,  5],[64, 87],[63, 41]])

var_parent_gene_1 = []
var_parent_gene_2 = []


for i in range(0,len(var_prometheus_gene_pool)) :
    while True :
        new_index = random.randint(0, 19)
        if new_index in var_parent_gene_1 :
            continue
        else :
            var_parent_gene_1.append(new_index)
            break

print(var_parent_gene_1)
var_kid = y_fitness_function.mth_sequencer(var_parent_gene_1)
print(y_fitness_function.mth_fitness_function(var_kid))



# for i in range(0,len(var_prometheus_gene_pool)) :
#     while True :
#         new_index = random.randint(0, 19)
#         if new_index in var_parent_gene_2 :
#             continue
#         else :
#             var_parent_gene_2.append(new_index)
#             break

# print(var_parent_gene_2)
# print(var_parent_gene_1)