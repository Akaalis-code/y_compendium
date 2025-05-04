## STREAMING 
    Spark streaming vs structured streaming :
        SPARK STREAMING(DSTREAM on RDD API) is the new and improved version of STRUCTURED STREAMING which includes the capabilities of data frames and sql like querying . 
        SPARK STREAMING is micro batched to simulate the STEAMING functionality
        STRUCTURED STREAMING(Which also works as micro batching until spark 2.3) is near continuous and fast -->> need to check this further
    
    Features of STRUCTURED STREAMING:
        fast, 
        scalable, 
        fault-tolerant, 
        end-to-end exactly-once stream processing 