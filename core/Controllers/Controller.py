"""

    Created by Colin Gelling on 26/03/2024
    Using Pycharm Professional

"""

class Controller:
    def __init__(self):
        super(Controller, self).__init__()
    
    @staticmethod
    def _set_notebook_storage():
        from core.Manage.NotebookStorage import NotebookStorage
        access_model = NotebookStorage()
        
        from core.Controllers.OverviewController import OverviewController
        OverviewController.notebook_storage_path = access_model.get_notebook_storage()