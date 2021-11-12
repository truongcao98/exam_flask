import requests

r = requests.get("http://192.168.1.7:9308/metrics")
# a = a.json()
result = r.text
result2list = result.split('\n')
list_1 = list()
for x in result2list:
    if "kafka_topic_partition_leader" in x and "#" not in x:
        a = x.split()
        if int(a[1]) != 0:
            list_1.append(x)
# print(a)
print(list_1)
print(len(list_1))
