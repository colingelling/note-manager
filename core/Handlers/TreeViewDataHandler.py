"""

    Created by Colin Gelling on 04/04/2024
    Using Pycharm Professional

"""

from PyQt6.QtCore import QModelIndex, Qt
from PyQt6.QtGui import QFileSystemModel


class TreeViewDataHandler(QFileSystemModel):

    def __init__(self, root_path, parent=None):
        super(TreeViewDataHandler, self).__init__(parent)
        self.setRootPath(root_path)

        self.index_model = None
        self.absolute_path = None

    def _set_index_model(self, index):
        self.index_model = index.model()

    def _set_absolute_path(self, model, index):
        self.absolute_path = model.filePath(index)

    def data(self, index: QModelIndex, role: int = ...) -> object:
        if role == Qt.ItemDataRole.DisplayRole:
            file_info = self.fileInfo(index)
            return file_info.completeBaseName()

        return super().data(index, role)

    def open_note(self, index):

        self._set_index_model(index)
        self._set_absolute_path(self.index_model, index)

        # Open the next dialog
        if 'txt' in self.absolute_path:
            from core.Controllers.WindowController import WindowController
            dialog = WindowController.opened_note_dialog(self.absolute_path)
            return dialog
