select count(*)
from
(select distinct docid
from frequency
where term = 'transactions'
intersect
select distinct docid
from frequency
where term = 'world'
);
