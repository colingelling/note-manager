"""

    Created by Colin Gelling on 06/09/2023
    Using Pycharm Professional

"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QDialog

from core.Controllers.WindowController import WindowController


class DisplayOptionsDialog(QDialog, WindowController):

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.load_style()

        self.show_content()

    def load_ui(self):
        from src.gui.ui.management.components.OptionsDialogCreate.OptionsDialogCreate import Ui_OptionsDialogCreate
        ui = Ui_OptionsDialogCreate()
        ui.setupUi(self)

        return ui

    def load_style(self):
        with open("src/gui/css/options-dialog-create.css", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            return self.setStyleSheet(stylesheet)

    def show_content(self):
        ui = self.ui

        window_title = "What do you want to add?"

        ui.HeadlineLabel.setText(window_title)
        ui.HeadlineLabel.adjustSize()

        ui.CreateNoteGroupButton.clicked.connect(WindowController.show_create_notebook_dialog)
        ui.CreateNoteGroupButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ui.CreateNoteGroupButton.setText("A notebook")

        ui.CreateNoteButton.clicked.connect(WindowController.show_create_note_dialog)
        ui.CreateNoteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ui.CreateNoteButton.setText("A note")

    # def show_create_notebook_dialog(self):
    #     from views.Dialogs.create_notebook import CreateNotebookDialog
    #     dialog = CreateNotebookDialog()
    #     dialog.setWindowTitle(self.add_notebook_dialog_title)
    #
    #     # Close this
    #     self.accept()
    #
    #     # Show dialog
    #     dialog.exec()
    #
    # def show_create_note_dialog(self):
    #     # Create access to the next Dialog class (view)
    #     from views.Dialogs.create_note import CreateNoteDialog
    #     dialog = CreateNoteDialog()
    #
    #     # Set the title for the Window bound to the Dialog class
    #     dialog.setWindowTitle(self.add_note_dialog_title)
    #
    #     # Close this window
    #     self.accept()
    #
    #     # Show the next dialog class
    #     dialog.exec()
