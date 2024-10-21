from kafka import KafkaConsumer
from utilty import ORDERS_KAFKA_TOPIC,BOOTSTARP_SERVERS
import json

if __name__=='__main__':
    consumer=KafkaConsumer(ORDERS_KAFKA_TOPIC,bootstrap_servers=BOOTSTARP_SERVERS)
    total_orders=0
    total_revenue=0
    for msg in consumer:
        consumed_msg=json.loads(msg.value)
        total_cost=consumed_msg['cost']
        total_revenue+=total_cost
        total_orders+=1
        print("The total orders are : {}".format(total_orders))
        print("The total revenue are : {}". format(total_revenue))

