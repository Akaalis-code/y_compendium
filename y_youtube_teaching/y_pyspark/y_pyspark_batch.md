# PLAN FOR THIS VIDEO
    1- Intro of SPARK
    2- Pyspark setup on local machine
    3- Coding topics in pyspark
        1- Read data from CSV 
        2- Show dataframes 
        3- select only few columns
        4- Alias column names
        5- Filter Columns 
        6- Aggregate Functions
        7- Joins of dataframes
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


# Problem statment 

<br>

<img src="./y_resources/y_spark_analogy.svg" alt="Spark analogy" width="1000"/>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


# INTRO of spark 

<br>

<img src="./y_resources/y_computers.svg" alt="Pool of computers" width="1000"/>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

### SOURCE = SPARK OFFICIAL DOCUMENTATION
<img src="./y_resources/y_spark_architechture.png" alt="Spark architechture" width="1000" title="From official documentation"/>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

###########################################################################################################################
# Responsibilities of each component in above diagram
#### SOURCE = https://techgurudehradun.in/blog/?p=77

    Driver program :
        1) Starts spark session
        2) Divides the work into tasks
        3) Talk to cluster manager to get info about worker
    Cluster Manager :
        1) Maintain information about the worker nodes
        2) Submit that info to Driver program
    Worker Nodes (or executor programs(EP)):
        1) Each work node may contain one or more execution programs(EP) 
        2) Each execution program will run in JVM s with the computing resources given to it
        3) Run the Taks given to it and submit it to driver program

###########################################################################################################################
# Pyspark setup For Local mode (i.e. single node cluster) ## Start 
###########################################################################################################################
1)  Inside vitualbox , a dedicated ubuntu OS is setup for pyspark teaching

2)  Ubuntu OS already comes with a python , OS doesnt allow PIP to install any libraries into this python ENV
    may be to keep OS python safe from external changes as OS might be dependent on this python.

3)  Use either "VirtualEnvironment" or "venv" or "pipenv" which ever is available for you or 
    can be installed from "apt" 

4)  I used venv , below is the setup :

        > sudo apt install python3.12-venv          ## To install venv into your system
        > python3 -m venv my_env                    ## Create an vitual env 
        > cd my_env/bin/                            ## Your activate and deactivate files for venv are present here
        > source activate                           ## Activate the venv "my_env" 
        (my_env) > deactivate                       ## This a shell function inside activate file , to comeout of venv


5)  We need JAVA installed SYSTEM wide for pyspark to work . open new terminal window and check as below

        > JAVA -version                             ## To check if JAVA already exists or not 
        > sudo apt install openjdk-21-jre-headless  ## If not there already choose a appropriate version and install as mentioned


6)  Next setup "JAVA_HOME" environment variable in ".bashrc" file , 
    You can find java installed location by below command

        > which java

7)  After finding the java installed path add JAVA home location to PATH variable , follow as below

        >nano ~/.bashrc                                 #nano is command line editor , ~ symbol takes you to home folder

        ##Add Below two lines in .bashrc file
        JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64/
        PATH=$PATH:$JAVA_HOME/bin

8)  Now Install PYSPARK library in your python virtual environment

        >pip install pyspark

9)  At this point you can run "pyspark" command and run spark code in pyspark shell line by line

10) For better visualization I am going to install "JUPYTER" notebooks 

        (my_venv) > pip install jupyter             ## Install JUPYTER inside your my_venv using pip
        (my_venv) > jupyter notebook                ## To start Jupyter Notebook server , open "http://localhost:8888/" in any browser
        (my_venv) > ctrl + c                        ## To stop Jupyter Notebook server
        
###########################################################################################################################
# Pyspark setup ## End 
###########################################################################################################################

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

###########################################################################################################################
## CSV file read ##
###########################################################################################################################

- y_sales folder
    - 2023 folder
        - mo=11.txt
        - mo=12.txt
    - 2024 folder
        - mo=01.txt
        - mo=02.txt


-->>Code

    from pyspark.sql import SparkSession
    ss=SparkSession.builder.appName('youtube_teaching').getOrCreate()


    from pyspark.sql.types import *
    my_schema = StructType([
                                StructField("col_company", StringType()) ,
                                StructField("col_product", StringType()) ,
                                StructField("col_number_of_items", IntegerType()) ,
                                StructField("col_sales", IntegerType()),
                            ])


    df_my_sales_data =  ss.read.options(header=True , recursiveFileLookup = True )\
                        .csv('/home/yvm/Documents/y_youtube/y_youtube_teaching/y_pyspark/y_datafiles/y_csv_files/*')


    df_my_sales_data.show()


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

###########################################################################################################################
## Select only few columns ##
###########################################################################################################################

                                                    select  col_company ,
                                                            col_sales
                                                    from df_my_sales_data


