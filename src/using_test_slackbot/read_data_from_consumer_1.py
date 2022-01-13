import time

from kafka import KafkaConsumer, TopicPartition

from src.common import Common, ServerName


class Consumer:
    def __init__(self):
        self.topic_name = 'ads-analyzing-stt'

    # @staticmethod
    def read_data_from_kafka_1(self):
        bootstrap_servers = [ServerName.SERVER]
        consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            group_id=Common.group_consumer,
            auto_offset_reset='latest',
            client_id="truongcl1"
        )
        consumer.subscribe([self.topic_name])

        for msg in consumer:
            print(msg.value)
            time.sleep(0.2)
            consumer.commit()


if __name__ == "__main__":
    Consumer().read_data_from_kafka_1()
