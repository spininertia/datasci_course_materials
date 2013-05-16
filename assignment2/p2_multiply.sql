select sum(value)
from 
(select A.row_num as row_num,B.col_num as col_num,A.value * B.value as value
from A,B
where A.col_num = B.row_num)
group by row_num,col_num
having row_num=2 and col_num=3;
