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
        self._set_notebook_information()
    
    def _set_notebook_information(self):
        model = self.collector_model
        notebook_information = model.get_notebook_information('*', '*')
        
    @staticmethod
    def get_notebook_storage():
        return OverviewController.notebook_storage_path
    
    @staticmethod
    def get_notebook_information():
        return OverviewController.notebook_information

    def data_handler(self):
        
        self.get_notebook_storage()
        self.get_notebook_information()
        
        from core.Manage.Data.NotebookInformation import NotebookInformation
        data_model = NotebookInformation()
        data_model.dump_json()

        # data = ({
        #     "notebook_storage_path": self.notebook_storage_path,
        #     "notebook_information": self.notebook_information
        # })
        #
        # return data
