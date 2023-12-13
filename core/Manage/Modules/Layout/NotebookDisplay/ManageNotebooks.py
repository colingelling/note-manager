"""

    Created by Colin Gelling on 11/12/2023
    Using Pycharm Professional

"""

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel


class ManageNotebooks:

    def __init__(self):
        super().__init__()

    def add_notebooks(self, manager_layout, notebook_collection):

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

            manager_layout.addWidget(widget)

            # Handle mouse events for the icon_label
            icon_label.mousePressEvent = lambda event, label=icon_label: self.toggle_notebook_icon(label)

            from core.Manage.Modules.Layout.NotebookDisplay.ManageNotes import ManageNotes
            obj = ManageNotes()
            obj.add_notes(manager_layout, notebook, collection)

    @staticmethod
    def add_notebook(notebook_information):
        # TODO - Output example:
        #  {'notebook': 'Notebook', 'notebook_path': '/home/colin/Desktop/note-manager/notebooks/Notebook'}
        print(notebook_information)
        # TODO (As of 12 december 2023, connect with the objects 'CreateElements' to add notebook
        #  into the graphical interface)

        from core.Manage.Elements.UI.CreateElements import CreateElements
        obj = CreateElements()
        obj.create_notebooks(notebook_information)

    @staticmethod
    def update_notebooks(notebook_information):
        # TODO - Output example:
        #  {'notebook': 'Notebook', 'notebook_path': '/home/colin/Desktop/note-manager/notebooks/Notebook'}
        print(notebook_information)

        # TODO (As of 12 december 2023, connect with the objects 'FindElements', and 'CreateElements' to add notebook
        #  into the graphical interface)

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
