
## PARTITIONS vs INDEXING
    To understand this by an analogical example :
        1)  Take a big pile of 1 billion books that you want to arrange in library
        2)  Now the entire library has to be segregated sectionized for better and fast access of any book wanted
        3)  Now each book has { book_id , book_name , book_author , book_genre } 
        4)  If we inspect above attributes of books in library in terms of granularity of distinct data,
            book_genre will have least possible distinct values compared to others followed by
            book_author , book_name , book_id in that increasing order .

    Now if you were to "PARTITION" the library into seperate sections , its meaningless to segregate library based on book_id because of two reasons .
        1)  BOOK_ID will be unique and PARTITIONING the library into billion partitions is as good as not doing at all , 
            you have to choose least possible cardinality attribute to partition by , BOOK_GENRE in this case
        2)  The customers of library wont know what they want by BOOK_ID  , in SELECT query context where clause.


## PARTITIONING 
    Types of partitioning :
        List partitioning
        Range partitioning
        Hash partitioning
        Composite partitioning
    
    Declarative partitioning vs Inheritence partitioning


## INDEX
    Local index vs global index

    Types :
        Clustered :
            In this type of INDEXING data is rearranged in an order according to the column used for indexing
        Non clustered :
            Data rearrangement will not be done , but the indexing info collected on this data will be ordered
        Heap




## Table Migratition startegies 
    Traditional
    Blue green
    logical replication


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
        
        ``` MERGE INTO target_tbl 
            USING source_tbl
            on MERGE COLS
            When matched and target_tbl.is_latest == 1 then
                update set  target_tbl.is_latest = 0 , target_tbl.end_date = source_tbl.start_date 
            When matched and target_tbl.is_latest == 0 then
                insert (target_cols) values (source_cols) 
        ```

    SCD type 3 :
        If any updated info of a CELL comes , to store that updated value we create a new column instead of adding
        them in new rows.
        SCD type 2 is better in terms of scalability than SCD type 3

    SCD type 4:
        For storing latest info NEW tables are created in this type

    SCD type 6 :
        This is mixed approach of SCD type 1 , 2 , 3 based on necessity


star and snowflake schema