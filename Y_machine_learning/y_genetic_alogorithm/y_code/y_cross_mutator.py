from pyspark.sql import SparkSession
import numpy as np
import random
import y_fitness_function
 
#[12, 0, 10, 1, 13, 4, 11, 7, 6, 14, 8, 9, 15, 18, 19, 17, 5, 3, 2, 16] --->> 778 fitness factor
#[14, 18, 1, 19, 2, 11, 0, 12, 17, 5, 15, 6, 4, 3, 8, 7, 13, 9, 16, 10] --->> 797 fitness factor
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



for i in range(0,len(var_prometheus_gene_pool)) :
    while True :
        new_index = random.randint(0, 19)
        if new_index in var_parent_gene_2 :
            continue
        else :
            var_parent_gene_2.append(new_index)
            break

print(var_parent_gene_2)
var_kid = y_fitness_function.mth_sequencer(var_parent_gene_2)
print(y_fitness_function.mth_fitness_function(var_kid))

var_ch_1 =[]
var_ch_2 =[]
var_ch_3 =[]
var_ch_4 =[]
var_ch_5 =[]
def mth_cross_mutation(para_parent_1 , para_parent_2):
    for i in range(0,len(var_prometheus_gene_pool)):
        if i<10 :
            var_ch_1.append(para_parent_1[i])
            var_ch_2.append(para_parent_1[19-i])
        else :
            var_ch_1.append(para_parent_2[i])
            var_ch_2.append(para_parent_2[19-i])
        
        if i<5 or (i>10 and i<15) :
            var_ch_3.append(para_parent_1[i])
        else :
            var_ch_4.append(para_parent_2[i])

