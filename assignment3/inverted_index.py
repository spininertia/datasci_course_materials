from MapReduce import MapReduce
import sys

mr = MapReduce()

def mapper(record):
	key, value = record
	terms = set(value.split())
	for term in terms:
		mr.emit_intermediate(term,key)

def reducer(key, list_of_values):
	mr.emit((key,list_of_values))
	
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)




