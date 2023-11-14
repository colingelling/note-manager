"""

    Created by Colin Gelling on 02/10/2023
    Using Pycharm Professional

"""

import os


class AppInformation:
    def __init__(self):
        super().__init__()

    @staticmethod
    def project_root():
        current_file = __file__

        # Get the absolute path of the current file
        current_file_path = os.path.abspath(current_file)

        # Split the path into directory components
        components = current_file_path.split(os.path.sep)

        # Find the index of the directory you want to consider as the project root
        index = components.index("note-manager")

        # Join the directory components up to the project root index
        project_root = os.path.sep.join(components[:index + 1])

        return project_root

    @staticmethod
    def application_storage():
        return "/home/colin/Desktop/note-manager/"