-->>Code

    df_my_sales_data.select(
                                'col_company' , 
                                'col_sales'
                            ).show()

    df_my_sales_data.select(
                                df_my_sales_data['col_company'] , 
                                df_my_sales_data['col_sales']
                            ).show()

    df_my_sales_data.select(
                                df_my_sales_data.col_company , 
                                df_my_sales_data.col_sales
                            ).show()


    from pyspark.sql.functions import col
    df_my_sales_data.select(
                                col('col_company'),
                                col('col_sales')
                            ).show()

    df_my_sales_data.select(
                                df_my_sales_data[1] , 
                                df_my_sales_data[2]
                            ).show()


    df_my_sales_data.select(
                                df_my_sales_data.columns[0:3]
                            ).show()


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

###########################################################################################################################
## alias columns  ##
###########################################################################################################################
 
                                                select  col_company as your_alias_name,
                                                        col_sales
                                                from df_my_sales_data


-->> PYSPARK Code

    df_my_sales_data.select(
                                df_my_sales_data['col_company'].alias('your_alias_name'), 
                                df_my_sales_data['col_sales']
                            ).show()

    df_my_sales_data.select(
                                df_my_sales_data.col_company.alias('your_alias_name') , 
                                df_my_sales_data.col_sales
                            ).show()


    from pyspark.sql.functions import col
    df_my_sales_data.select(
                                col('col_company').alias('your_alias_name'),
                                col('col_sales')
                            ).show()

    df_my_sales_data.select(
                                df_my_sales_data[1].alias('your_alias_name') , 
                                df_my_sales_data[2]
                            ).show()


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

###########################################################################################################################
##  Where clause  ##
###########################################################################################################################
 
                                                select  *
                                                from df_my_sales_data
                                                where col_company = 'C1'
                                                  and (col_sales > 100) or ( col_number_of_items > 10 )



-->> PYSPARK Code

    df_my_sales_data.where( col("col_company") == 'C1' ).show()


    df_my_sales_data.where( 
                                ( col("col_company") == 'C1' ) &
                                ( ( col("col_sales") > 100 ) | ( col("col_number_of_items") > 10 ) )
                            ).show()



    df_my_sales_data.where( 
                                ( col("col_company") == 'C1' ) &
                                ( ( col("col_sales") > 100 ) | ( col("col_number_of_items") > 10 ) )
                            ).show()


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

###########################################################################################################################
##  Filter clause  ##
###########################################################################################################################
 
                                                select  *
                                                from df_my_sales_data
                                                where col_company = 'C1'
                                                  and (col_sales > 100) or ( col_number_of_items > 10 )



-->> PYSPARK Code

    df_my_sales_data.filter( col("col_company") == 'C1' ).show()


    df_my_sales_data.filter( 
                                ( col("col_company") == 'C1' ) &
                                ( ( col("col_sales") > 100 ) | ( col("col_number_of_items") > 10 ) )
                            ).show()



    df_my_sales_data.filter( 
                                ( col("col_company") == 'C1' ) &
                                ( ( col("col_sales") > 100 ) | ( col("col_number_of_items") > 10 ) )
                            ).show()


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

###########################################################################################################################
##  AGGREGATE FUNCTIONS  ##
###########################################################################################################################
 
                                                select  col_company , 
                                                        AGG(col_sales) , 
                                                        AGG(col_number_of_items)
                                                from df_my_sales_data
                                                group by col_company
                                                order by col_company ASC

AGG()  ---->>>>  sum(), avg(), max(), min(), and count()



-->> PYSPARK Code

    df_my_sales_data.groupBy(col("col_company")).sum(col("col_sales")).show()


    from pyspark.sql.functions import col,asc,desc
    df_my_sales_data.groupBy("col_company").\
                    sum("col_sales","col_number_of_items").\
                    orderBy(col("col_company").desc()).\
                    show()


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

###########################################################################################################################
##  JOINS FUNCTIONS  ##
###########################################################################################################################
 
                                                select  *
                                                from df_my_sales_data YOUR_JOIN df_test
                                                  on col_company = tst_company and
                                                     col_product = tst_product


-->> PYSPARK Code

    ####### creating df_test as another dataframe to use in join
        my_schema = StructType([
                                    StructField("tst_company", StringType()) ,
                                    StructField("tst_product", StringType()) ,
                                    StructField("tst_number_of_items", IntegerType()) ,
                                    StructField("tst_sales", IntegerType()),
                                ])
        df_test = ss.createDataFrame( [('C1','P2',57,23424),('C20','P2',80,5000)]  ,  my_schema)
        df_test.show()



    df_my_sales_data.join(  df_test ,\
                            (
                                (col("col_company") == col("tst_company")) & \
                                (col("col_product") == col("tst_product"))\
                            ),\
                            "inner"
                        )\
    .show()




    df_my_sales_data.join(  df_test ,\
                            (
                                (col("col_company") == col("tst_company")) & \
                                (col("col_product") == col("tst_product"))\
                            ),\
                            "full"
                        )\
    .show()



    from pyspark.sql.functions import lit
    df_my_sales_data.join(  df_test ,\
                            (lit(1)==lit(1)),\
                            "cross"
                        )\
    .show()


