## SCD (Slowly changing dimensions )
    SCD type 0 :
        Table that has data which never NEEDS a change
        Examples:
            Date of birth
            An employee’s start date with a company
    
        ``` INSERT INTO target_tbl values(....) ```

    SCD type 1 :
        Table whose data just needs to be always latest and no worrying about history retaining or change tracking
        Examples :
            Current salary 
            Current employee department
        
        ``` UPDATE target_tbl set column_name="new_value" ```

    SCD type 2 :
        Its extension of SCD type 1 in a way where when a latest data comes , outdated data will be retained and updated 
        data will be added as a new row.
        Examples :
            All SCD type 1 examples come under here with extra necessity of retaining old record

    SCD type 3 :
        If any updated info of a CELL comes , to store that updated value we create a new column instead of adding
        them in new rows.
        SCD type 2 is better in terms of scalability than SCD type 3

    SCD type 4:
        For storing latest info NEW tables are created in this type

    SCD type 6 :
        This is mixed approach of SCD type 1 , 2 , 3 based on necessity


star and snowflake schema

Snowflake snowpipe = COPY command

Snowflake streams = 

Snowflake time travel = 