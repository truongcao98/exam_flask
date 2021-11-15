import time

from kafka import KafkaConsumer, TopicPartition


class Consumer:

    @staticmethod
    def read_data_from_kafka_2():
        bootstrap_servers = ['localhost:9092']
        topic = 'main_test'
        consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            group_id="consumer_group"
        )
        consumer.assign([TopicPartition(topic, 1)])
        for msg in consumer:
            print(msg.value)
            time.sleep(2)


if __name__ == "__main__":
    Consumer.read_data_from_kafka_2()
