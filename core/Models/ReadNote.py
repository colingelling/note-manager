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
            return self.read(file_info.filePath())

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
    def read(notebook_information):

        directory = None

        file_path = None
        file_name = None
        
        listed_notebook = [value for key, value in notebook_information.items() if key == 'notebooks']
        listed_note_path = [value for key, value in notebook_information.items() if key == 'note_path_values']
        
        from pathlib import Path
        file_name = Path(listed_note_path[0][0]).stem
        
        directory = listed_notebook[0][0]
        file_path = listed_note_path[0][0]

        with open(file_path, "r") as file:
            content = file.read()

            separate_description = content.split(file_name + '\n\n')
            description_text = ''.join(separate_description)

            file_information = {
                "filePath": file_path,
                "fileName": file_name,
                "parentDirectory": directory,
                "fileContent": description_text
            }

            return file_information
