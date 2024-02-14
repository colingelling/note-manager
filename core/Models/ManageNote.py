"""

    Created by Colin Gelling on 31/01/2024
    Using Pycharm Professional

"""
import os

from PyQt6.QtCore import QModelIndex, Qt
from PyQt6.QtGui import QFileSystemModel


class ManageNote(QFileSystemModel):
    def __init__(self, parent=None):
        super(ManageNote, self).__init__(parent)

    def data(self, index: QModelIndex, role: int = ...) -> object:
        if role == Qt.ItemDataRole.DisplayRole:
            file_info = self.fileInfo(index)
            return self.read_note(file_info.filePath())

        return super().data(index, role)

    @staticmethod
    def read_note(file_path):

        with open(file_path, "r") as file:
            content = file.read()

        file_content = content.split(os.linesep)
        return file_content

    @staticmethod
    def save_note_changes(ui, note_path):

        # TODO: Currently not working properly as it should

        note_title = ui.noteTitle_lineEdit.text()
        selected_notebook = ui.selector_comboBox.currentText()
        note_description = ui.noteDescription_textEdit.toPlainText()

        new_content = {  # TODO: Separate keys from values using the base collection, avoid duplicated code
            "Title": note_title,
            "Notebook": selected_notebook,
            "Description": note_description
        }

        try:
            with open(note_path, 'w') as file:
                for key, value in new_content.items():
                    print(f"Processing changes to the existing note containing the following: \n\n {key}: {value}")
                    new_template = f"{key}: {value}\n\n"
                    file.write(new_template)
        except IOError:
            print("Unable to save changes to the file.")
