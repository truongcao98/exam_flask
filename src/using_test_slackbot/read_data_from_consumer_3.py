import time

from kafka import KafkaConsumer, TopicPartition

from src.common import Common


class Consumer:

    @staticmethod
    def read_data_from_kafka_3():
        bootstrap_servers = ['localhost:9092']
        topic = 'ads-analyzing-stt'
        consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            group_id=Common.group_consumer
        )
        consumer.assign([TopicPartition(topic, 2)])
        for msg in consumer:
            print(msg.value)
            consumer.commit()
            time.sleep(5)


if __name__ == "__main__":
    Consumer.read_data_from_kafka_3()
