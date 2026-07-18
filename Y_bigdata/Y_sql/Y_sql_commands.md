
# Most important execution order in SQL statements for compiler 

Execution Order :
    FROM / JOIN
    WHERE
    GROUP BY
    HAVING
    SELECT
    ORDER BY
    LIMIT




### HAVING clause example :

    SELECT 
            department_name, 
            SUM(salary_offered) AS total_budget
    FROM    HiringRequests
    WHERE   employment_type = 'Permanent'-- Filter raw rows first (cheaper for the engine)
    GROUP BY department_name
    HAVING SUM(salary_offered) > 500000; -- Cannot use "total_budget" column in select yet as SELECT comes after HAVING clause


# Window Function 
Reference : https://www.javatpoint.com/mysql-window-functions

SYNATX : 
    SELECT  expression 1, 
            expression 2, 
            agg_func() OVER (  
                                [partition_defintion]             -- No commas after PARTITION BY and ORDER BY and ROWS BETWEEN
                                [order_definition]  
                                [frame_definition]  
                            ) 
    FROM table

    [partition_defintion] :
        Add all the comma seperate columns that you want to work group together for agg_func()
        EXAMPLE : PARTITION BY col1,col2,....coln
    
    [order_definition] :
        Specify columns that you want t order by the subset mentioned in [partition_defintion]
        Example : ORDER BY col1,col2,....coln ASC|DESC
    
    [frame_definition] :
        -   This frame definition helps you to have a subset inside the set defined in [partition_defintion]
            with the order defined in [order_definition]
        -   Default is "ROWS BETWEEN UNBOUNDED PRECEDING and CURRENT ROW"
        -   Examples : agg_func() OVER(PARTITION BY col1  ORDER BY col2 ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
            Possible values :   1) UNBOUNDED PRECEDING
                                2) UNBOUNDED FOLLOWING
                                3) CURRENT ROW
                                4) N PRECEDING
                                5) N FOLLOWING


    - THE WINDOWS FUNCTIONS :

        ROW_NUMBER()    - 1,2,3,4....
        RANK()          - 1,2,2,4....
        DENSE_RANK()    - 1,2,2,3....
        NTILE(n)        - Based on partion by and order by , it divides each partition into "n" equal groups
                          after analyzing total rows in that partition or on whole if no partition is given.


        LAG(col_name , number_of_rows_to_LAG_by , Default_values_if_found_nothing)           
        LEAD(col_name , number_of_rows_to_LAG_by , Default_values_if_found_nothing)
        FIRST_VALUE(col_name)   - careful with its default [frame_definition] , its "ROWS BETWEEN UNBOUNDED PRECEDING and CURRENT ROW"
        LAST_VALUE(col_name)    - careful with its default [frame_definition] , its "ROWS BETWEEN UNBOUNDED PRECEDING and CURRENT ROW"
        NTH_VALUE(col, n)       - careful with its default [frame_definition] , its "ROWS BETWEEN UNBOUNDED PRECEDING and CURRENT ROW"
################### Window Function ## End ######################################################################





Lead() and Lag() functions in window functions
WINDOW functions have types like :
    TUMBLING window : when the current window doesnt intersect with previous or next window
    SLIDING window  : when the current window intersect with previous or next window

