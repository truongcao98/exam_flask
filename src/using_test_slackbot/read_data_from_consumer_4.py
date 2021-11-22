import time

from kafka import KafkaConsumer, TopicPartition

from src.common import Common


class Consumer:
    def __init__(self):
        self.topic_name = 'ads-analyzing-stt'

    def read_data_from_kafka_4(self):
        bootstrap_servers = ['localhost:9092']
        topic = 'ads-analyzing-stt'
        consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            group_id=Common.group_consumer,
            client_id='truongcl4'
        )
        consumer.assign([TopicPartition(topic, 3)])
        # consumer.subscribe([topic])
        for msg in consumer:
            print(msg.value)
            # consumer.commit()
            time.sleep(5)


if __name__ == "__main__":
    Consumer.read_data_from_kafka_4(3)
