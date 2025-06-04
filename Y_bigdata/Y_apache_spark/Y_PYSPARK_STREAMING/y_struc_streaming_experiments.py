#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from pyspark.sql import SparkSession
ss=SparkSession.builder.appName('app_for_struct_stream').getOrCreate()


# In[2]:


ss


# In[3]:


ss.conf.set("spark.sql.streaming.schemaInference", True)
read_stream_df =    ss.readStream.format("csv")\
                    .options(header = True,delimiter = ",", recursiveFileLookup = True )\
                    .load("file://"+os.environ['my_home_directory']+"/Documents/y_compendium/y_youtube_teaching/y_pyspark/y_datafiles/y_csv_files/")


# In[4]:


from pyspark.sql.functions import udf
@udf
def func_date_time():
    return str(datetime.now())


# In[5]:


from datetime import datetime,timedelta
transform_df = read_stream_df.withColumn("Read_time",func_date_time())


# In[6]:


from pyspark.sql.types import *
from pyspark.sql.functions import *
transform_df_change_type = transform_df.withColumn("col_sales_int_type", col("col_sales").cast(IntegerType()))\
                                        .withColumn("Read_time_type_tmstmp", col("Read_time").cast(TimestampType()))


# In[7]:


transform_df_change_type.printSchema()


# <br>
# <br>
# 
# # OUTPUT MODE = "APPEND" to "FILE" sink
# 
# <br>
# <br>

# In[ ]:


writing_df_append =    transform_df.writeStream\
                .format("csv")\
                .options(header = True,delimiter = ",")\
                .option("path", "file://"+os.environ['my_home_directory']+"/Documents/y_compendium/y_youtube_teaching/y_pyspark/y_datafiles/y_output_of_ss/")\
                .option("checkpointLocation","file://"+os.environ['my_home_directory']+"/Documents/y_compendium/y_youtube_teaching/y_pyspark/y_datafiles/y_checkpointing_location/")\
                .outputMode("append")\
                .start()
writing_df_append.awaitTermination()


# <br>
# <br>
# 
# # OUTPUT MODE = "COMPLETE" with windows function (!! NOT WORKING)
# 
# <br>
# <br>

# In[ ]:


from pyspark.sql.window import Window
from pyspark.sql import functions as F
windowSpec  = Window.partitionBy("col_company").orderBy(F.desc("col_company"))
transform_df_win = transform_df.withColumn("sum_sales_by_company", sum(col("col_sales")).over(windowSpec))


# In[ ]:


writing_df_complete =    transform_df_win.writeStream\
                .format("console")\
                .options(header = True,delimiter = ",")\
                .option("path", "file://"+os.environ['my_home_directory']+"/Documents/y_youtube/y_youtube_teaching/y_pyspark/y_datafiles/y_output_of_ss/")\
                .option("checkpointLocation","file://"+os.environ['my_home_directory']+"/Documents/y_youtube/y_youtube_teaching/y_pyspark/y_datafiles/y_checkpointing_location/")\
                .outputMode("complete")\
                .start()
writing_df_complete.awaitTermination()


# <br>
# <br>
# 
# # SINK = "CONSOLE" with aggregate function
# 
# <br>
# <br>

# In[ ]:


from pyspark.sql.types import IntegerType
from pyspark.sql.functions import *
transform_to_int_sales = transform_df.withColumn("col_sales_int_type", col("col_sales").cast(IntegerType()))
transform_df_agg = transform_to_int_sales.groupBy('col_company').sum("col_sales_int_type")


# In[ ]:


writing_df_complete =    transform_df_agg.writeStream\
                .format("console")\
                .options(header = True,delimiter = ",")\
                .option("checkpointLocation","file://"+os.environ['my_home_directory']+"/Documents/y_youtube/y_youtube_teaching/y_pyspark/y_datafiles/y_checkpointing_location/")\
                .outputMode("append")\
                .start()
writing_df_complete.awaitTermination()


# <br>
# <br>
# 
# # OPERATION   = SIMPLE SELECT    
# # SINK        = CONSOLE
# # OUTPUT MODE = APPEND , COMPLETE , UPDATE
# 
# <br>
# <br>

# In[ ]:


