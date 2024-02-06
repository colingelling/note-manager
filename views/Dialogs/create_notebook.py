"""

    Created by Colin Gelling on 13/09/2023
    Using Pycharm Professional

"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QDialog

from core.Controllers.WindowController import WindowController


class CreateNotebookDialog(QDialog, WindowController):

    def __init__(self):
        super().__init__()

        self.ui = self.load_ui()

        self.load_style()

        self.show_content()

    def load_ui(self):
        from src.gui.ui.dialogs.DialogCreateNotebook.DialogCreateNotebook import Ui_DialogCreateNotebook
        ui = Ui_DialogCreateNotebook()
        ui.setupUi(self)

        return ui

    def load_style(self):
        with open("src/gui/css/dialog-create-notebook.css", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            return self.setStyleSheet(stylesheet)

    def show_content(self):
        ui = self.ui

        window_title = "Create a notebook"
        ui.HeadlineLabel.setText(window_title)
        ui.HeadlineLabel.adjustSize()

        ui.WhatIsYourNotebookNameLabel.setText("What is the name of your new notebook?")
        ui.WhatIsYourNotebookNameLabel.adjustSize()

        ui.AddNotebookButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ui.AddNotebookButton.clicked.connect(self.add_notebook_button)

    def add_notebook_button(self):
        ui = self.ui

        # Set text value
        notebook_name = ui.NotebookNamelineEdit.text()
        print(f"notebook_name: {notebook_name}")

        # Store the notebook as a directory
        from core.Models.StoreNotebook import StoreNotebook
        obj = StoreNotebook()
        obj.store_notebook(notebook_name)

        self.accept()
