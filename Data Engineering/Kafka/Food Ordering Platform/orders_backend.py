from kafka import KafkaProducer
import time
import json
from orders import get_orders

KAFKA_TOPIC="food_orders"
ORDER_LIMIT=100


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer=KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=json_serializer)

if __name__=='__main__':
    for i in range(ORDER_LIMIT):
     producer.send(KAFKA_TOPIC,get_orders())
     time.sleep(5)