class OverviewController:

    """
    This class is responsible for processing raw data before it will get passed into the view
    """

    def __init__(self, view_obj):
        super().__init__()
        self.view_obj = view_obj
        self.notebook_storage_path = None
        self._set_notebook_storage()

    def _set_notebook_storage(self):
        from core.Reader import Reader
        reader = Reader()
        resources = reader.read_configuration('resources.navigation')

        from core.Accessor import Accessor
        accessor = Accessor()
        resource_path = accessor.notebook_storage(resources)
        self.notebook_storage_path = resource_path

    def processed_data(self):
        processed_data = {
            'notebook_storage_path': self.notebook_storage_path
        }

        return processed_data
