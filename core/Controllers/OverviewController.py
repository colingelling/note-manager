"""

    Created by Colin Gelling on 26/03/2024
    Using Pycharm Professional

"""

from core.Collectables.NotebookCollector import NotebookCollector


class OverviewController:

    """
    This class is responsible for processing raw data before it will get passed into the view
    """
    
    notebook_storage_path = None
    notebook_information = None

    def __init__(self):
        super().__init__()
        
        self.collector_model = NotebookCollector()
    
    @staticmethod
    def _set_notebook_storage():
        from core.Manage.NotebookStorage import NotebookStorage
        access_model = NotebookStorage()
        OverviewController.notebook_storage_path = access_model.get_notebook_storage_path()
        
    def _set_notebook_information(self):
        model = self.collector_model
        OverviewController.notebook_information = model.get_notebook_information('*', '*')

    def get_view_data(self):
        self._set_notebook_storage()
        self._set_notebook_information()
        
        data = ({
            "notebook_storage_path": self.notebook_storage_path,
            "notebook_information": self.notebook_information
        })

        return data
