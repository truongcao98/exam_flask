import json
import time
from datetime import datetime, timedelta

import requests


class Test:

    def test(self):
        start = datetime.now() - timedelta(minutes=5)
        end = datetime.now()
        print(start.timestamp())
        print(end.timestamp())
        a = requests.get('http://192.168.5.28:9090/api/v1/query?query=(1 - avg(rate(node_cpu_seconds_total{}[5m])) by (instance))*100&time=1649844413.46')
        a = json.loads(a.text)
        print(a)
        return a


if __name__ == '__main__':
    Test().test()
