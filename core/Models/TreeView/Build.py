"""

    Created by Colin Gelling on 16/01/2024
    Using Pycharm Professional

"""

from PyQt6.QtCore import QModelIndex, Qt
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtWidgets import QTreeView


class Build(QFileSystemModel):

    def __init__(self, root_path, parent=None):
        super(Build, self).__init__(parent)
        self.setRootPath(root_path)

        self.tree_view = None
        self.index_model = None

        self.absolute_path = None

    def data(self, index: QModelIndex, role: int = ...) -> object:
        if role == Qt.ItemDataRole.DisplayRole:
            file_info = self.fileInfo(index)
            return file_info.completeBaseName()

        return super().data(index, role)

    def build(self, root_index):
        self.tree_view = QTreeView()
        self.tree_view.setModel(self)
        self.tree_view.setRootIndex(root_index)

        # TODO: Somehow a third note is not showing up after the first two notes were added, the third note does exist
        #  - After a restart of the application all three are showing

        self.customize_tree(self.tree_view)

        return self.tree_view

    @staticmethod
    def customize_tree(tree):
        # Hide column names
        header = tree.header()
        header.setSectionHidden(0, False)
        header.setSectionHidden(1, True)
        header.setSectionHidden(2, True)
        header.setSectionHidden(3, True)

        # Hide column-headers
        return header.hide()

    def open_note(self, index):

        # Setters
        self._set_index_model(index)
        self._set_absolute_path(self.index_model, index)

        path = self.absolute_path

        # Open the next dialog
        if 'txt' in path:
            from core.Controllers.WindowController import WindowController
            dialog = WindowController.opened_note_dialog(path)
            return dialog

    def _set_index_model(self, index):
        self.index_model = index.model()

    def _set_absolute_path(self, model, index):
        self.absolute_path = model.filePath(index)
