"""

    Created by Colin Gelling on 26/03/2024
    Using Pycharm Professional

"""


class OverviewController:

    """
    This class is responsible for processing raw data before it will get passed into the view
    """

    notebook_storage_path = None

    def __init__(self, child_view):
        super().__init__()
        self.view_obj = child_view
        self.notebook_storage_path = None
        self._set_notebook_storage()

    def _set_notebook_storage(self):
        from core.Handlers.NotebookStorageHandler import NotebookStorage
        access_model = NotebookStorage()
        self.notebook_storage_path = access_model.get_notebook_storage_path()

    def get_view_data(self):
        data = {
            'notebook_storage_path': self.notebook_storage_path
        }

        return data
