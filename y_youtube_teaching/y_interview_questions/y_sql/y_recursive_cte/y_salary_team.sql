-------------------------------- Question -- start -----------------------------------------------------------------
Hiring Budget Analysis SQL
    Problem Description
        A company wants to hire new employees. The total budget for salaries is $50,000.
        The hiring criteria are:
            1) Keep hiring the Senior with the smallest salary until you cannot hire any more seniors.
            2) Use the remaining budget to hire the Junior with the smallest salary.
            3) Keep hiring the Junior with the smallest salary until you cannot hire any more juniors.
-------------------------------- Question -- end -----------------------------------------------------------------


-------------------------------- Data Setup -- start ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS candidates 
(
    id int,
    position VARCHAR(20) not null,
    salary int not null
);

-- Example Data
INSERT INTO candidates VALUES (20, 'junior', 10000);
INSERT INTO candidates VALUES (30, 'senior', 15000);
INSERT INTO candidates VALUES (40, 'senior', 30000);
INSERT INTO candidates VALUES (1, 'junior', 5000);
INSERT INTO candidates VALUES (2, 'junior', 7000);
INSERT INTO candidates VALUES (3, 'junior', 7000);
INSERT INTO candidates VALUES (4, 'senior', 10000);
INSERT INTO candidates VALUES (5, 'junior', 10000);
INSERT INTO candidates VALUES (6, 'senior', 20000);
INSERT INTO candidates VALUES (7, 'senior', 30000);
-------------------------------- Data Setup -- end ------------------------------------------------------------



------------------------------- Solution -- start -------------------------------------------------------------

WITH SENIOR AS 
(
    SELECT 0 as ID,'SENIOR' AS SNR_POS,0 as salary, 0 AS SNR_SAL_SUMMATION, 0 AS SNR_CNT
    UNION ALL
    SELECT 
    ID,
        UPPER(position) as SNR_POS,
        salary,
        SUM(salary) OVER(ORDER BY salary ASC, ID ASC) AS SNR_SAL_SUMMATION,
        ROW_NUMBER() OVER(ORDER BY salary ASC, ID ASC) AS SNR_CNT
    FROM candidates 
    WHERE upper(position) = 'SENIOR'
),
JUNIOR AS 
(
    SELECT 0 as ID,'JUNIOR' AS JNR_POS,0 as salary, 0 AS JNR_SAL_SUMMATION, 0 AS JNR_CNT
    UNION ALL
    SELECT 
    ID,
        UPPER(position) as JNR_POS,
        salary,
        SUM(salary) OVER(ORDER BY salary ASC, ID ASC) AS JNR_SAL_SUMMATION,
        ROW_NUMBER() OVER(ORDER BY salary ASC, ID ASC) AS JNR_CNT
    FROM candidates 
    WHERE upper(position) = 'JUNIOR'
),
COMBINATIONS AS 
(
    SELECT 
        SNR_POS,
        COALESCE(SNR_CNT, 0) AS SENIORS_CNT,
        SNR_SAL_SUMMATION,
        JNR_POS,
        COALESCE(JNR_CNT, 0) AS JUNIORS_CNT,
        JNR_SAL_SUMMATION,
        CASE 
            WHEN COALESCE(SNR_SAL_SUMMATION, 0) <= 50000 THEN SNR_CNT 
            ELSE 0 
        END AS seniors,
        CASE 
            WHEN COALESCE(SNR_SAL_SUMMATION, 0) <= 50000 
                 AND COALESCE(SNR_SAL_SUMMATION, 0) + COALESCE(JNR_SAL_SUMMATION, 0) <= 50000 
            THEN JNR_CNT 
            ELSE 0  
        END AS juniors
    FROM SENIOR SR 
    CROSS JOIN JUNIOR JR
),
final_summary AS 
(
    SELECT *, 
           ROW_NUMBER() OVER(ORDER BY seniors DESC, juniors DESC) AS RNK 
    FROM COMBINATIONS
)
SELECT juniors, seniors 
FROM final_summary 
WHERE RNK = 1;

-------------------------------------------- Solution -- end ----------------------------------------------

------------------------- Explanation bits -- start -------------------------------------------------------
-- chunk 1 
WITH SENIOR AS 
(
    SELECT 0 as ID,'SENIOR' AS SNR_POS,0 as salary, 0 AS SNR_SAL_SUMMATION, 0 AS SNR_CNT
    UNION ALL
    SELECT 
    ID,
        UPPER(position) as SNR_POS,
        salary,
        SUM(salary) OVER(ORDER BY salary ASC, ID ASC) AS SNR_SAL_SUMMATION,
        ROW_NUMBER() OVER(ORDER BY salary ASC, ID ASC) AS SNR_CNT
    FROM candidates 
    WHERE upper(position) = 'SENIOR'
),
JUNIOR AS 
(
    SELECT 0 as ID,'JUNIOR' AS JNR_POS,0 as salary, 0 AS JNR_SAL_SUMMATION, 0 AS JNR_CNT
    UNION ALL
    SELECT 
    ID,
        UPPER(position) as JNR_POS,
        salary,
        SUM(salary) OVER(ORDER BY salary ASC, ID ASC) AS JNR_SAL_SUMMATION,
        ROW_NUMBER() OVER(ORDER BY salary ASC, ID ASC) AS JNR_CNT
    FROM candidates 
    WHERE upper(position) = 'JUNIOR'
)
select * from SENIOR
union 
select * from JUNIOR


