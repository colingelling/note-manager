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


class CreateNoteDialog(QDialog, WindowController):

    requested_note = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.load_style()

        self.create_note = None

        self.show_content()

    def load_ui(self):
        from src.gui.ui.dialogs.DialogCreateNote.DialogCreateNote import Ui_DialogCreateNote
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
        ui.WhatIsYourNewNoteDescription.setText("What should the description of your note be?")
        ui.WhatIsYourNewNoteDescription.adjustSize()

        # Set a different pointer status for the save button
        ui.AddNoteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Bind the add_note_button functionality to the button
        ui.AddNoteButton.clicked.connect(self.add_note_button)

    def notebook_selector(self, selector):

        """
        Add a list of notebooks into the selector comboBox
        :param selector: ui.ParentNotebookSelector
        :return:
        """

        # Show an empty ComoBox upon launch of this dialog
        selector.addItem("")

        from core.Models.ManageNotebook import ManageNotebooks
        model = ManageNotebooks()

        if model.get_notebooks():
            notebooks = model.get_notebooks()
            selector.addItems(notebooks)

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

        # TODO: Replace with source logic
        root_path = "/home/colin/Desktop/note-manager/notebooks"
        notebook_path = os.path.join(root_path, selected_notebook)
        # End TODO

        # Store the note
        from core.Models.StoreNote import StoreNote
        obj = StoreNote()
        obj.store_note(notebook_path, note_template)

        self.accept()
