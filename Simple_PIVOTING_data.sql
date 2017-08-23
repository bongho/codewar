or this challenge you need to PIVOT data. You have two tables, products and details. Your task is to pivot the rows in products to produce a table of products which have rows of their detail. Group and Order by the name of the Product.

Tables and relationship below:



You must use the CROSSTAB statement to create a table that has the schema as below:

CROSSTAB table.

name
good
ok
bad
Compare your table to the expected table to view the expected results.

CREATE EXTENSION tablefunc;
-- Create your CROSSTAB statement here

SELECT * 
FROM CROSSTAB(
              'SELECT A.NAME,B.DETAIL,COUNT(B.*) ct
               FROM PRODUCTS A, DETAILS B
               WHERE A.ID = B.PRODUCT_ID
               GROUP BY 1,2
               ORDER BY 1,2'
               ,$$VALUES ('good'::text), ('ok'::text),('bad'::text)$$)
AS ct (NAME text, good int, ok int, bad int); 

select *
from crosstab(
  'select p.name, d.detail, count(1)::int as value
  from products p
    inner join details d
      on p.id = d.product_id
  group by 1, 2
  order by 1, 2',
  $$values ('good'), ('ok'), ('bad')$$)
  as (name text, good int, ok int, bad int)
order by name
