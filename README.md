README:
/*  Author: Anand Keshri */

Problem Statement:
"ABC" is one of the largest supermarket chains in India. They have their stores spread across different cities and they cater to thousands of customers everyday. They are in need of a dashboard where they can see the sales metrics for that day in a near real time manner. Assume that the store back office software has an adapter that emits the sales data at receipt level to a kafka queue as soon as the sale happens. The requirements we have for you is to build a stream processing system that would aggregate the sales receipts by store level since that day morning. Feel free to use any technology that suits this process and please add a README file to the github repository, along with the code, describing the architecture and why then chosen technology would suit it. 

Input: 

Kafka queue name : sales_receipts

Kafka message JSON schema: 

{
    "store_id": <some_integer>,
    "receipt_id": <some_integer>,
    "customer_id": <some_integer>,
    "items": [
        {
            "item_id": <some_integer>,
            "quantity": <some_integer>,
            "total_price_paid": <some_float>
        }
    ]
}

Output

The stream processor is expected to print the aggregated sales details every 30 seconds on to the console in the below format:

[
    {"store_id": <some_integer>, "total_sales_price": <aggregated_sales_price>}
]


Kafka Architecture:
From the official website of Kafka "Apache Kafka™ is a distributed streaming platform", where a producer push the data stream and a consumer consumes data stream.
Producer needs to know that exactly where it needs to push the data stream, we call this location as 'Topic', similarly consumer needs to know that from which 'Topic' it
needs to consume the data.

As per the problem statement, I have created a Consumer (KafkaConsumer.py), which consumes sales receipts which are pushed from multiple stores in the 'sales_receipts' kafka queue (Topic).
After consuming receipts from Topic, it aggregates the total sales price on store_id and print it on dashboard every 30 seconds. For the testing, I have created a producer,
which generates reciepts with random values for receipts data.

Technology:
I have used Kafka for python to address this problem.



Prerequisite to run this code:
Install python 2.7
Install Kafka-python

How to Run:
run kafkaConsumer.py, to be ready to consume data on one console
run Producer.py  on another consol (it will generate receipts every second and send it to topic)




