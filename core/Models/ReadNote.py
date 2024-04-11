"""

    Created by Colin Gelling on 06/03/2024
    Using Pycharm Professional

"""

from PyQt6.QtCore import QModelIndex, Qt
from PyQt6.QtGui import QFileSystemModel


class ReadNote(QFileSystemModel):

    def __init__(self, parent=None):
        super(ReadNote, self).__init__(parent)
        self.file_path = None

    def data(self, index: QModelIndex, role: int = ...) -> object:
        if role == Qt.ItemDataRole.DisplayRole:
            file_info = self.fileInfo(index)
            return self.read(file_info.filePath(), '')

        return super().data(index, role)

    @staticmethod
    def prepare_temporary_note(file_name, file_content):
        note_title = None
        description = []

        if file_name:
            note_title = ''.join(file_name)

        if file_content:
            description.append(file_content)

        description_string = ''.join(description)
        return [note_title, description_string]

    @staticmethod
    def read(path, notebook_information):

        notebook = None

        file_path = None
        file_name = None

        for collection in notebook_information:
            for key, value in collection.items():
                if '.txt' not in value:
                    notebook = key
                else:
                    file_path = value
                    file_name = key

        with open(path, "r") as file:
            content = file.read()

            separate_description = content.split(file_name + '\n\n')
            description_text = ''.join(separate_description)

            file_information = {
                "filePath": file_path,
                "fileName": file_name,
                "parentDirectory": notebook,
                "fileContent": description_text
            }

            return file_information
