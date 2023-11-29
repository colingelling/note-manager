"""

    Created by Colin Gelling on 07/11/2023
    Using Pycharm Professional

"""

import os

from core.app_information import AppInformation


class ManageDirectoryCollections:

    target = None

    content = {}

    def __init__(self):
        super().__init__()

    @staticmethod
    def storage_path():
        obj = AppInformation()
        storage = os.path.abspath(obj.application_storage())
        return storage

    def get_notebooks(self, source, selector):

        """
          Set resource path, put the notebooks dictionary together with the resource path, a single notebook and the
          selector value into the next function
        :param source:
        :param selector:
        :return:
        """

        notebooks = {}

        resource = self._set_storage_category(source)

        # Iterate over the source directories
        for path in resource:
            if "notebooks" in path:
                for root, dirs, files in os.walk(path):
                    for directory in dirs:
                        if selector == directory:
                            self._add_notebook_to_collection(path, notebooks, directory, selector)

                        if selector == '*':
                            self._add_notebook_to_collection(path, notebooks, directory, selector)

                    break

        return notebooks

    def _set_storage_category(self, source):

        # Include storage path
        storage_path = self.storage_path()

        # Collect resource directories and attempt to find the chosen source value
        resource = self._collect_resources(storage_path, source)

        return resource

    @staticmethod
    def _collect_resources(storage, source):
        """
          Request a storage location (path value) for where to start from, use the source value to select a specific
          value or use '*' to select on all values, return directories that were found as path values

          Function output: collection contains first layer path values (showing categories)
        :param storage:
        :param source:
        :return:
        """

        collection = []

        for root, dirs, files in os.walk(storage):
            for directory in dirs:

                selector = source
                path = os.path.join(storage, directory)

                if selector == '*':
                    collection.append(path)

                if selector == directory:
                    collection.append(path)

            break

        return collection

    def _add_notebook_to_collection(self, path, notebooks, directory, selector):
        # Set notebooks based on showing all information or only specifics
        if selector == directory:
            self._set_notebook_collection(notebooks, path, directory)
        else:
            self._set_notebook_collection(notebooks, path, directory)

    def _set_notebook_collection(self, collection, notebook_path, notebook):
        # Use the values and put them into the original notebooks dictionary
        notebook_path = os.path.join(notebook_path, notebook)
        notebook_collection = self._create_collection(notebook_path, notebook)
        collection[notebook] = notebook_collection

    @staticmethod
    def _create_collection(notebook_path, notebook_name):
        # Create a dictionary for a notebook and notes
        return {
            'notebook_path': notebook_path,
            'notebook': notebook_name,
            'notes': {}  # Initialize an empty dictionary for notes
        }
