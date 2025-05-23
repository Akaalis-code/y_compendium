# Structured streaming :

    Problem statement :-
        While spark sql is there to process BATCH(data size is bound and expected to stay that way) data ,
        There is a need of technology which is capable of working with a "UNBOUND CONTINOUSLY GROWING"
        data sources , in short that kind of data is called STREAMING data.
        That is where STRUCTURED STREAMING comes into picture
    
    How is this different from "SPARK STREAMING" :-
        STRUCTURED STREAMING(Uses dataframe and datasets API s) is advanced version of SPARK STREAMING(Dstream API)
        STRUCTURED STREAMING has been added with many advanced features compared to SPARK STREAMING
        Those details we will see below



# Sources and Sinks

    Sources can be = File source ,Socket Source ,Rate Source ,Rate Per Micro-Batch Source(format:rate-micro-batch) ,Kafka Source

    Sinks are based on the output modes , mentioned as below :

        | SINK TYPE         | OUTPUT MODE              |
        |:-----------------:|:------------------------:|
        | File sink         | Append                   |
        | Memory Sink       | Append, Complete         |
        | KAFKA Sink        | Append, Update, Complete |
        | Console Sink      | Append, Update, Complete |
        | Foreach Sink      | Append, Update, Complete |
        | ForeachBatch Sink | Append, Update, Complete |


# SCHEMA 

    For structured streaming in every tutorial or documentation , info is like SCHEMA needs to be explicitly specified  
    But when I tried , I set config like "spark.sql.streaming.schemaInference = True" and did not give any schema ,  
    it worked fine.

    New test reveal : if the source has zero files when reader is started , it indeed is giving 
                        "unable to infer schema" error message.

                        But if the source already has any data while the reader has started,
                        it is infereing schema succesfully ,with below config set ofcourse

    Example :
        ss.conf.set("spark.sql.streaming.schemaInference", True)
        read_stream_df = ss.readStream.format("csv")\
                        .options(header = True,delimiter = ",", recursiveFileLookup = True )\
                        .load(path)


# STREAMING options or config :

    “maxFilesPerTrigger”


CHECK POINTING :
    Its a folder location where structured streaming keeps its meta data on which files from SOURCE have been read
    and written succesfully into the SINK .

    We generally will give the checkpointing location through STREAMWRITER object , like below .

WRITE AHEAD LOGS
WATERMARKING :
    (subject to change) -->> output modes are only Append and Update , when complete mode is there Watermarking is Infinite time threshold 

    Think of the pupose of watermark as memory cleaner which holds STATE store and 
    any window whose end time is outside {MAX_EVEN_TIME - THRESHOLD} will be wiped out from memory's STATE STORE which holds
    this aggregated intermediate data 


# Aggregations and Window functions check for different output modes :

        | OPERATION         | OUTPUT MODE              | SINK   | Working or not |
        |:-----------------:|:------------------------:|:------:|:--------------:|
        |          | Append                   |
        |       | Append, Complete         |
        |         | Append, Update, Complete |
        |       | Append, Update, Complete |
        |       | Append, Update, Complete |
        |  | Append, Update, Complete |



# WINDOWS operation :

    Windows operation syntax and functionality is almost same with usual SQl Windows but with slight added features
    like Watermark functionality to provide a thresholld value on late arrival of data and etc .

    Synatx is as follows : (may be subject to change)

        window(timeColumn: Column,          -->> use a time related column in your dataframe
                windowDuration: String,     -->> mention that duration like this "10 minutes"
                slideDuration: String,      -->> mention that duration like this "5 minutes"
                startTime: String           -->> mention that duration like this "5 minutes"
                )
        
        dataframe.groupBy   (  <Windowsobject derved from above>,
                                <your dataframe column>,
                            ).agg()
    

    Types of Windows operation :
        Rolling Window 
        Sliding window
        session window 