from pyspark.sql import SparkSession
import numpy as np
import random
import y_fitness_function
import math

var_prometheus_gene_pool = []
var_parent_gene_1 = []
var_parent_gene_2 = []
var_parent_gene_3 = []
var_parent_gene_4 = []





var_offspring_gene_1 = []
var_offspring_gene_2 = []
var_offspring_gene_3 = []

var_offspring_gene_4 = []
var_offspring_gene_5 = []
var_offspring_gene_6 = []



with open(var_directory+'/y_primal_data.json', 'r') as var_file:
    data = json.load(var_file)

print("Gene_pool_test1",data["Gene_pool_test1"])
print("Parent_gene_1",data["Parent_gene_1"])
print("Parent_gene_2",data["Parent_gene_2"])
print("Parent_gene_3",data["Parent_gene_3"])
print("Parent_gene_4",data["Parent_gene_4"])


var_prometheus_gene_pool = data["Gene_pool_test1"]
var_parent_gene_1 = data["Parent_gene_1"]
var_parent_gene_2 = data["Parent_gene_2"]
var_parent_gene_3 = data["Parent_gene_3"]
var_parent_gene_4 = data["Parent_gene_4"]


# for i in range(0,len(var_prometheus_gene_pool)) :
#     while True :
#         new_index = random.randint(0, 19)
#         if new_index in var_parent_gene_1 :
#             continue
#         else :
#             var_parent_gene_1.append(new_index)
#             break

# print(var_parent_gene_1)
# var_kid = y_fitness_function.mth_sequencer(var_parent_gene_1)
# print(y_fitness_function.mth_fitness_function(var_kid))


def mth_cross_mutation(para_parent_1 , para_parent_2 , para_offspring_number):
    var_offspring_gene_temp = var_parent_gene_1
    for i in range(0,len(var_prometheus_gene_pool)):

        var_best_sequence = distance_evaluator()


def distance_evaluator(para_combination_1 , para_combination2):
    var_comb1_x1 = var_prometheus_gene_pool[para_combination_1[0]][0]
    var_comb1_y1 = var_prometheus_gene_pool[para_combination_1[0]][1]
    var_comb1_x2 = var_prometheus_gene_pool[para_combination_1[1]][0]
    var_comb1_y2 = var_prometheus_gene_pool[para_combination_1[1]][1]
    var_comb1_distance = math.sqrt((var_comb1_x1 - var_comb1_x2)**2 + (var_comb1_y1 - var_comb1_y2)**2)

    var_comb2_x1 = var_prometheus_gene_pool[para_combination_2[0]][0]
    var_comb2_y1 = var_prometheus_gene_pool[para_combination_2[0]][1]
    var_comb2_x2 = var_prometheus_gene_pool[para_combination_2[1]][0]
    var_comb2_y2 = var_prometheus_gene_pool[para_combination_2[1]][1]
    var_comb2_distance = math.sqrt((var_comb2_x1 - var_comb2_x2)**2 + (var_comb2_y1 - var_comb2_y2)**2)

    if var_comb1_distance<var_comb2_distance :
        return 1
    else :
        return 2
