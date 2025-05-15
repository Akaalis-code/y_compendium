from pyspark.sql import SparkSession
ss=SparkSession.builder.appName('labcorp_exam').getOrCreate()
Employee_df = ss.createDataFrame\
(\
    [\
        (11114 , '1919–01–01 08:30:00' , 'I' ),\
        (11114 , '1919–01–01 10:30:00' , 'O' ),\
        (11114 , '1919–01–01 11:30:00' , 'I' ),\
        (11114 , '1919–01–01 15:30:00' , 'O' ),\
        (11115 , '1919–01–01 09:30:00' , 'I' ),\
        (11115 , '1919–01–01 17:30:00' , 'O' )\
    ]  ,\
    ('employee_id' , 'log_time' , 'Status')\
)

from pyspark.sql.window import Window
from pyspark.sql.functions import *
from pyspark.sql.functions import lag
windowSpec  = Window.partitionBy(Employee_df["employee_id"]).orderBy(Employee_df["log_time"].asc())
Employee_df_temp =  Employee_df.\
                    withColumn( "temp_substraction_of_time",\
                                to_timestamp(Employee_df["log_time"])-to_timestamp(
                                                                                        lag(Employee_df["log_time"],
                                                                                        1,
                                                                                        to_timestamp('0001–01–01 08:30:00')
                                                                                        ).over(windowSpec)
                                                                                    )\
                                ).filter(Employee_df["Status"] = 'O')
FINAL_DF = Employee_df_temp.withColumn  (
                                            "SUM_OF_TIMES" ,
                                            sum(Employee_df_temp["temp_substraction_of_time"]).over(windowSpec)
                                        )

FINAL_DF.select('employee_id' , 'SUM_OF_TIMES').show()