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

from core.Resources.Storage import StorageResources


class CreateNoteDialog(QDialog, WindowController):

    requested_note = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.load_style()

        self.create_note = None

        # set application storage
        storage_obj = StorageResources()
        storage_root = storage_obj.get_resource_path('notebooks')
        self.storage = storage_root

        self.show_content()

    def load_ui(self):
        from src.gui.ui.management.components.DialogCreateNote.DialogCreateNote import Ui_DialogCreateNote
        ui = Ui_DialogCreateNote()
        ui.setupUi(self)

        return ui

    def load_style(self):
        with open("src/gui/css/dialog-create-note.css", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            return self.setStyleSheet(stylesheet)

    def show_content(self):
        ui = self.ui

        window_title = "Create a note"
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

    def notebook_selector(self, selector):

        """
        Use the content of selector and the application's storage folder to find categorized subdirectories, add these
        as items to the ComboBox
        :param selector: ui.ParentNotebookSelector
        :return:
        """

        # Show an empty ComoBox upon launch of this dialog
        selector.addItem("")

        # Verify that the combined path value is existing and has been created already
        if os.path.exists(self.storage):
            # List one-level directories in the specific path
            directories = [d for d in os.listdir(self.storage) if os.path.isdir(os.path.join(self.storage, d))]

            # Add directories as values to the ComboBox
            selector.addItems(directories)

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

        notebook_path = os.path.join(self.storage, selected_notebook)

        # Store the note
        from core.Models.CreateNote import CreateNote
        obj = CreateNote()
        obj.store_note(notebook_path, note_template)

        if not WindowController:
            print(f"WindowController is not available")

        # Get access to important window data
        data_obj = WindowController.accessible_data
        tree_view = data_obj.tree_view

        # Update the notebook-manager  # TODO: Temporarily full rebuild
        from core.Models.RebuildTree import RebuildTree
        rebuild_obj = RebuildTree()
        rebuild_obj.rebuild(tree_view)

        self.accept()
