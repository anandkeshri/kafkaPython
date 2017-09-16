from kafka import KafkaProducer
import time
import json
from random import randint

_PRODUCTION_RATE = 1
_KAFKA_QUEUE = 'sales_receipts'
def generateReceipt():
	receipt = {}
	receipt['store_id'] = randint(1,3)
	receipt['receipt_id'] = randint(0,10000)
	receipt['customer_id'] = randint(1,100)

	item_array = []
	for i in range(randint(1,10)):
		item = {}
		item['item_id'] = randint(1,100)
		item['quantity'] = randint(1,5)
		item['total_price_paid'] = randint(10,1000)
		item_array.append(item)
	receipt['items'] = item_array
	print(receipt)
	receipt_json = json.dumps(receipt)
	return receipt_json

def producer():
	producer = KafkaProducer(bootstrap_servers='localhost:9092')
	i = 0
	while True:
		receipt_json = generateReceipt()
		producer.send(_KAFKA_QUEUE, receipt_json)
		time.sleep(_PRODUCTION_RATE)
		
producer()



