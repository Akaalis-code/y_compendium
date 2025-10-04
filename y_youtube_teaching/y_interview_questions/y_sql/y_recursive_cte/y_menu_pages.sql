-- QUESTION :

We have an INPUT TABLE in which there are list of page numbers and the pages title ,
The title can be either "MAIN_DISH" or "ADDITIVES" .
Only EVEN pages will contain "MAIN_DISH" titles and only ODD pages contains "ADDITIVES",
The missing pages which doesnt have titles indicate that the recipie of previous page extended 
into those missing pages .

We need output like given below .
Three columns which should contain 
    Only even page numbers in one column , 
    MAIN_DISH titles in this column , if missing leave it as Na
    ADDITIVES columns should consist of the titles in the odd column

-- INPUT TABLE :
+-------------+----------------------+
| PAGE_NUMBER | RECIPIE_TITLE        |
+-------------+----------------------+
|           0 | Spicy Tomato Soup    |
|           2 | Garlic Butter Shrimp |
|           3 | onions and tomatos   |
|           4 | Paneer Tikka         |
|           8 | Chicken Curry        |
|           9 | ROTI                 |
|          12 | Aloo Paratha         |
|          13 | SAUCE                |
|          14 | Chai Latte           |
+-------------+----------------------+

-- EXPECTED OUTPUT :
+-------------+----------------------+----------------------+
| PAGE_NUMBER | MAIN_DISH            |       ADDITIVES      |
+-------------+----------------------+----------------------+
|           0 | Spicy Tomato Soup    |                      |
|           2 | Garlic Butter Shrimp | onions and tomatos   |
|           4 | Paneer Tikka         |                      |
|           6 |                      |                      |
|           8 | Chicken Curry        | ROTI                 |
|          10 |                      |                      |
|          12 | Aloo Paratha         | SAUCE                |
|          14 | Chai Latte           |                      |
+-------------+----------------------+----------------------+






---------------- SETUP -- START ----------------------------------------

CREATE TABLE TBL_MENU 
(
    PAGE_NUMBER INT,
    RECIPIE_TITLE VARCHAR(255)
);


INSERT INTO TBL_MENU (PAGE_NUMBER, RECIPIE_TITLE)
VALUES
    (0, 'Spicy Tomato Soup'),
    (2, 'Garlic Butter Shrimp'),
    (3, 'onions and tomatos'),
    (4, 'Paneer Tikka'),
    (8, 'Chicken Curry'),
    (9, 'ROTI'),
    (12, 'Aloo Paratha'),
    (13, 'SAUCE'),
    (14, 'Chai Latte');

---------------- SETUP -- END ----------------------------------------

---------------- FINAL SOLUTION -- START ----------------------------------------
    WITH RECURSIVE tbl_pages as
    (
        select 0 as temp_nums
            union
        select temp_nums+1 as temp_nums
        from tbl_pages
        where temp_nums < (select max(PAGE_NUMBER) from TBL_MENU)
    ),
    EVEN_PAGE_TITLES as
    (
        select *
        from      tbl_pages as tp
        left join TBL_MENU  as tm 
          on tp.temp_nums = tm.PAGE_NUMBER
        where tp.temp_nums%2 = 0 
    ),
    ODD_PAGE_TITLES as
    (
        select *
        from      tbl_pages as tp
        left join TBL_MENU  as tm 
          on tp.temp_nums = tm.PAGE_NUMBER
        where tp.temp_nums%2 = 1  
    )
    select EPT.temp_nums as PAGES ,
           EPT.RECIPIE_TITLE as MAIN_DISH,
           OPT.RECIPIE_TITLE as ADDITIVES
    from        EVEN_PAGE_TITLES as EPT 
    LEFT JOIN  ODD_PAGE_TITLES  as OPT
      on        (EPT.PAGE_NUMBER+1) = OPT.PAGE_NUMBER
---------------- FINAL SOLUTION -- END ----------------------------------------

---------------- EXPLANATION CHUNKS -- START ----------------------------------------

-- CHUNK 1
    -- ANALOGY from C LANGUAGE FOR loop 
    -- for (i=0 ; i<15 ; i++) :
    WITH RECURSIVE tbl_pages as
    (
        select 0 as temp_nums
            union
        select temp_nums+1 as temp_nums
        from tbl_pages
        where temp_nums < (select max(PAGE_NUMBER) from TBL_MENU)
    )
    select * from tbl_pages

-- CHUNK 2 
    WITH RECURSIVE tbl_pages as
    (
        select 0 as temp_nums
            union
        select temp_nums+1 as temp_nums
        from tbl_pages
        where temp_nums < (select max(PAGE_NUMBER) from TBL_MENU)
    ),
    EVEN_PAGE_TITLES as
    (
        select *
        from      tbl_pages as tp
        left join TBL_MENU  as tm 
          on tp.temp_nums = tm.PAGE_NUMBER
        where tp.temp_nums%2 = 0 
    ),
    ODD_PAGE_TITLES as
    (
        select *
        from      tbl_pages as tp
        left join TBL_MENU  as tm 
          on tp.temp_nums = tm.PAGE_NUMBER
        where tp.temp_nums%2 = 1  
    )
    SELECT * FROM EVEN_PAGE_TITLES


-- CHUNK FINAL
    WITH RECURSIVE tbl_pages as
    (
        select 0 as temp_nums
            union
        select temp_nums+1 as temp_nums
        from tbl_pages
        where temp_nums < (select max(PAGE_NUMBER) from TBL_MENU)
    ),
    EVEN_PAGE_TITLES as
    (
        select *
        from      tbl_pages as tp
        left join TBL_MENU  as tm 
          on tp.temp_nums = tm.PAGE_NUMBER
        where tp.temp_nums%2 = 0 
    ),
    ODD_PAGE_TITLES as
    (
        select *
        from      tbl_pages as tp
        left join TBL_MENU  as tm 
          on tp.temp_nums = tm.PAGE_NUMBER
        where tp.temp_nums%2 = 1  
    )
    select EPT.temp_nums as PAGES ,
           EPT.RECIPIE_TITLE as MAIN_DISH,
           OPT.RECIPIE_TITLE as ADDITIVES
    from        EVEN_PAGE_TITLES as EPT 
    LEFT JOIN  ODD_PAGE_TITLES  as OPT
      on        (EPT.PAGE_NUMBER+1) = OPT.PAGE_NUMBER
        
---------------- EXPLANATION CHUNKS  -- END ----------------------------------------



