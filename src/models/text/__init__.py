import json
from pathlib import Path

from configs import Action


class TextModel:

    @staticmethod
    def read_file(path):
        try:
            input_file = open(path, Action.READ)
            input_data = input_file.read()
            result = json.loads(input_data)
            input_file.close()
            return result
        except Exception as e:
            print('read_file', e)