writing_df =    transform_df.writeStream\
                .format("console")\
                .options(header = True,delimiter = ",")\
                .option("checkpointLocation","file://"+os.environ['my_home_directory']+"/Documents/y_youtube/y_youtube_teaching/y_pyspark/y_datafiles/y_checkpointing_location/")\
                .outputMode("append")\
                .start()
writing_df.awaitTermination()


# In[ ]:


writing_df =    transform_df.writeStream\
                .format("console")\
                .options(header = True,delimiter = ",")\
                .option("checkpointLocation","file://"+os.environ['my_home_directory']+"/Documents/y_youtube/y_youtube_teaching/y_pyspark/y_datafiles/y_checkpointing_location/")\
                .outputMode("complete")\
                .start()
writing_df.awaitTermination()


# In[ ]:


writing_df =    transform_df.writeStream\
                .format("console")\
                .options(header = True,delimiter = ",")\
                .option("checkpointLocation","file://"+os.environ['my_home_directory']+"/Documents/y_youtube/y_youtube_teaching/y_pyspark/y_datafiles/y_checkpointing_location/")\
                .outputMode("update")\
                .start()
writing_df.awaitTermination()


# <br>
# <br>
# 
# # OPERATION   = AGGREGATIONS   
# # SINK        = CONSOLE
# # OUTPUT MODE = APPEND , COMPLETE , UPDATE
# 
# <br>
# <br>

# In[ ]:


transform_df_agg = transform_df_change_type.groupBy('col_company').sum("col_sales_int_type")


# In[ ]:


writing_df =    transform_df_agg.writeStream\
                .format("console")\
                .options(header = True,delimiter = ",")\
                .option("checkpointLocation","file://"+os.environ['my_home_directory']+"/Documents/y_youtube/y_youtube_teaching/y_pyspark/y_datafiles/y_checkpointing_location/")\
                .outputMode("append")\
                .start()
writing_df.awaitTermination()


# In[ ]:


writing_df =    transform_df_agg.writeStream\
                .format("console")\
                .options(header = True,delimiter = ",")\
                .option("checkpointLocation","file://"+os.environ['my_home_directory']+"/Documents/y_youtube/y_youtube_teaching/y_pyspark/y_datafiles/y_checkpointing_location/")\
                .outputMode("complete")\
                .start()
writing_df.awaitTermination()


# In[ ]:


writing_df =    transform_df_agg.writeStream\
                .format("console")\
                .options(header = True,delimiter = ",")\
                .option("checkpointLocation","file://"+os.environ['my_home_directory']+"/Documents/y_youtube/y_youtube_teaching/y_pyspark/y_datafiles/y_checkpointing_location/")\
                .outputMode("update")\
                .start()
writing_df.awaitTermination()


# <br>
# <br>
# 
# # OPERATION   = Window function  
# # SINK        = CONSOLE
# # OUTPUT MODE = APPEND , COMPLETE , UPDATE
# 
# <br>
# <br>

# In[ ]:


writing_df =    transform_df_agg.writeStream\
                .format("console")\
                .options(header = True,delimiter = ",")\
                .option("checkpointLocation","file://"+os.environ['my_home_directory']+"/Documents/y_youtube/y_youtube_teaching/y_pyspark/y_datafiles/y_checkpointing_location/")\
                .outputMode("append")\
                .start()
writing_df.awaitTermination()


# In[ ]:


transform_df_window = transform_df_change_type.\
                        groupBy(window(transform_df_change_type.Read_time_type_tmstmp,\
                                        "2 minutes",\
                                        "1 minute"\
                                        ),'col_company'\
                               ).count()


# In[ ]:


writing_df =    transform_df_window.writeStream\
                .format("console")\
                .options(header = True,delimiter = ",")\
                .option("checkpointLocation","file://"+os.environ['my_home_directory']+"/Documents/y_youtube/y_youtube_teaching/y_pyspark/y_datafiles/y_checkpointing_location/")\
                .outputMode("complete")\
                .start()
writing_df.awaitTermination()


# In[10]:


writing_df =    transform_df_window.writeStream\
                .format("console")\
                .options(header = True,delimiter = ",")\
                .option("checkpointLocation","file://"+os.environ['my_home_directory']+"/Documents/y_youtube/y_youtube_teaching/y_pyspark/y_datafiles/y_checkpointing_location/")\
                .outputMode("update")\
                .start()
writing_df.awaitTermination()


# In[ ]:




