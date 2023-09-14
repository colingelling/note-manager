"""

    Created by Colin Gelling on 06/09/2023
    Using Pycharm Professional

"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QDialog

from core.Controllers.WindowController import WindowController


class OptionsDialogCreate(QDialog, WindowController):

    add_notebook_dialog_title = "Add a notebook"

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.initUi()

        self.show_content()

    def load_ui(self):
        from src.gui.ui.management.components.OptionsDialogCreate.OptionsDialogCreate import Ui_OptionsDialogCreate
        ui = Ui_OptionsDialogCreate()
        ui.setupUi(self)

        return ui

    def initUi(self):
        with open("src/gui/css/options-dialog-create.css", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            return self.setStyleSheet(stylesheet)

    def show_content(self):
        ui = self.ui

        from views.Overview import Overview
        view = Overview()
        window_title = view.options_dialog_title

        ui.HeadlineLabel.setText(window_title)
        ui.HeadlineLabel.adjustSize()

        ui.CreateNoteGroupButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ui.CreateNoteGroupButton.setText("A notebook")
        ui.CreateNoteGroupButton.clicked.connect(self.show_create_dialog)

        ui.CreateNoteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ui.CreateNoteButton.setText("A note")

    def show_create_dialog(self):
        from views.components.DialogCreateNotebook import DialogCreateNotebook
        dialog = DialogCreateNotebook()
        dialog.setWindowTitle(self.add_notebook_dialog_title)

        # Close this
        self.accept()

        # Show dialog
        dialog.exec()
