import numpy as np
import os
import random
from pyspark.sql import SparkSession
# import y_fitness_function as fvf


# Below is the source of all possible values that the gene can have
var_locations = list(np.array([[8, 73],[37, 71],[65,  9],[99,  8],[65, 49],[18, 39],[98, 28],[41, 74],[74, 87],[68, 74],[17, 29],[71, 71],[ 0, 50],[51, 84],[76, 98],[62, 31],[35, 13],[47,  5],[64, 87],[63, 41]]))


try :
    var_my_home_fldr = os.getenv('my_home_fldr')
except :
    print("You need to create a variable in .bashrc file with variable name my_home_fldr and add whatever path that is equivalent to ~")

var_directory = var_my_home_fldr+'/Documents/y_genetic_algorith_space/y_population/y_starting_point'


if not os.path.exists(var_directory):
    print(" y_log : Path doesnt exist , creating now ")
    os.makedirs(var_directory)
    print(" y_log : Succesfully created")
    
with open(var_directory+'/y_initial_population.txt', 'w') as var_file:
    var_file.write(str(var_locations))



# var_p_dna_1 = []
# var_p_dna_2 = []
# var_p_dna_3 = []
# var_p_dna_4 = []

# var_directory_1 = var_my_home_fldr+'/Documents/y_population/y_generations'
# if not os.path.exists(var_directory_1):
#     os.makedirs(var_directory_1)

#     for i in range(0,len(var_locations)) :
#         while True :
#             var_rand_int = random.randint(0, (len(var_locations)-1))
#             if var_rand_int in var_p_dna_1 :
#                 continue
#             else :
#                 var_p_dna_1.append(var_rand_int)
#                 break
#         while True :
#             var_rand_int = random.randint(0, (len(var_locations)-1))
#             if var_rand_int in var_p_dna_2 :
#                 continue
#             else :
#                 var_p_dna_2.append(var_rand_int)
#                 break
#         while True :
#             var_rand_int = random.randint(0, (len(var_locations)-1))
#             if var_rand_int in var_p_dna_3 :
#                 continue
#             else :
#                 var_p_dna_3.append(var_rand_int)
#                 break
#         while True :
#             var_rand_int = random.randint(0, (len(var_locations)-1))
#             if var_rand_int in var_p_dna_4 :
#                 continue
#             else :
#                 var_p_dna_4.append(var_rand_int)
#                 break

# print(var_p_dna_1 , len(var_p_dna_1))
# print(var_p_dna_2 , len(var_p_dna_2))
# print(var_p_dna_3 , len(var_p_dna_3))
# print(var_p_dna_4 , len(var_p_dna_4))

# ss = SparkSession.builder.appName("initial data").getOrCreate()
# #students_df=ss.createDataFrame( [(1,'rama','physics'),(2,'raju','maths'),(1,'rama','maths')]  ,  ('ID','name','subject'))

# var_generation = '1'
# from pyspark.sql.types import *
# my_schema = StructType([
#                             StructField("ID", IntegerType(), True) ,
#                             StructField("GENERATION_ID", StringType()),
#                             StructField("DNA", ArrayType(IntegerType())),
#                             StructField("FITNESS_VALUE", IntegerType()),
#                             StructField("PARENT_ID1", IntegerType()),
#                             StructField("PARENT_ID2", IntegerType()),
#                         ])
# my_data =   [\
#                 (1,var_generation,var_p_dna_1,fvf.mth_fitness_function(var_p_dna_1),0),\
#                 (2,var_generation,var_p_dna_2,fvf.mth_fitness_function(var_p_dna_2),0),\
#                 (3,var_generation,var_p_dna_3,fvf.mth_fitness_function(var_p_dna_3),0),\
#                 (4,var_generation,var_p_dna_4,fvf.mth_fitness_function(var_p_dna_4),0)\
#             ]
# my_dataframe = ss.createDataFrame(data=my_data, schema=my_schema)

# output_dir = var_directory_1+'y_population'+str(var_generation)+'.csv'
# my_dataframe.write.csv(output_dir, header=True)

