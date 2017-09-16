from kafka import KafkaConsumer
import json
import time
from cStringIO import StringIO

_INTERVAL = 10
_MESSAGE_INDEX = 6
_KAFKA_QUEUE = 'sales_receipts'

def salesDashboard():
	consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
	consumer.subscribe([_KAFKA_QUEUE])
	dict={}
	start = time.time()
	for message in consumer:
		receipt_json = message[_MESSAGE_INDEX]
		f = StringIO(receipt_json)
		receipt = json.loads(f.read())
		store_id = receipt['store_id']
		total_sale = 0
		for item in receipt['items']:
			total_sale = total_sale + item['total_price_paid']
		if store_id in dict:
			dict[store_id] = dict[store_id] + total_sale
		else:
			dict[store_id] = total_sale
		end = time.time()
		if(end - start >_INTERVAL):
			print '\n\n'
			for key, value in dict.iteritems() :
				print '"store id : "' , key
				print '"total_sales_price"', value
			print '\n\n'
			start = end
		
salesDashboard()

