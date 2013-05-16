select count(*)
from(
select distinct docid
from frequency
group by docid
having sum(count) > 300);
