select max(score)
from(
select b.docid as docid,sum(a.count*b.count) as score
from query as a, frequency as b
where a.docid = 'q' and a.term = b.term
group by docid);

