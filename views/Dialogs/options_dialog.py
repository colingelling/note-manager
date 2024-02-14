"""

    Created by Colin Gelling on 06/09/2023
    Using Pycharm Professional

"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QDialog

from core.Controllers.WindowController import WindowController


class OptionsDialog(QDialog, WindowController):

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.setFixedSize(468, 344)

        self.window_title = "What do you want to add?"
        self.setWindowTitle(self.window_title)

        self.load_style()

        self.show_content()

    def load_ui(self):
        from src.gui.ui.dialogs.OptionsDialogCreate.OptionsDialogCreate import Ui_OptionsDialogCreate
        ui = Ui_OptionsDialogCreate()
        ui.setupUi(self)

        return ui

    def load_style(self):
        with open("src/gui/css/options-dialog-create.css", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            return self.setStyleSheet(stylesheet)

    def show_content(self):
        ui = self.ui

        ui.HeadlineLabel.setText(self.window_title)
        ui.HeadlineLabel.adjustSize()

        ui.CreateNotebookButton.clicked.connect(WindowController.create_notebook_dialog)
        ui.CreateNotebookButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ui.CreateNotebookButton.setText("A notebook")

        ui.CreateNoteButton.clicked.connect(WindowController.create_note_dialog)
        ui.CreateNoteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ui.CreateNoteButton.setText("A note")
