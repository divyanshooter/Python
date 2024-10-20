from kafka import KafkaProducer
import json
import time
from data import get_registered_users

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def get_partition(key,all,available):
    #to send all msg to parition 0
    return 0

producer=KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=json_serializer,partitioner=get_partition)

if __name__=='__main__':
    while 1==1:
        registered_user=get_registered_users()
        producer.send("registered_users_project1",registered_user)
        print(registered_user)
        time.sleep(4)