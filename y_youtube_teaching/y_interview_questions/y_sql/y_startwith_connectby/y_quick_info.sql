SELECT 
    LEVEL,
    LPAD(' ', 2 * (LEVEL - 1)) || employee_name AS employee_name,
    manager_id
FROM 
    employees
START WITH 
    manager_id IS NULL             -- Start at the CEO (Level 1)
CONNECT BY 
    PRIOR employee_id = manager_id -- Connect where the PRIOR employee is the current manager
ORDER SIBLINGS BY 
    employee_name;                 -- Orders nodes at the same level (optional)



Pseudocolumn,Description
LEVEL,Returns the depth of the node in the hierarchy (the root is level 1).
CONNECT_BY_ISLEAF,"Returns 1 if the node has no children; otherwise, 0."
CONNECT_BY_ROOT,Returns the value of an expression from the root row of the hierarchy.
SYS_CONNECT_BY_PATH,"Returns the path from the root to the current node, usually as a concatenated string."