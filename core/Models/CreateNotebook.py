"""

    Created by Colin Gelling on 06/12/2023
    Using Pycharm Professional

"""


class CreateNotebook:

    def __init__(self):
        super().__init__()

    @staticmethod
    def store_notebook(notebook_name):
        from core.Resources.Storage import StorageResources
        storage_obj = StorageResources()

        storage_root = storage_obj.get_resource_path('notebooks')

        # Create a directory for the notebook
        import os
        notebook_path = os.path.join(storage_root, notebook_name)
        os.makedirs(notebook_path, exist_ok=True)

        print(f"Notebook saved to: '{notebook_path}'")
