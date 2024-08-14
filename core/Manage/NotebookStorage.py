"""

    Created by Colin Gelling on 26/03/2024
    Using Pycharm Professional

"""
import importlib


class NotebookStorage:
    
    notebook_storage_path = None
    storage_path = None

    def __init__(self):
        super().__init__()

    def get_notebook_storage(self):
        # Retrieve usable parameters
        model_import = importlib.import_module('config.navigation')
        resource = getattr(model_import, "resources", {})
        
        self._set_storage_properties(resource)

        return self.storage_path

    @staticmethod
    def _set_storage_properties(dictionary):
        # Iterate through the dictionary and pick the path that matches root storage
        for key, value in dictionary.items():
            if 'storage' in key:
                NotebookStorage.notebook_storage_path = value + "/notebooks"
                NotebookStorage.storage_path = value
