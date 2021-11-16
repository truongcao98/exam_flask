import json
import time

from kafka import KafkaProducer


class Producer:
    @staticmethod
    def push_data_to_kafka_2():
        bootstrap_servers = ['localhost:9092']
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                 value_serializer=lambda value: bytes(value, encoding='utf-8'))

        topic = 'voucher-internal-grant-code-profile'
        for x in range(1000):
            data = {
                "staff": str(x*3),
            }
            producer.send(topic, value=json.dumps(data), partition=1)
            time.sleep(0.3)


if __name__ == "__main__":
    Producer().push_data_to_kafka_2()
