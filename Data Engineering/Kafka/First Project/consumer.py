from kafka import KafkaConsumer
import json

if __name__=='__main__':
    consumer=KafkaConsumer("registered_users_project1",bootstrap_servers="localhost:9092",
                           auto_offset_reset='earliest',
                           group_id="cosumer_group1_project1")

    for msg in consumer:
        print("Resgisterd User:{}".format(json.loads(msg.value)))