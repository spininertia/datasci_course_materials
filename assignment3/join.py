import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
	rec_type = record[0]
	order_id = record[1]
	mr.emit_intermediate(order_id,(rec_type,record))
	
def reducer(key, list_of_values):
	orders = []
	line_items = []
	for value in list_of_values:
		rec_type = value[0]
		if rec_type == 'order':
			orders.append(value[1])
		else:
			line_items.append(value[1])
	for order in orders:
		for item in line_items:
			mr.emit(order+item)

if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
