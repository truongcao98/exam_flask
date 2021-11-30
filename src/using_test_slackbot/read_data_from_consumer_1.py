import time

from kafka import KafkaConsumer, TopicPartition

from src.common import Common


class Consumer:
    def __init__(self):
        self.topic_name = 'ads-analyzing-stt'

    # @staticmethod
    def read_data_from_kafka_1(self):
        bootstrap_servers = ['localhost:9092']
        topic = 'ads-analyzing-stt'
        consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            group_id=Common.group_consumer,
            # enable_auto_commit=True,
            # auto_commit_interval_ms=1,
            auto_offset_reset='latest',
            client_id="truongcl"
        )
        consumer.subscribe([self.topic_name])
        # consumer.assign([TopicPartition(topic, 0)])

        for msg in consumer:
            print(msg.value)
            consumer.commit()
            time.sleep(0.5)


if __name__ == "__main__":
    Consumer().read_data_from_kafka_1()
