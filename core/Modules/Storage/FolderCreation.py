"""

    Created by Colin Gelling on 06/12/2023
    Using Pycharm Professional

"""


class FolderCreation:
    def __init__(self):
        super().__init__()

    @staticmethod
    def save_notebook(notebook_title):

        from core.app_information import AppInformation
        app_information = AppInformation()
        root_folder = app_information.application_storage()

        notebook_directory = "notebooks"

        import os
        notebook_destination = os.path.expanduser(f"{root_folder}/{notebook_directory}")
        os.makedirs(notebook_destination, exist_ok=True)

        # Create a directory for the notebook
        notebook_path = os.path.join(notebook_destination, notebook_title)
        os.makedirs(notebook_path, exist_ok=True)

        print(f"Notebook saved to: '{notebook_path}'")
