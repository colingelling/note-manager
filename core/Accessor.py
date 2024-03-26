"""

    Created by Colin Gelling on 25/03/2024
    Using Pycharm Professional

"""


class Accessor:
    def __init__(self):
        super().__init__()

    @staticmethod
    def notebook_storage(dictionary):
        for key, value in dictionary.items():
            if 'storage' in key:
                notebook_storage = value + "/notebooks"
                return notebook_storage
