from kafka import KafkaConsumer
from utilty import ORDERS_CONFIRMED_KAFKA_TOPIC,BOOTSTARP_SERVERS
import json

email_so_far=set()

if __name__=='__main__':
    while True:
        consumer = KafkaConsumer(ORDERS_CONFIRMED_KAFKA_TOPIC,bootstrap_servers=BOOTSTARP_SERVERS)
        for msg in consumer:
            consumed_msg=json.loads(msg.value)
            print(consumed_msg)
            email=consumed_msg['user_id']
            email_so_far.add(email)
            print('Order is confirmed.Send Email to  {}.'.format(email))
            print(email_so_far)
