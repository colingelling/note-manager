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

        # Receive the title that was set earlier from within the Dialog mentioned below
        from views.components.OptionsDialogCreate import OptionsDialogCreate
        view = OptionsDialogCreate()
        window_title = view.add_note_dialog_title

        # Also set the title as a label
        ui.HeadlineLabel.setText(window_title)
        ui.HeadlineLabel.adjustSize()

        # Adding a description for user friendliness
        ui.DialogDescriptionText.setText("Add a note by entering the title, a description and confirm by pressing the button if you're done!")
        ui.DialogDescriptionText.adjustSize()

        # Declare first input label content (Name and note title)
        ui.WhatIsYourNewNoteNameLabel.setText("What should the title of your note be?")
        ui.WhatIsYourNewNoteNameLabel.adjustSize()

        # Declare label content for the ComboBox into selecting a notebook for binding purposes
        ui.SelectParentNotebook.setText("Select a notebook for this note")
        ui.SelectParentNotebook.adjustSize()

        # Enable the ComboBox and pass it to the 'notebook_selector' function in order to find the notebooks
        ui.ParentNotebookSelector.setEnabled(True)
        self.notebook_selector(ui.ParentNotebookSelector)

        # Declare label content for adding a note description
        ui.WhatIsYourNewNoteDescription.setText("What should the body description of your note be?")
        ui.WhatIsYourNewNoteDescription.adjustSize()

        # Set a different pointer status for the save button
        ui.AddNoteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Bind the add_note_button functionality to the button
        ui.AddNoteButton.clicked.connect(self.add_note_button)

    @staticmethod
    def notebook_selector(selector):

        """
        Use the content of selector and the application's storage folder to find categorized subdirectories, add these
        as items to the ComboBox
        :param selector: ui.ParentNotebookSelector
        :return:
        """

        # Declare and get access to the following class
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

    def get_notebooks(self):
        from core.Manage.Collections.NotebookCollection import NotebookCollection
        collection_obj = NotebookCollection()

        # Set a source directory within storage, followed by selecting a notebook
        notebook_information = collection_obj.get_collection('*', '*')

        return notebook_information

    def add_note_button(self):
        # Initialize the layout
        ui = self.ui

        # Store the note title
        note_title = ui.NoteNamelineEdit.text()

        # Store the notebook value from 'notebook_selector' functionality
        selected_notebook = ui.ParentNotebookSelector.currentText()

        # Store the note description content
        note_description = ui.NoteBodytextEdit.toPlainText()

        # Put all information into a Dictionary
        note_template = {
            "Title": note_title,
            "Notebook": selected_notebook,
            "Description": note_description
        }

        import json
        # Prepare the Dictionary as a JSON formatted string because of what the 'requested_note' signal expects
        note_template_str = json.dumps(note_template)

        # Emit a signal (requested_note) to notify the Overview window to add the new note
        # (Putting the Dictionary into the signal)
        self.requested_note.emit(note_template_str)

        # TODO: Seeing updated collection, consider next whether the entire collection should be updated in the Ui or
        #  only the specific one (note_title)
        print(self.get_notebooks())

        # Close this Dialog window (class)
        self.accept()
