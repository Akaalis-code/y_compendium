1.For the input data,Using pyspark calculate the total hours employee was inside office status.
employee_id|log_time|Status
11114|1919–01–01 08:30:00| I
11114|1919–01–01 10:30:00| O
11114|1919–01–01 11:30:00| I
11114|1919–01–01 15:30:00| O
11115|1919–01–01 09:30:00| I
11115|1919–01–01 17:30:00| O

ANSWER : Pseudo code 
Employee_df = Details given above

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














2.From the given data set using pyspark find the manager and their employees.

empl_id|name|mngr_id
4529| Nancy| 4125
4238| John| 4329
4329| Martina| 4125
4009| Klaus| 4329
4125| Mafalda| NULL
4500| Jakub| 4529
4118| Moira| 4952
4012| Jon| 4952
4952| Sandra| 4529
4444| Seamus| 4329


ANSWER : PSEUDO CODE

Note : The given tables itself is already an answer to itself , its just select manage name first and employee name second by filtering manager id is not null

table_df.filter(mngr_id is not NULL).select(‘mngr_id’ , ‘empl_id’)





















3.Write pyspark code to return the shipped and delivered rate for each order. Return order_id, shipped percentage, and delivered percentage.

Columns : Order_Id,Order_Status,Order_Date

data = [
 (15, "Shipped", "2024-04-01"),
 (15, "Shipped", "2024-04-02"),
 (24, "Delivered", "2024-04-01"),
 (24, "Delivered", "2024-04-02"),
 (24, "Shipped", "2024-04-03"),
 (39, "Shipped", "2024-04-01"),
 (39, "Delivered", "2024-04-02"),
 (39, "Delivered", "2024-04-03")

ANSWER : PSEUDO CODE 

Temp_df = TABLE_DF.groupby(‘Order_Id’)\
.agg(sum(if ‘Order_Status’ == ‘shipped’ then 1 else 0).alias(‘count_shipped’)\
        ,sum(if ‘Order_Status’ == delivered then 1 else 0).alias(‘count_delivered’)\
       )

Temp_df.withColumn(‘shipped_percentage’,’ (‘count_shipped’/(‘count_shipped’ +‘count_delivered’)*100)
.withColumn(‘delivered_percentage’,’ (‘count_delivered’/(‘count_shipped’ +‘count_delivered’)*100).show()

















4.Remove the extra characters other than characters ,digits and get each word and its count using pyspark.

Input —
data = [
“Hello All! This is the pyspark code.”,
“Spark is best, isn’t it?”,
“Get the benefit's by using the pyspark.”
“List out the optimization's that are used in spark 0 55.”
]

ANSWER : 
I would have to refer REGEXP and solve this question 






























5.Using sql select the projects with the highest budget per employee ratio(calculate) from related tables project_table and empl_table.

project_table:
project_id,
budget,
Manager_name

empl_table:
employee_id,
Employee_name

ANSWER : 

There is no connection between Project table and employee table in the given question ,
Assuming manager_id is employee_id column , I am writing below awnser

With temp_tbl as
(
Select project_id , budget/cnt as Ratio
from
(
Select project_id , 
budget , 
count(et.employee_id) over(partition by project_id) as cnt
From project_table as pt Inner join empl_table as et
On pt.employee_id = et.employee_id
)
)
Select Project_id,Ratio
From temp_tbl
Where Ratio in (Select max(ration) as max_value
From temp_tbl
)









6.Using both Sql and pyspark, Handle the data and get the two columns in unique format by converting the currency amount into INR.
columns = ['date', 'amount']

data = [
 ('2024-02-01', '$100.50'),
 ('Feb 15, 2024', '€169.75'),
 ('03/20/24', '£150.20'),
 ('2024-05-05', '¥300.00')
]


ANSWER : 
I will have to refer some documentation to get an idea on this.