-- chunk 2

WITH SENIOR AS 
(
    SELECT 0 as ID,'SENIOR' AS SNR_POS,0 as salary, 0 AS SNR_SAL_SUMMATION, 0 AS SNR_CNT
    UNION ALL
    SELECT 
    ID,
        UPPER(position) as SNR_POS,
        salary,
        SUM(salary) OVER(ORDER BY salary ASC, ID ASC) AS SNR_SAL_SUMMATION,
        ROW_NUMBER() OVER(ORDER BY salary ASC, ID ASC) AS SNR_CNT
    FROM candidates 
    WHERE upper(position) = 'SENIOR'
),
JUNIOR AS 
(
    SELECT 0 as ID,'JUNIOR' AS JNR_POS,0 as salary, 0 AS JNR_SAL_SUMMATION, 0 AS JNR_CNT
    UNION ALL
    SELECT 
    ID,
        UPPER(position) as JNR_POS,
        salary,
        SUM(salary) OVER(ORDER BY salary ASC, ID ASC) AS JNR_SAL_SUMMATION,
        ROW_NUMBER() OVER(ORDER BY salary ASC, ID ASC) AS JNR_CNT
    FROM candidates 
    WHERE upper(position) = 'JUNIOR'
),
COMBINATIONS AS 
(
    SELECT 
        SNR_POS,
        COALESCE(SNR_CNT, 0) AS SENIORS_CNT,
        SNR_SAL_SUMMATION,
        JNR_POS,
        COALESCE(JNR_CNT, 0) AS JUNIORS_CNT,
        JNR_SAL_SUMMATION,
        CASE 
            WHEN COALESCE(SNR_SAL_SUMMATION, 0) <= 50000 THEN SNR_CNT 
            ELSE 0 
        END AS seniors,
        CASE 
            WHEN COALESCE(SNR_SAL_SUMMATION, 0) <= 50000 
                 AND COALESCE(SNR_SAL_SUMMATION, 0) + COALESCE(JNR_SAL_SUMMATION, 0) <= 50000 
            THEN JNR_CNT 
            ELSE 0  
        END AS juniors
    FROM SENIOR SR 
    CROSS JOIN JUNIOR JR
)
select * from COMBINATIONS 
order by JNR_SAL_SUMMATION asc , SNR_SAL_SUMMATION asc

-- Chunk final

WITH SENIOR AS 
(
    SELECT 0 as ID,'SENIOR' AS SNR_POS,0 as salary, 0 AS SNR_SAL_SUMMATION, 0 AS SNR_CNT
    UNION ALL
    SELECT 
    ID,
        UPPER(position) as SNR_POS,
        salary,
        SUM(salary) OVER(ORDER BY salary ASC, ID ASC) AS SNR_SAL_SUMMATION,
        ROW_NUMBER() OVER(ORDER BY salary ASC, ID ASC) AS SNR_CNT
    FROM candidates 
    WHERE upper(position) = 'SENIOR'
),
JUNIOR AS 
(
    SELECT 0 as ID,'JUNIOR' AS JNR_POS,0 as salary, 0 AS JNR_SAL_SUMMATION, 0 AS JNR_CNT
    UNION ALL
    SELECT 
    ID,
        UPPER(position) as JNR_POS,
        salary,
        SUM(salary) OVER(ORDER BY salary ASC, ID ASC) AS JNR_SAL_SUMMATION,
        ROW_NUMBER() OVER(ORDER BY salary ASC, ID ASC) AS JNR_CNT
    FROM candidates 
    WHERE upper(position) = 'JUNIOR'
),
COMBINATIONS AS 
(
    SELECT 
        SNR_POS,
        COALESCE(SNR_CNT, 0) AS SENIORS_CNT,
        SNR_SAL_SUMMATION,
        JNR_POS,
        COALESCE(JNR_CNT, 0) AS JUNIORS_CNT,
        JNR_SAL_SUMMATION,
        CASE 
            WHEN COALESCE(SNR_SAL_SUMMATION, 0) <= 50000 THEN SNR_CNT 
            ELSE 0 
        END AS seniors,
        CASE 
            WHEN COALESCE(SNR_SAL_SUMMATION, 0) <= 50000 
                 AND COALESCE(SNR_SAL_SUMMATION, 0) + COALESCE(JNR_SAL_SUMMATION, 0) <= 50000 
            THEN JNR_CNT 
            ELSE 0  
        END AS juniors
    FROM SENIOR SR 
    CROSS JOIN JUNIOR JR
),
final_summary AS 
(
    SELECT *, 
           ROW_NUMBER() OVER(ORDER BY seniors DESC, juniors DESC) AS RNK 
    FROM COMBINATIONS
)
SELECT juniors, seniors ,*
FROM final_summary 
------------------------- Explanation bits -- End -------------------------------------------------------