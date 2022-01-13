import json
import time

from kafka import KafkaProducer

from src.common import ServerName


class Producer:
    @staticmethod
    def push_data_to_kafka_4():
        bootstrap_servers = [ServerName.SERVER]
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                 value_serializer=lambda value: bytes(value, encoding='utf-8'))

        topic = 'dnc-e0-retry-kafka'
        for x in range(1000):
            data = {
                "staff": str(x * 5),
            }
            producer.send(topic, value=json.dumps(data))
            print(x)
            # time.sleep(0.5)


if __name__ == "__main__":
    Producer().push_data_to_kafka_4()

