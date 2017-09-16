from kafka import KafkaProducer
import time
import json
from random import randint

def generateReceipt():
	receipt = {}
	receipt['store_id'] = randint(4,6)
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

def run():
	producer = KafkaProducer(bootstrap_servers='localhost:9092')
	i = 0
	while True:
		receipt_json = generateReceipt()
		producer.send('my-topic', receipt_json)
		time.sleep(1)
		
run()



#{
#    "store_id": <some_integer>,
#    "receipt_id": <some_integer>,
#    "customer_id": <some_integer>,
#    "items": [
#        {
#            "item_id": <some_integer>,
#            "quantity": <some_integer>,
#            "total_price_paid": <some_float>
#        }
#    ]
#}
#
#receipt = {}
#receipt['store_id'] = s_id
#receipt['receipt_id'] = r_id
#receipt['customer_id'] = c_id
#
#item_array = []
#for i in range(10):
#	item = {}
#	item['item_id'] = _item_id
#	item['quantity'] = qty
#	item['total_price_paid'] = tpp
#	item_array.append(item)
#receipt['items'] = item_array
#receipt_json = json.dumps(receipt)