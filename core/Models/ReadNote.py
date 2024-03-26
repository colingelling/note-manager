"""

    Created by Colin Gelling on 06/03/2024
    Using Pycharm Professional

"""

import os

from PyQt6.QtCore import QModelIndex, Qt
from PyQt6.QtGui import QFileSystemModel


class ReadNote(QFileSystemModel):

    def __init__(self, parent=None):
        super(ReadNote, self).__init__(parent)
        self.file_path = None

    def data(self, index: QModelIndex, role: int = ...) -> object:
        if role == Qt.ItemDataRole.DisplayRole:
            file_info = self.fileInfo(index)
            return self.read(file_info.filePath())

        return super().data(index, role)

    @staticmethod
    def prepared_list(note_information):
        note_title = None
        description = []

        for key, value in note_information.items():

            if "Name" in key:
                note_title = ''.join(value)

            if "Description" in key:
                description.append(value)

        description_string = ''.join(description)
        return note_title, description_string

    @staticmethod
    def read(file_path):

        with open(file_path, "r") as file:
            content = file.read()

        from core.Collections.NotebookInformation import CollectNotebooks
        model = CollectNotebooks()

        notebooks = model.get_notebooks('*')
        file_name = os.path.basename(file_path).split('.')[0]

        for notebook in notebooks:
            if notebook in file_path and file_name in content:
                separate_description = content.split(file_name + '\n\n')
                description_text = ''.join(separate_description)

                file_information = {
                    "filePath": file_path,
                    "fileName": file_name,
                    "parentNotebook": notebook,
                    "fileDescription": description_text
                }

                return file_information
