"""

    Created by Colin Gelling on 25/03/2024
    Using Pycharm Professional

"""

import importlib
import os


class Reader:

    """
    This class reads and returns dictionary data from configuration config
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def read_configuration(reference):

        """
        Import the given attribute as a module and return it as a dictionary
        """

        if '.' in reference:
            print(f"Reference: {reference}")
            model_import = importlib.import_module(reference)
            resources = getattr(model_import, "resources", {})
            return resources
