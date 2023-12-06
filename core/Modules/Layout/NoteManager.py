"""

    Created by Colin Gelling on 06/11/2023
    Using Pycharm Professional

"""

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel


class NoteManager:

    # layout properties
    horizontal_layout_container = None
    horizontal_layout = None

    def __init__(self):
        super().__init__()

        # flag to check if layout has been created
        self.layout_created = False

        # property for the notebook manager layout element
        self.manager_layout = None

    def create_layout(self, ui):
        # create the layout only the first time
        if not self.layout_created:
            # create a layout inside the NotebookWidget
            self.manager_layout = QVBoxLayout()  # Create a common layout

            # Set alignment to top
            self.manager_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

            # Create a container widget for the horizontal layout
            self.horizontal_layout_container = QtWidgets.QWidget()

            # Create the horizontal layout
            self.horizontal_layout = QtWidgets.QHBoxLayout()

            # Set the horizontal layout for the container widget
            self.horizontal_layout_container.setLayout(self.horizontal_layout)

            # Add the container widget (with the horizontal layout) to the vertical layout
            self.manager_layout.addWidget(self.horizontal_layout_container)

            # define and set the layout
            ui.NotebookWidget.setLayout(self.manager_layout)

            # alter the flag
            self.layout_created = True

            return self.manager_layout

    def add_notebooks(self, manager_layout, notebook_collection):

        # Open the collection and start decorating
        for notebook, collection in notebook_collection.items():
            # TODO:
            #  2) Every notebook should be in a separated widget (including actions like edit and delete)

            parent_widget = QWidget()

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

            parent_widget.setLayout(layout)

            manager_layout.addWidget(parent_widget)

            # Handle mouse events for the icon_label
            icon_label.mousePressEvent = lambda event, label=icon_label: self.toggle_notebook_icon(label)

    @staticmethod
    def toggle_notebook_icon(icon_label):
        # Toggle the icon's orientation when the icon_label is clicked
        current_icon = icon_label.text()
        if current_icon == "\uf0da":
            icon_label.setText("\uf0d7")  # Change to a different icon (pointing down)
            icon_label.setStyleSheet("font-size: 8px; color: #000; /* additional styles for down icon */")
        else:
            icon_label.setText("\uf0da")  # Change back to the original icon (pointing right)
            icon_label.setStyleSheet("font-size: 8px; color: #000; /* additional styles for down icon */")
