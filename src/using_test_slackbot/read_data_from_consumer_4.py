import time

from kafka import KafkaConsumer, TopicPartition

from src.common import Common, ServerName


class Consumer:
    def __init__(self):
        self.topic_name = 'dnc-e0-retry-kafka'

    def read_data_from_kafka_4(self):
        bootstrap_servers = [ServerName.SERVER]
        consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            group_id='dnc-common-event',
            client_id='truongcl4'
        )
        consumer.subscribe([self.topic_name])
        for msg in consumer:
            print(msg.value)
            consumer.commit()
            time.sleep(5)


if __name__ == "__main__":
    Consumer().read_data_from_kafka_4()
