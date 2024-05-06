"""

    Created by Colin Gelling on 26/03/2024
    Using Pycharm Professional

"""
import importlib


class NotebookStorage:

    storage_path = None

    def get_notebook_storage_path(self):
        # Retrieve usable information from the application in general
        
        model_import = importlib.import_module('config.navigation')
        resource = getattr(model_import, "resources", {})
        
        self._set_storage(resource)

        return self.storage_path

    def _set_storage(self, dictionary):
        # Iterate through the dictionary and pick the path that matches root storage
        for key, value in dictionary.items():
            if 'storage' in key:
                self.storage_path = value + "/notebooks"
