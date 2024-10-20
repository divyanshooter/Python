from kafka import KafkaProducer,KafkaConsumer
from utilty import json_serializer,ORDERS_KAFKA_TOPIC,ORDERS_CONFIRMED_KAFKA_TOPIC,BOOTSTARP_SERVERS
import json


producer=KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=json_serializer)
consumer=KafkaConsumer(ORDERS_KAFKA_TOPIC,bootstrap_servers=BOOTSTARP_SERVERS)

if __name__=='__main__':
    while True:
        for msg in consumer:
           consumed_msg=json.loads(msg.value)
           user_id=consumed_msg['user_id']
           total_cost=consumed_msg['cost']
           print("Successful Transaction")
           data={"user_id":user_id,"total_cost":total_cost}
           producer.send(ORDERS_CONFIRMED_KAFKA_TOPIC,data)