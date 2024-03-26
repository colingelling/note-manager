"""

    Created by Colin Gelling on 25/03/2024
    Using Pycharm Professional

"""

import importlib
import os


class Reader:

    """
    This class reads and returns dictionary data from configuration resources
    """

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
    def read_configuration(reference):

        """
        Import the given attribute as a module and return it as a dictionary
        """

        if '.' in reference:
            model_import = importlib.import_module(reference)
            resources = getattr(model_import, "resources", {})
            return resources
