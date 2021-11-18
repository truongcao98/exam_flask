import json
import time

from kafka import KafkaProducer


class Producer:
    @staticmethod
    def push_data_to_kafka_1():
        bootstrap_servers = ['localhost:9092']
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                 value_serializer=lambda value: bytes(value, encoding='utf-8'),
                                 client_id='truongcl')

        topic = 'ads-analyzing-stt'
        for x in range(1000):
            data = {
                "staff": str(x * 2),
            }
            producer.send(topic, value=json.dumps(data), partition=0)
            print(x)
            time.sleep(0.1)


if __name__ == "__main__":
    Producer().push_data_to_kafka_1()
