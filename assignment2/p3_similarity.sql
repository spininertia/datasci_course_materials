select sum(score)
from(
select a.docid as a_docid, b.docid as b_docid,sum(a.count * b.count) as score
from frequency as a, frequency as b
where a.term = b.term and a.docid = '10080_txt_crude' and b.docid = '17035_txt_earn'
)
group by a_docid,b_docid
having a_docid='10080_txt_crude' and b_docid = '17035_txt_earn';
