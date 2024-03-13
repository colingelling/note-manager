"""

    Created by Colin Gelling on 16/01/2024
    Using Pycharm Professional

"""

from PyQt6.QtCore import QModelIndex, Qt
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtWidgets import QTreeView


class BuildTree(QFileSystemModel):

    def __init__(self, root_path, parent=None):
        super(BuildTree, self).__init__(parent)
        self.setRootPath(root_path)
        self.tree = None

    def data(self, index: QModelIndex, role: int = ...) -> object:
        if role == Qt.ItemDataRole.DisplayRole:
            file_info = self.fileInfo(index)
            return file_info.completeBaseName()

        return super().data(index, role)

    def build(self, root_index):

        self.tree = QTreeView()
        self.tree.setModel(self)
        self.tree.setRootIndex(root_index)

        self.customize(self.tree)

        return self.tree

    @staticmethod
    def customize(tree):
        # Hide column names
        header = tree.header()
        header.setSectionHidden(0, False)
        header.setSectionHidden(1, True)
        header.setSectionHidden(2, True)
        header.setSectionHidden(3, True)

        # Hide column-headers
        return header.hide()

    @staticmethod
    def open_note(index):

        index_model = index.model()
        path_value = index_model.filePath(index)

        if 'txt' in path_value:
            from core.Controllers.WindowController import WindowController
            # from views.Dialogs.opened_note import OpenedNote
            dialog = WindowController.opened_note_dialog(path_value)
            return dialog
