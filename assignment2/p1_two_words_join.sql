select count(distinct f0.docid)
from frequency as f0 ,frequency as f1
where f0.docid = f1.docid and f0.term='transactions' and f1.term = 'world';
