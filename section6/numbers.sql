SELECT
*  
FROM
  numdata12345678.mytable


SELECT
*  
FROM
  numdata12345678.mytable

LIMIT
  5


SELECT
number, square, cube_root
FROM
  numdata12345678.mytable

LIMIT
  5


SELECT
*
FROM
  numdata12345678.mytable
WHERE
  square > 1000



SELECT
*
FROM
  numdata12345678.mytable
WHERE
  square > 1000
  AND
  square < 10000




SELECT
  number as num, square, square_root
FROM
  numdata12345678.mytable
WHERE
  square > 1000
  AND square < 10000
ORDER BY square_root desc
LIMIT
  10;