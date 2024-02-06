"""

    Created by Colin Gelling on 06/12/2023
    Using Pycharm Professional

"""

import os


class StoreNotebook:

    def __init__(self):
        super().__init__()

    @staticmethod
    def store_notebook(notebook_name):
        root_path = "/home/colin/Desktop/note-manager/notebooks/"  # TODO: Replace
        notebook_path = os.path.join(root_path, notebook_name)
        os.makedirs(notebook_path, exist_ok=True)

        print(f"Notebook saved to: '{notebook_path}'")
