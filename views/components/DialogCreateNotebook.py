"""

    Created by Colin Gelling on 13/09/2023
    Using Pycharm Professional

"""
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QDialog

from core.Controllers.WindowController import WindowController


class DialogCreateNotebook(QDialog, WindowController):

    requested_notebook = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.initUi()

        self.create_notebook = None

        self.show_content()

    def load_ui(self):
        from src.gui.ui.management.components.DialogCreateNotebook.DialogCreateNotebook import Ui_DialogCreateNotebook
        ui = Ui_DialogCreateNotebook()
        ui.setupUi(self)

        return ui

    def initUi(self):
        with open("src/gui/css/dialog-create-notebook.css", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            return self.setStyleSheet(stylesheet)

    def show_content(self):
        ui = self.ui

        from views.components.OptionsDialogCreate import OptionsDialogCreate
        view = OptionsDialogCreate()
        window_title = view.add_notebook_dialog_title

        ui.HeadlineLabel.setText(window_title)
        ui.HeadlineLabel.adjustSize()

        ui.WhatIsYourNewNotebookNameLabel.setText("What is the name of your new notebook?")
        ui.WhatIsYourNewNotebookNameLabel.adjustSize()

        ui.AddNotebookButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ui.AddNotebookButton.clicked.connect(self.add_notebook_button)

    def add_notebook_button(self):

        ui = self.ui

        # Store text value
        new_notebook_text = ui.NewNotebookNamelineEdit.text()

        # Emit a signal to notify the Overview window to add the new notebook
        # self.requested_notebook.emit(new_notebook_text)

        # self.accept()  # Close the dialog

        from views.Overview import Overview
        view = Overview()
        return view.add_note_group(new_notebook_text)
