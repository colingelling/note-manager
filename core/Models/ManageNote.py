"""

    Created by Colin Gelling on 31/01/2024
    Using Pycharm Professional

"""

from PyQt6.QtCore import QModelIndex, Qt
from PyQt6.QtGui import QFileSystemModel


class ManageNote(QFileSystemModel):
    def __init__(self, parent=None):
        super(ManageNote, self).__init__(parent)

    def data(self, index: QModelIndex, role: int = ...) -> object:
        if role == Qt.ItemDataRole.DisplayRole:
            file_info = self.fileInfo(index)
            return self.read_note_values(file_info.filePath())

        return super().data(index, role)

    @staticmethod
    def read_note_values(file_path):

        title = None
        notebook = None
        description = None

        with open(file_path, 'r') as file:
            for line in file:
                key, value = map(str.strip, line.split(':', 1))
                if key == "Title":
                    title = value
                if key == "Notebook":
                    notebook = value
                if key == "Description":
                    description = value

        return title, notebook, description
