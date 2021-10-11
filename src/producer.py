import json

from kafka import KafkaProducer


class Producer:
    @staticmethod
    def push_data_to_kafka(datas):
        BOOTSTRAP_SERVERS = ['localhost:29092']
        producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
                                 value_serializer=lambda value: bytes(value, encoding='utf-8'))

        topic = 'assign-task'
        for x in range(len(datas['tasks'])):
            data = {
                "staff": "uuid",
                "task_infor": datas['tasks'][x]
            }
            producer.send(topic, value=json.dumps(data))
        producer.flush()
