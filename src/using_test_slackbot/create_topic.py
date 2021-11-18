from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id="truongcl"
)
list_name_topic = ['ads-analyzing-stt']
list_topic = list()
for name in list_name_topic:
    list_topic.append(NewTopic(name=name, num_partitions=4, replication_factor=1))
admin_client.create_topics(new_topics=list_topic, validate_only=False)
