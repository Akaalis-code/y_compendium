-------------------------------- Question -- start -----------------------------------------------------------------
Hiring Budget Analysis SQL
    Problem Description
        A company wants to hire new employees. The total budget for salaries is $50,000.
        The hiring criteria are:
            1)  Keep hiring the higher level employees with lowest salaries until you cannot hire them with remaining budget.
            2)  Use the remaining budget to hire the next level employees with lowest salaries until you cannot hire them 
                with remaining budget.
            3)  Keep repeating the process with next level employees  and so on until either your budget becomes zero or 
                there arent any level employees that you can hire
-------------------------------- Question -- end -----------------------------------------------------------------


-------------------------------- Data Setup -- start ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS candidates 
(
    id int,
    position VARCHAR(20) not null,
    level int not null,
    salary int not null
);


INSERT INTO candidates (id, position, level, salary) VALUES 
(1, 'junior', 2, 2000),
(2, 'junior', 2, 2000),
(3, 'junior', 2, 7000),
(4, 'senior', 3, 10000),
(5, 'junior', 2, 10000),
(6, 'senior', 3, 20000),
(7, 'senior', 3, 20000),
(8, 'junior', 2, 10000),
(9, 'senior', 3, 15000),
(10, 'senior', 3, 30000);
-- (11, 'Intern', 1, 500),
-- (12, 'Intern', 1, 200),
-- (13, 'Intern', 1, 800),
-- (14, 'Super senior', 4, 20000),
-- (15, 'Super senior', 4, 50000),
-- (16, 'Super senior', 4, 60000);


select * 
from candidates 
order by level DESC , salary ASC;


-------------------------------- Data Setup -- end ------------------------------------------------------------



-------------------------------Bad  Solution -- start -------------------------------------------------------------

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

-------------------------------------------- Bad Solution  -- end ----------------------------------------------

------------------------- More dynamic solution -- start -------------------------------------------------------
with recursive Rolling_sum_data as 
(
 SELECT
        id,
        position,
        salary,
        level,
        sum(salary) over (
                            partition by level
                              order by level desc ,salary asc , id asc
                              rows between unbounded preceding and current row
                          ) as running_expenses,
        Row_number() over (order by level desc ,salary asc , id asc) as intended_order
    FROM candidates 

),
expense_tracking_data as 
(
  select id,
        position,
        salary,
        level,
        running_expenses,
        intended_order,
        50000-running_expenses as remaining_amt,
        case 
            when 50000-running_expenses>=0 then 'Hired'
            else 'Not possible to hire'
        end as hire_or_no,
        1 as cnt
  from Rolling_sum_data
  where intended_order = 1
  
  union 
  
  select rsd.id,
        rsd.position,
        rsd.salary,
        rsd.level,
        rsd.running_expenses,
        rsd.intended_order,
        case 
            when etd.remaining_amt-rsd.salary <0 then etd.remaining_amt
             else etd.remaining_amt-rsd.salary
        end as remaining_amt,
        case 
            when etd.remaining_amt-rsd.salary >=0 then 'Hired'
            else 'Not possible to hire'
        end as hire_or_no,
        etd.cnt+1
  from Rolling_sum_data as rsd
  inner join expense_tracking_data as etd on rsd.intended_order = etd.cnt+1
)
select count(id),position 
from expense_tracking_data
where hire_or_no = 'Hired'
group by position
------------------------- More dynamic solution  -- End -------------------------------------------------------


------------------------- Explanation  chunks-- Start -------------------------------------------------------

with recursive Buy_order_of_employees as 
(
SELECT
        id,
        position,
        salary,
        level,
        Row_number() over (order by level desc ,salary asc , id asc) as intended_order_to_buy
    FROM candidates 

),
expense_tracking_data as 
(
  select id,                                    id as iid,
        position,                               position as ip,
        level,                                  level as il,
        intended_order_to_buy,                  intended_order_to_buy as iiotb,
        salary,                                 salary as isa,
        50000-salary as budget_remaining_amt,
        case 
            when 50000-salary>=0 then 'Hired'
            else 'Not possible to hire'
        end as hire_or_no,
        1 as counter
  from Buy_order_of_employees
  where intended_order_to_buy = 1
  
  union 
  
  select  boe.id  ,                             etd.id  , 
          boe.position  ,                       etd.position,
          boe.level,                            etd.level,
          boe.intended_order_to_buy,            etd.intended_order_to_buy,
          boe.salary  ,                         etd.salary,
          case 
              when  etd.budget_remaining_amt-boe.salary <0 then etd.budget_remaining_amt
              else  etd.budget_remaining_amt-boe.salary
          end as budget_remaining_amt,
          case 
              when etd.budget_remaining_amt-boe.salary >=0 then 'Hired'
              else 'Not possible to hire'
          end as hire_or_no,
          etd.counter+1 as counter
  from        expense_tracking_data as etd 
  inner join  Buy_order_of_employees as boe 
          on  boe.intended_order_to_buy = etd.counter+1
)
-- select count(id),position 
-- from expense_tracking_data
-- where hire_or_no = 'Hired'
-- group by position
select * from expense_tracking_data
------------------------- Explanation chunks -- End -------------------------------------------------------
