import os

from config.resources.set_storage import ApplicationStorage


class StorageResources:
    def __init__(self):
        super().__init__()

    def _set_root(self):
        # Retrieve storage path value and return it
        obj = ApplicationStorage()
        storage_path = os.path.abspath(obj.application_storage())
        self.source_path = storage_path

    def get_root(self):
        self._set_root()
        return self.source_path

    def _set_resource_path(self, source):
        root = self.get_root()
        resource_path = os.path.join(root, source)
        print(resource_path)
        return resource_path

    def get_resource_path(self, source):
        return self._set_resource_path(source)
