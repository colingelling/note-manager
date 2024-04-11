"""

    Created by Colin Gelling on 26/03/2024
    Using Pycharm Professional

"""


class NotebookStorage:

    storage_path = None

    def get_notebook_storage_path(self):
        # Retrieve usable information from the application in general
        from core.Import.Configurations import Configurations
        import_model = Configurations()
        config_collection = import_model.get_navigation_config()
        self._set_storage(config_collection)

        return self.storage_path

    @staticmethod
    def _set_storage(dictionary):
        # Iterate through the dictionary and pick the path that matches root storage
        for key, value in dictionary.items():
            if 'storage' in key:
                NotebookStorage.storage_path = value + "/notebooks"
