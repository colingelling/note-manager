"""

    Created by Colin Gelling on 04/12/2023
    Using Pycharm Professional

"""


class ManageNotebookResources:

    resource_path = None
    source_path = None

    def __init__(self):
        super().__init__()

    def get_storage(self):

        self._set_source()

        self._set_resource(self.resource_path)

        resource = self._get_resource_path()

        return resource

    def _set_source(self):
        from core.Manage.Resources.StorageResources import ManageStorageResources
        obj = ManageStorageResources()
        source = obj.get_source()
        self.source_path = source

    def _set_resource(self, source):
        resource = 'notebooks'
        resource_path = f"{self.source_path}/{resource}"
        self.resource_path = resource_path

    def _get_resource_path(self):
        return self.resource_path
