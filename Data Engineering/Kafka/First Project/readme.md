# Kafka Producer and Consumer for Registered Users

This repository contains Python scripts that produce and consume messages related to registered users using Apache Kafka. The producer generates fake user data and sends it to a Kafka topic, while the consumer retrieves and displays this data.

## Prerequisites

Before running the scripts, ensure you have the following:

- Python 3.x installed
- Kafka server running on `localhost:9092`
- Required Python packages installed:
  ```bash
  pip install kafka-python faker
  ```

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/divyanshooter/Python.git
   cd Data Engineering/Kafka/First Project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Ensure your Kafka server is running. You can start it using the following command (assuming Kafka is installed):

```bash
bin/kafka-server-start.sh config/server.properties
```

### Running the Producer

To start the Kafka producer, run the following command:

```bash
python producer.py
```

### Running the Consumer

To start the Kafka consumer, run the following command in a new terminal window:

```bash
python consumer.py
```

### How It Works

#### Producer

- The producer uses `KafkaProducer` from the `kafka-python` library to send messages to a Kafka topic.
- It generates fake user data using the `Faker` library in the `get_registered_users` function.
- The generated user data includes a name, address, and creation year.
- The user data is serialized to JSON format before being sent to the topic `registered_users_project1`.
- Messages are sent to partition 0 of the topic.

#### Consumer

- The consumer uses `KafkaConsumer` to listen for messages from the `registered_users_project1` topic.
- It starts reading messages from the earliest offset.
- For each message received, it deserializes the JSON data and prints it to the console.

### Example Output

**Producer Output**:
```
{'name': 'John Doe', 'address': '1234 Elm St, Springfield, IL', 'created_at': '2022'}
```

**Consumer Output**:
```
Registered User: {'name': 'John Doe', 'address': '1234 Elm St, Springfield, IL', 'created_at': '2022'}
```

### Customization

- **Partitioning**: The `get_partition` function in the producer is currently set to send all messages to partition 0. Modify this function to implement custom partitioning logic based on the key.
- **Interval**: The producer script sleeps for 4 seconds between sending messages. Adjust the `time.sleep(4)` line as needed.
- **Consumer Group**: You can modify the `group_id` in the consumer script for different consumer groups.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. 

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- [Kafka Documentation](https://kafka.apache.org/documentation/)
- [kafka-python Library](https://kafka-python.readthedocs.io/en/master/)
- [Faker Library](https://faker.readthedocs.io/en/master/)
