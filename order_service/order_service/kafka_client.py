from kafka import KafkaProducer, KafkaConsumer
import json

class KafkaClient:
    def __init__(self, broker_list, topic):
        self.producer = KafkaProducer(bootstrap_servers=broker_list, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        self.consumer = KafkaConsumer(topic, bootstrap_servers=broker_list, value_deserializer=lambda v: json.loads(v.decode('utf-8')))
        self.topic = topic

    def send_message(self, key, value):
        self.producer.send(self.topic, key=key.encode('utf-8'), value=value)
        self.producer.flush()

    def get_messages(self):
        return self.consumer
