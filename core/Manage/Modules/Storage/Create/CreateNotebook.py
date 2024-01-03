"""

    Created by Colin Gelling on 06/12/2023
    Using Pycharm Professional

"""


class CreateNotebook:

    def __init__(self):
        super().__init__()

    @staticmethod
    def store_notebook(notebook_name):
        from config.resources.set_storage import ApplicationStorage
        app_information = ApplicationStorage()
        root_folder = app_information.application_storage()

        notebook_directory = "notebooks"  # TODO: Use Core.Manage.Resources.NotebookResource

        import os
        notebook_destination = os.path.join(root_folder, notebook_directory)
        os.makedirs(notebook_destination, exist_ok=True)

        # Create a directory for the notebook
        notebook_path = os.path.join(notebook_destination, notebook_name)
        os.makedirs(notebook_path, exist_ok=True)

        print(f"Notebook saved to: '{notebook_path}'")
