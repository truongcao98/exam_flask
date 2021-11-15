from kafka import KafkaConsumer


class Consumer:

    @staticmethod
    def read_data_from_kafka():
        bootstrap_servers = ['localhost:29092']
        topic = 'assign-task'
        consumer = KafkaConsumer(topic, auto_offset_reset='latest',
                                 bootstrap_servers=bootstrap_servers,
                                 value_deserializer=lambda value: value.decode('utf-8'))