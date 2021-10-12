import json

from kafka import KafkaConsumer
from src.models.mongo.task import TaskCollection


class Consumer:

    @staticmethod
    def read_data_from_kafka():
        BOOTSTRAP_SERVERS = ['localhost:29092']
        topic = 'assign-task'
        consumer = KafkaConsumer(topic, auto_offset_reset='latest',
                                 bootstrap_servers=BOOTSTRAP_SERVERS,
                                 value_deserializer=lambda value: value.decode('utf-8'))
        for msg in consumer:
            print(msg.value)
            a = json.loads(msg.value)
            TaskCollection().insert(a)


if __name__ == "__main__":
    Consumer.read_data_from_kafka()
