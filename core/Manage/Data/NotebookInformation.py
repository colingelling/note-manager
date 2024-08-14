"""

    Created by Colin Gelling on 12/08/2024
    Using Pycharm Professional

"""

import json


class NotebookInformation:
    def __init(self):
        super().__init__()
        
    @staticmethod
    def base_path(path):
        pass
     
    @staticmethod
    def blueprint():
        return {
            "notebook_values": [],
            "notebook_path_values": [],
            "note_values": [],
            "note_path_values": []
        }
    
    def dump_json(self):
        json_object = json.dumps(self.blueprint(), indent=4)
        
        with open("/home/colin/Desktop/note-manager/data/sample.json", "w") as outfile:
            outfile.write(json_object)
    