import time

from kafka import KafkaConsumer, TopicPartition

from src.common import Common


class Consumer:
    def __init__(self):
        self.topic_name = 'merge-profile'

    def read_data_from_kafka_3(self):
        bootstrap_servers = ['localhost:9092']
        topic = 'ads-analyzing-stt'
        consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            group_id=Common.group_consumer,
            client_id='truongcl3'
        )
        # consumer.assign([TopicPartition(topic, 2)])
        consumer.subscribe([self.topic_name])
        for msg in consumer:
            print(msg.value)
            # consumer.commit()
            time.sleep(2)


if __name__ == "__main__":
    Consumer().read_data_from_kafka_3()
