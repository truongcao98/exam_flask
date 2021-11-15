import time

from kafka import KafkaConsumer, TopicPartition


class Consumer:

    @staticmethod
    def read_data_from_kafka_3():
        bootstrap_servers = ['localhost:9092']
        topic = 'main_test'
        consumer = KafkaConsumer(
            # topic,
            # auto_offset_reset='latest',
            bootstrap_servers=bootstrap_servers,
            # value_deserializer=lambda value: value.decode('utf-8'),
            group_id="consumer_group"
        )
        consumer.assign([TopicPartition(topic, 2)])
        for msg in consumer:
            print(msg.value)
            time.sleep(5)


if __name__ == "__main__":
    Consumer.read_data_from_kafka_3()
