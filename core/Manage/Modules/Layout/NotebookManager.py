"""

    Created by Colin Gelling on 11/12/2023
    Using Pycharm Professional

"""

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QObject
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


class NotebookManager(QtWidgets.QMainWindow):

    horizontal_layout_container = None
    horizontal_layout = None

    layout_created = False

    def __init__(self):
        super().__init__()

        self.layout = None
        self.widgets = []

    def add_notebooks(self, notebook_collection):

        # print(notebook_collection)  # TODO: Not getting output

        # Open the collection and start decorating
        for notebook, collection in notebook_collection.items():

            widget = QWidget()

            # Set the icon
            notebook_arrow_unicode = "\uf0da"

            # Create a QLabel for the icon
            icon_label = QLabel(notebook_arrow_unicode)
            icon_label.setStyleSheet("font-size: 8px; color: #000")

            notebook_label = QLabel(notebook)
            notebook_label.setStyleSheet("color: #000")

            # Create a horizontal layout for the icon and text
            layout = QtWidgets.QHBoxLayout()

            # Add the icon label to the layout and align it to the left
            layout.addWidget(icon_label)
            layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

            # Add some spacing between the icon and text
            layout.addSpacing(1)

            layout.setContentsMargins(4, 0, 4, 0)  # Adjust the left and right margins as needed

            # Add the label with notebook name to the layout and align it to the left
            layout.addWidget(notebook_label)

            widget.setLayout(layout)

            self.layout.addWidget(widget)

            self.widgets.append(widget)  # Keep track of the created widget

            # Handle mouse events for the icon_label
            icon_label.mousePressEvent = lambda event, label=icon_label: self.toggle_notebook_icon(label)

            # Add note(s) within this (or an individual) notebook
            self.add_notes(collection)

    @staticmethod
    def toggle_notebook_icon(icon_label):
        # Toggle the icon's orientation when the icon_label is clicked
        current_icon = icon_label.text()
        icon_style = "font-size: 8px; color: #000; /* additional styles for down icon */"
        if current_icon == "\uf0da":
            icon_label.setText("\uf0d7")  # Change to a different icon (pointing down)
            icon_label.setStyleSheet(icon_style)
        else:
            icon_label.setText("\uf0da")  # Change back to the original icon (pointing right)
            icon_label.setStyleSheet(icon_style)

    def add_notes(self, collection):

        for notebook_key, notebook_value in collection.items():
            if 'notes' in notebook_key:
                note_collection = notebook_value
                for item in note_collection:
                    note = item['note']

                    widget = QWidget()

                    notebook_label = QLabel(note)
                    notebook_label.setStyleSheet("color: #000")
                    notebook_label.setContentsMargins(13, 0, 0, 0)

                    # Create a horizontal layout for the icon and text
                    layout = QtWidgets.QHBoxLayout()

                    layout.setContentsMargins(4, 0, 4, 0)  # Adjust the left and right margins as needed

                    # Add the label with notebook name to the layout and align it to the left
                    layout.addWidget(notebook_label)

                    widget.setLayout(layout)

                    self.layout.addWidget(widget)

                    self.widgets.append(widget)

                    note_label = QLabel(note)
                    note_label.setStyleSheet("color: #000")

    def create_layout(self, ui):
        # create the layout only the first time
        if not self.layout_created:
            # create a layout inside the NotebookWidget
            self.layout = QVBoxLayout(self.centralWidget())

            # Set alignment to top
            self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

            # Create a container widget for the horizontal layout
            self.horizontal_layout_container = QtWidgets.QWidget()

            # Create the horizontal layout
            self.horizontal_layout = QtWidgets.QHBoxLayout()

            # Set the horizontal layout for the container widget
            self.horizontal_layout_container.setLayout(self.horizontal_layout)

            # Add the container widget (with the horizontal layout) to the vertical layout
            self.layout.addWidget(self.horizontal_layout_container)

            self.layout.deleteLater()

            # define and set the layout
            ui.NotebookWidget.setLayout(self.layout)

            # alter the flag
            self.layout_created = True

            return self.layout
