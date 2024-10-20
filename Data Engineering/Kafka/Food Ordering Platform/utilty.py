import json
def json_serializer(data):
    return json.dumps(data).encode("utf-8")

BOOTSTARP_SERVERS='localhost:9092'
ORDERS_KAFKA_TOPIC="food_orders"
ORDERS_CONFIRMED_KAFKA_TOPIC="food_orders_confirmed"
ORDER_LIMIT=100