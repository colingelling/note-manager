"""

    Created by Colin Gelling on 25/09/2023
    Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QDialog

import os

from core.Controllers.WindowController import WindowController


class DialogCreateNote(QDialog, WindowController):

    requested_note = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.initUi()

        self.create_note = None

        self.show_content()

    def load_ui(self):
        from src.gui.ui.management.components.DialogCreateNote.DialogCreateNote import Ui_DialogCreateNote
        ui = Ui_DialogCreateNote()
        ui.setupUi(self)

        return ui

    def initUi(self):
        with open("src/gui/css/dialog-create-note.css", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            return self.setStyleSheet(stylesheet)

    def show_content(self):
        ui = self.ui

        from views.components.OptionsDialogCreate import OptionsDialogCreate
        view = OptionsDialogCreate()
        window_title = view.add_note_dialog_title

        ui.HeadlineLabel.setText(window_title)
        ui.HeadlineLabel.adjustSize()

        ui.DialogDescriptionText.setText("Add a note by entering the title, a description and confirm by pressing the button if you're done!")
        ui.DialogDescriptionText.adjustSize()

        ui.WhatIsYourNewNoteNameLabel.setText("What should the title of your note be?")
        ui.WhatIsYourNewNoteNameLabel.adjustSize()

        ui.SelectParentNotebook.setText("Select a notebook for this note")
        ui.SelectParentNotebook.adjustSize()

        self.notebook_selector(ui.ParentNotebookSelector)
        ui.ParentNotebookSelector.setEnabled(True)

        ui.WhatIsYourNewNoteDescription.setText("What should the body description of your note be?")
        ui.WhatIsYourNewNoteDescription.adjustSize()

        ui.AddNoteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ui.AddNoteButton.clicked.connect(self.add_note_button)

    @staticmethod
    def notebook_selector(selector):

        from core.app_information import AppInformation
        app_information = AppInformation()

        # Set base path according to the storage folder
        storage_root = app_information.application_storage()

        # Expand the tilde (~) to the user's home directory
        storage_folder = os.path.expanduser(storage_root)

        # Manually name the directory about where to look in
        notebook_directory = "notebooks"

        # Combine them as path value
        path_result = f"{storage_folder}/{notebook_directory}"

        # Show an empty ComoBox upon launch of this dialog
        selector.addItem("")

        # Verify that the combined path value is existing and has been created already
        if os.path.exists(path_result) and os.path.isdir(path_result):
            # List one-level directories in the specific path
            directories = [d for d in os.listdir(path_result) if os.path.isdir(os.path.join(path_result, d))]

            # Add directories as values to the ComboBox
            selector.addItems(directories)

    def add_note_button(self):
        ui = self.ui

        # Store the title
        note_title = ui.NoteNamelineEdit.text()

        # Store the notebook value
        # notebook_selector = ui.ParentNotebookSelector.textActivated()

        # Store the note text
        # note_body = ui.NoteBodytextEdit.text()

        # Emit a signal to notify the Overview window to add the new note
        self.requested_note.emit(note_title)

        self.accept()
