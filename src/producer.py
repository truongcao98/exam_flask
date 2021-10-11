from kafka import KafkaProducer

BOOTSTRAP_SERVERS = ['localhost:29092']
producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
                         value_serializer=lambda value: bytes(value, encoding='utf-8'))

username1 = input('What is your name? ')
username2 = input('Who do want connect? ')

while True:
    value = input()
    producer.send(username2, value=value)
    producer.flush()