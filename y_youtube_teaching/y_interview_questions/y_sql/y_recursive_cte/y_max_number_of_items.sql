What is the maximum number of items that can be bought by spending at most $100?
I just need the output value as 26.(20 pencils + 5 Rubbers + 1 scale).
I dont want the list of items,i just need the maximum possible products.
if the table only have the below values.

-------------------------------------
|           INPUT TABLE             |
-------------------------------------
ProductName |   Price   |   Quantity|
-------------------------------------
Pencil      |   3       |   20      |
Rubber      |   4       |   5       |
Scale       |   4       |   15      |
-------------------------------------


------------------------------ SETUP -- START --------------------------------------------------------

create table if not exists product
(
    product_name varchar(20),
    price int,
    quantity int
);

insert into product values ('Pencil',3,20);
insert into product values ('Rubber',4,5);
insert into product values ('Scale',50,4);

select * from product;
------------------------------ SETUP -- END --------------------------------------------------------


------------------------------ Solution -- start --------------------------------------------------------

with recursive cten as
(
    select
      product_name,
      1 as nbr
    from product

    union all

    select
      a.product_name,
      a.nbr+1
    from cten a 
    inner join product b on a.product_name=b.product_name
    where a.nbr<b.quantity
),
final_cte as 
(
    select
        a.nbr,
        b.product_name,
        b.price,
        sum(b.price) over(order by b.price,b.product_name,a.nbr) as total_price
    from cten a 
    inner join product b on b.product_name=a.product_name
    order by b.price,b.product_name,a.nbr
)
select count(nbr) 
from final_cte 
where total_price<=100

------------------------------ Solution -- END --------------------------------------------------------


------------------------------ Explanation -- start --------------------------------------------------------

--- CHUNK 1
with recursive cten as
(
    select
      product_name,
      1 as nbr
    from product

    union all

    select
      a.product_name,
      a.nbr+1
    from cten a 
    inner join product b on a.product_name=b.product_name
    where a.nbr<b.quantity
)
select * from cten;


--- CHUNK 2
with recursive cten as
(
    select
      product_name,
      1 as nbr
    from product

    union all

    select
      a.product_name,
      a.nbr+1
    from cten a 
    inner join product b on a.product_name=b.product_name
    where a.nbr<b.quantity
),
final_cte as 
(
    select
        a.nbr,
        b.product_name,
        b.price,
        sum(b.price) over(order by b.price,b.product_name,a.nbr) as total_price
    from cten a 
    inner join product b on b.product_name=a.product_name
    order by b.price,b.product_name,a.nbr
)
select * from final_cte


--- CHUNK 3 and final solution 

with recursive cten as
(
    select
      product_name,
      1 as nbr
    from product

    union all

    select
      a.product_name,
      a.nbr+1
    from cten a 
    inner join product b on a.product_name=b.product_name
    where a.nbr<b.quantity
),
final_cte as 
(
    select
        a.nbr,
        b.product_name,
        b.price,
        sum(b.price) over(order by b.price,b.product_name,a.nbr) as total_price
    from cten a 
    inner join product b on b.product_name=a.product_name
    order by b.price,b.product_name,a.nbr
)
select count(nbr) 
from final_cte 
where total_price<=100

------------------------------ Explanation -- end --------------------------------------------------------
