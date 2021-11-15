from kafka import KafkaConsumer, TopicPartition


class Consumer:

    @staticmethod
    def read_data_from_kafka():
        TOPIC = "main_test"
        PARTITION_0 = 0
        PARTITION_1 = 1
        PARTITION_2 = 2
        PARTITION_3 = 3

        consumer_0 = KafkaConsumer(
            group_id='consumer_group', bootstrap_servers=['localhost:9092']
        )
        consumer_1 = KafkaConsumer(
            group_id='consumer_group', bootstrap_servers=['localhost:9092']
        )
        consumer_2 = KafkaConsumer(
            group_id='consumer_group', bootstrap_servers=['localhost:9092']
        )
        consumer_3 = KafkaConsumer(
            group_id='consumer_group', bootstrap_servers=['localhost:9092']
        )
        topic_partition_0 = TopicPartition(TOPIC, PARTITION_0)
        topic_partition_1 = TopicPartition(TOPIC, PARTITION_1)
        topic_partition_2 = TopicPartition(TOPIC, PARTITION_2)
        topic_partition_3 = TopicPartition(TOPIC, PARTITION_3)
        # format: topic, partition
        consumer_0.assign([topic_partition_0])
        consumer_1.assign([topic_partition_1])
        consumer_2.assign([topic_partition_2])
        consumer_3.assign([topic_partition_3])


if __name__ == "__main__":
    Consumer().read_data_from_kafka()
