from kafka import KafkaProducer
import time
from orders import get_orders
from utilty import json_serializer,ORDER_LIMIT,ORDERS_KAFKA_TOPIC,BOOTSTARP_SERVERS


producer=KafkaProducer(bootstrap_servers=BOOTSTARP_SERVERS,value_serializer=json_serializer)

if __name__=='__main__':
    for i in range(ORDER_LIMIT):
     producer.send(ORDERS_KAFKA_TOPIC,get_orders())
     time.sleep(5)