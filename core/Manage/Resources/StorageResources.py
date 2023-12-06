import os

from core.app_information import AppInformation


class ManageStorageResources:
    def __init__(self):
        super().__init__()

    def _set_source(self):
        # Retrieve storage path value and return it
        obj = AppInformation()
        storage_path = os.path.abspath(obj.application_storage())
        self.source_path = storage_path

    def get_source(self):
        self._set_source()
        return self.source_path
