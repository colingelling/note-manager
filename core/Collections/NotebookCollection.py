"""

    Created by Colin Gelling on 21/03/2024
    Using Pycharm Professional

"""

import os

from PyQt6.QtGui import QFileSystemModel


class NotebookCollection(QFileSystemModel):
    def __init__(self):
        super().__init__()
        self.notebook_information = {}

        self.directory_information = []
        self.file_information = []

    def get_notebook_information(self, notebook_selector, note_selector):

        #  Declare notebook storage as a resource
        from core.Manage.Handling.NotebookStorageHandler import NotebookStorage
        handler = NotebookStorage()
        resource = handler.get_notebook_storage_path()

        # Verify that the resource has been set, collect all subdirectories
        if resource:
            self.directory_information = self._directory_information_collector(resource)

        # Verify and use the collected directories in order to find all subfiles
        if self.directory_information:
            self.file_information = self._file_information_collector(self.directory_information)

        # Verify both collections and set notebook information in general, unsorted though
        if self.directory_information and self.directory_information:
            self._set_notebook_information(self.directory_information, self.file_information)

        # Check the selector values and sort the dictionary
        if self.notebook_information:
            notebook_values = self._store_notebook_values(notebook_selector)
            note_values = self._store_note_values(notebook_values, note_selector)
            self.notebook_information = notebook_values, note_values

        # Return the final result dictionary
        if self.notebook_information:
            return self.notebook_information

    @staticmethod
    def _directory_information_collector(source):

        """
        Declare a dictionary with lists and add system-level received values into those lists, eventually return the
        dictionary
        """

        collection = {
            "directories": [],
            "path_values": []
        }

        for root, dirs, files in os.walk(source):
            for directory in dirs:
                collection["directories"].append(directory)
                collection["path_values"].append(os.path.join(source, directory))

        return collection

    @staticmethod
    def _file_information_collector(resource_collection):

        """
        Declare a dictionary containing lists, use the absolute path values from the main dictionary in order to get
        system-level file information, add these to the dictionary lists and return the entire dictionary
        """

        collection_items = resource_collection['path_values']

        collection = {
            "files": [],
            "path_values": []
        }

        if collection_items:
            for source in collection_items:
                for root, dirs, files in os.walk(source):
                    for file in files:
                        file_result = file.strip('.txt')
                        collection["files"].append(file_result)
                        collection["path_values"].append(os.path.join(source, file))

        return collection

    def _set_notebook_information(self, directory_information, file_information):

        """
        Sort and combine both pieces of information and store it in another dictionary, return that
        """

        for key, collection in directory_information.items():
            if "directories" in key:
                self.notebook_information.update({
                    "notebooks": collection
                })
            if "path" in key:
                self.notebook_information.update({
                    "notebook_path_values": collection
                })

        for key, collection in file_information.items():
            if "files" in key:
                self.notebook_information.update({
                    "notes": collection
                })
            if "path" in key:
                self.notebook_information.update({
                    "note_path_values": collection
                })

    def _store_notebook_values(self, selector):

        """
          Assign usable attributes to each value type and set the matching pair based on the selector value, return the
          collection pair after
        """

        collection = {}

        # Iterate through the lists associated with directory names and absolute path keys simultaneously, two types of
        # values join the iteration process and use the attributes to keep them separated
        for notebook_name, notebook_path in zip(
                self.notebook_information['notebooks'],
                self.notebook_information['notebook_path_values']
        ):

            if selector == '*':
                collection[notebook_name] = notebook_path
            elif notebook_name == selector:
                collection[notebook_name] = notebook_path

        return collection

    def _store_note_values(self, directory_collection, selector):

        """
          Assign usable attributes to each value type and set the matching pair based on the selector value, return the
          collection after
        """

        collection = {}

        # Iterate through the lists associated with file names and absolute path keys simultaneously, two types of
        # values join the iteration process and use the attributes to keep them separated
        for notebook_name, notebook_path in directory_collection.items():
            for note_name, note_path in zip(
                    self.notebook_information['notes'],
                    self.notebook_information['note_path_values']
            ):

                if notebook_path in note_path:
                    if selector == '*':
                        collection[note_name] = note_path
                    elif note_name == selector:
                        collection[note_name] = note_path

        return collection
