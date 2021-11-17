import time

from kafka import KafkaConsumer, TopicPartition

from src.common import Common


class Consumer:

    @staticmethod
    def read_data_from_kafka_1():
        bootstrap_servers = ['localhost:9092']
        topic = 'voucher-internal-grant-code-profile'
        consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            group_id=Common.group_consumer,
            enable_auto_commit=True,
            auto_commit_interval_ms=1,
            auto_offset_reset='latest',
            client_id="truongcl"
        )
        consumer.assign([TopicPartition(topic, 0)])
        for msg in consumer:
            print(msg.value)
            time.sleep(0.5)


if __name__ == "__main__":
    Consumer.read_data_from_kafka_1()
