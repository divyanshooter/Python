# Kafka Food Ordering Platform

This Python project includes modules to generate random order data, send it to a Kafka topic, and consume those orders for further processing. It uses the Faker library to create user details and a predefined restaurant menu to generate order items.

## Requirements

- Python 3.x
- Kafka Python library
- Faker library

You can install the required libraries using pip:

```bash
pip install kafka-python faker
```

## Overview

The project consists of five main components:

1. **Order Generation**: A function that creates random order data.
2. **Kafka Producer**: A script that sends generated orders to a specified Kafka topic.
3. **Kafka Consumer**: A script that consumes orders from the Kafka topic and sends confirmation to another Kafka topic.
4. **Confirmed Orders Consumer**: A script that listens for confirmed orders and prints out confirmation messages.
5. **Revenue Tracking Consumer**: A script that tracks total orders and revenue from the orders consumed.

## Order Generator

The `get_orders` function generates a random order containing a unique order ID, user details, selected menu items, and a total cost.

### Restaurant Menu

The following items are included in the restaurant menu:

- Margherita Pizza
- Cheeseburger
- Caesar Salad
- Spaghetti Carbonara
- Grilled Salmon
- Chicken Tikka Masala
- Vegetable Stir Fry
- Beef Tacos
- Pancakes
- Shrimp Scampi
- Mushroom Risotto
- Chocolate Lava Cake
- Caprese Salad
- Lamb Chops
- Fettuccine Alfredo
- Tom Yum Soup

### Usage of `get_orders`

You can use the `get_orders` function to generate a random order. Here’s an example of how to call the function:

```python
from your_module_name import get_orders

order = get_orders()
print(order)
```

#### Example Output

The `get_orders` function returns a dictionary structured as follows:

```json
{
    "order_id": 12345,
    "user_id": "user@example.com",
    "name": "John Doe",
    "items": [
        "Margherita Pizza",
        "Cheeseburger"
    ],
    "cost": 40,
    "created_at": "2023-10-21"
}
```

## Utility Functions and Constants

These are defined in your `utilty` module:

### JSON Serializer

```python
import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")
```

### Configuration Constants

```python
BOOTSTARP_SERVERS = 'localhost:9092'
ORDERS_KAFKA_TOPIC = "food_orders"
ORDERS_CONFIRMED_KAFKA_TOPIC = "food_orders_confirmed"
ORDER_LIMIT = 100
```

## Kafka Producer

The following script initializes a Kafka producer and sends generated orders to a specified Kafka topic at regular intervals.

### Producer Script

Here’s the script for sending orders to Kafka:

```python
from kafka import KafkaProducer
import time
from orders import get_orders
from utilty import json_serializer, ORDER_LIMIT, ORDERS_KAFKA_TOPIC, BOOTSTARP_SERVERS

producer = KafkaProducer(bootstrap_servers=BOOTSTARP_SERVERS, value_serializer=json_serializer)

if __name__ == '__main__':
    for i in range(ORDER_LIMIT):
        producer.send(ORDERS_KAFKA_TOPIC, get_orders())
        time.sleep(5)
```

### Running the Producer

1. Ensure your Kafka broker is running.
2. Run the producer script:

```bash
python your_producer_script_name.py
```

The script will send `ORDER_LIMIT` number of orders to the specified Kafka topic, with a 5-second delay between each message.

## Kafka Consumer

The following script initializes a Kafka consumer that listens for incoming orders and sends confirmation to another Kafka topic.

### Consumer Script

Here’s the script for consuming orders and sending confirmations:

```python
from kafka import KafkaProducer, KafkaConsumer
from utilty import json_serializer, ORDERS_KAFKA_TOPIC, ORDERS_CONFIRMED_KAFKA_TOPIC, BOOTSTARP_SERVERS
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=json_serializer)
consumer = KafkaConsumer(ORDERS_KAFKA_TOPIC, bootstrap_servers=BOOTSTARP_SERVERS)

if __name__ == '__main__':
    while True:
        for msg in consumer:
            consumed_msg = json.loads(msg.value)
            user_id = consumed_msg['user_id']
            total_cost = consumed_msg['cost']
            print("Successful Transaction")
            data = {"user_id": user_id, "total_cost": total_cost}
            producer.send(ORDERS_CONFIRMED_KAFKA_TOPIC, data)
```

### Running the Consumer

1. Ensure your Kafka broker is running.
2. Run the consumer script:

```bash
python your_consumer_script_name.py
```

The consumer will continuously listen for new orders on the specified topic and send a confirmation message to the `ORDERS_CONFIRMED_KAFKA_TOPIC`.

## Confirmed Orders Consumer

This script listens for confirmed orders and processes them by printing confirmation messages and tracking emails.

### Confirmed Orders Consumer Script

```python
from kafka import KafkaConsumer
from utilty import ORDERS_CONFIRMED_KAFKA_TOPIC, BOOTSTARP_SERVERS
import json

email_so_far = set()

if __name__ == '__main__':
    while True:
        consumer = KafkaConsumer(ORDERS_CONFIRMED_KAFKA_TOPIC, bootstrap_servers=BOOTSTARP_SERVERS)
        for msg in consumer:
            consumed_msg = json.loads(msg.value)
            print(consumed_msg)
            email = consumed_msg['user_id']
            email_so_far.add(email)
            print('Order is confirmed. Send Email to {}.'.format(email))
            print(email_so_far)
```

### Running the Confirmed Orders Consumer

1. Ensure your Kafka broker is running.
2. Run the confirmed orders consumer script:

```bash
python your_confirmed_orders_consumer_script_name.py
```

This script will listen for confirmed orders and print out confirmation messages along with a list of emails that have been processed.

## Revenue Tracking Consumer

This script listens for orders and calculates total revenue and total orders consumed.

### Revenue Tracking Consumer Script

```python
from kafka import KafkaConsumer
from utilty import ORDERS_KAFKA_TOPIC, BOOTSTARP_SERVERS
import json

if __name__ == '__main__':
    consumer = KafkaConsumer(ORDERS_KAFKA_TOPIC, bootstrap_servers=BOOTSTARP_SERVERS)
    total_orders = 0
    total_revenue = 0
    for msg in consumer:
        consumed_msg = json.loads(msg.value)
        total_cost = consumed_msg['cost']
        total_revenue += total_cost
        total_orders += 1
        print("The total orders are: {}".format(total_orders))
        print("The total revenue is: {}".format(total_revenue))
```

### Running the Revenue Tracking Consumer

1. Ensure your Kafka broker is running.
2. Run the revenue tracking consumer script:

```bash
python your_revenue_tracking_consumer_script_name.py
```

This script will listen for new orders and update the total orders and revenue statistics in real time.

## Notes

- The cost is calculated as 20 per item; adjust this logic as needed.
- The order will include a random selection of menu items, with the number of items being anywhere from 1 to the total number of items available in the menu.

## Contributing

If you have suggestions for improvements or find issues, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
