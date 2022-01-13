from kafka.admin import KafkaAdminClient, NewTopic

from src.common import ServerName

admin_client = KafkaAdminClient(
    bootstrap_servers=ServerName.SERVER,
    client_id="truongcl"
)
list_name_topic = ['ads-analyzing-stt', 'e1119-broadcast-merge', 'merge-profile', 'dnc-e0-retry-kafka']
# list_name_topic = ['save_info_media_sdk']
list_topic = list()
for name in list_name_topic:
    list_topic.append(NewTopic(name=name, num_partitions=4, replication_factor=1))
admin_client.create_topics(new_topics=list_topic, validate_only=False)
