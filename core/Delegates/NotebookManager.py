"""

    Created by Colin Gelling on 17/01/2024
    Using Pycharm Professional

"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QStyledItemDelegate


class NotebookManager(QStyledItemDelegate):
    def __init__(self):
        super().__init__()

        self.widget = None

    def set_widget(self, obj):
        self.widget = obj

    def paint(self, painter, option, index):
        widget = self.widget

        # Retrieve the model from the widget
        model = widget.model()

        # Retrieve data for the index
        model.data(index, Qt.ItemDataRole.DisplayRole)

        # Set the foreground color to black
        option.palette.setColor(QPalette.ColorRole.Text, QColor(0, 0, 0))

        # Customize the painting of items here
        super().paint(painter, option, index)
