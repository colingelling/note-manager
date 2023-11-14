"""

    Created by Colin Gelling on 07/11/2023
    Using Pycharm Professional

"""

import os
import pathlib

from core.app_information import AppInformation


class ManageDirectoryCollections:

    target_directory = None
    target_file = None

    content = {}

    def __init__(self):
        super().__init__()

        obj = AppInformation()
        self.storage_base = os.path.abspath(obj.application_storage())

        self.base_path = None
        self.notebook_collection = {}

    def first_layer_directories(self):

        directories = [d for d in os.listdir(self.storage_base) if os.path.isdir(os.path.join(self.storage_base, d))]
        if directories:
            return directories

    def second_layer_directories(self, directories):

        if directories:
            for directory in directories:
                full = f"{self.storage_base}/{directory}"
                subdirectories = [d for d in os.listdir(full) if os.path.isdir(os.path.join(full, d))]
                if subdirectories:
                    return subdirectories

    def directory_finder(self, source_directory, target_directory):

        # Set base path value (root/first_layer) ----------------------------------

        first_layer = self.first_layer_directories()

        if not first_layer:
            return print('First layer directories could not be found!')

        for layer in self.first_layer_directories():
            if layer == source_directory:

                root_storage = self.storage_base
                self.base_path = f"{root_storage}/{layer}"

        # List all notebooks ----------------------------------

        notebooks = []

        for root, dirs, files in os.walk(self.base_path):
            for directory in dirs:

                # Add to list
                notebooks.append(directory)

        for notebook in notebooks:

            if notebook == target_directory:
                self.target_directory = notebook
                self.set_collection(notebook)

            if target_directory == '*':
                self.set_collection(notebook)

    def set_collection(self, notebook):
        notebook_path = f"{self.base_path}/{notebook}"

        self.notebook_collection.update({
            'notebook_path': notebook_path,
            'notebook': notebook
        })

    def file_finder(self, source, file_extension):

        for root, dirs, files in os.walk(source):
            for file in files:
                if file.endswith(file_extension):
                    self.target_file = file

                    self.content.update({
                        "child_file": file
                    })

                    return f"{file}"
            # for file in files:
            #     print(file)
                # if file.endswith(file_extension):
                #     file_path = os.path.join(file)
                #     print(f"File found: {file_path}")

        # for root, dirs, files in os.walk(source):
        #     print(f"root: {root}")
        #     print(f"dirs {dirs}")
        #     print(f"files {files}")
        #     for file in files:
        #         if file.endswith(file_extension):
        #             print(f"File found: {os.path.join(root, file)}")

        # first_layer = self.first_layer_directories()
        #
        # if first_layer:
        #     for layer in self.first_layer_directories():
        #         print(layer)  # TODO: notebooks
        #
        #         if layer == source:
        #             print('Pass!')  # TODO: Great success
        #
        #             # Put a dot in front of the extension
        #             dotted_extension = ".{0}".format(file_extension)
        #
        #             # find file by the help of extension value
        #             root_storage = self.storage_base
        #             self.base_path = f"{root_storage}/{layer}"
        #
        #             for root, dirs, files in os.walk(self.base_path):
        #                 for directory in dirs:
        #                     print(directory)

                            # if file.endswith(dotted_extension):
                            #     print(f"File: {os.path.join(base_path, file)}")

                    # for file in os.listdir(base_path):
                    #     print(file)
                    #     if file.endswith(dotted_extension):
                    #         print(f"File {os.path.join(base_path, file)}")
