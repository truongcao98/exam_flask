from kafka import KafkaConsumer

BOOTSTRAP_SERVERS = ['localhost:29092']
username2 = input('What is your name? ')

consumer = KafkaConsumer(username2, auto_offset_reset='latest',
                         bootstrap_servers=BOOTSTRAP_SERVERS,
                         value_deserializer=lambda value: value.decode('utf-8'))

for msg in consumer:
    print(msg.value)