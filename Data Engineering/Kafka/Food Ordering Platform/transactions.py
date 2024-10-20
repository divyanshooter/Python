from kafka import KafkaProducer,KafkaConsumer
from utilty import json_serializer,ORDERS_KAFKA_TOPIC,ORDERS_CONFIRMED_KAFKA_TOPIC,BOOTSTARP_SERVERS
import json


producer=KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=json_serializer)
consumer=KafkaConsumer(ORDERS_KAFKA_TOPIC,bootstrap_servers=BOOTSTARP_SERVERS)

if __name__=='__main__':
    while True:
        for msg in consumer:
           consumed_msg=json.loads(msg.value)
           print(consumed_msg)