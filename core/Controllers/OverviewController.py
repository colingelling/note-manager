"""

    Created by Colin Gelling on 26/03/2024
    Using Pycharm Professional

"""


class OverviewController:

    """
    This class is responsible for processing raw data before it will get passed into the view
    """

    notebook_storage_path = None
    notebook_information = None

    def __init__(self):
        super().__init__()
    
    @staticmethod
    def _set_notebook_storage():
        from core.Handlers.NotebookStorageHandler import NotebookStorage
        access_model = NotebookStorage()
        OverviewController.notebook_storage_path = access_model.get_notebook_storage_path()
        
    @staticmethod
    def _set_notebook_information():
        from core.Collections.NotebookCollection import NotebookCollection
        collection_model = NotebookCollection()
        OverviewController.notebook_information = collection_model.get_notebook_information('*', '*')

    def get_view_data(self):
        self._set_notebook_information()
        self._set_notebook_storage()
        
        prepared_data = ({
            "notebook_storage_path": self.notebook_storage_path,
            "notebook_information": self.notebook_information
        })
        
        print(f"View data: '{prepared_data}'")

        return prepared_data
