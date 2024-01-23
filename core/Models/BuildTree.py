"""

    Created by Colin Gelling on 16/01/2024
    Using Pycharm Professional

"""

from PyQt6.QtCore import QModelIndex, Qt, pyqtSignal
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtWidgets import QTreeView


class BuildTree(QFileSystemModel):

    data_updated = pyqtSignal()

    def __init__(self, parent=None):
        super(BuildTree, self).__init__(parent)
        self.root_path = "/home/colin/Desktop/note-manager/notebooks"
        self.setRootPath(self.root_path)

    def data(self, index: QModelIndex, role: int = ...) -> object:
        if role == Qt.ItemDataRole.DisplayRole:
            file_info = self.fileInfo(index)
            return file_info.completeBaseName()

        return super().data(index, role)

    def build(self, root_index):
        tree = QTreeView()
        tree.setModel(self)
        tree.setRootIndex(root_index)

        # Hide column names
        header = tree.header()
        header.setSectionHidden(0, False)
        header.setSectionHidden(1, True)
        header.setSectionHidden(2, True)
        header.setSectionHidden(3, True)

        # Hide column-headers
        header.hide()

        return tree
