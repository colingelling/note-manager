"""

    Created by Colin Gelling on 25/09/2023
    Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QDialog

from core.Controllers.WindowController import WindowController


class CreateNoteView(QDialog, WindowController):

    requested_note = QtCore.pyqtSignal(str)

    def __init__(self, view_data):
        super().__init__()
        
        self.notebook_directories = []
        self.notebook_path_information = []

        # Declaration of view_data elements
        for collection in view_data:
            for key, value in collection.items():
                if "notebook" in key:
                    self.notebook_directories.append(key)
                if "/" in value:
                    self.notebook_path_information.append(value)

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.setMinimumSize(800, 698)

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
        self.setWindowTitle(window_title)
        ui.headlineLabel.setText(window_title)
        ui.headlineLabel.adjustSize()

        # Adding a description for user friendliness
        ui.descriptionText.setText("Add a note by entering the title, a description and confirm by pressing the button "
                                   "if you're done!")
        ui.descriptionText.adjustSize()

        # Declare first input label content (Name and note title)
        ui.noteNameLabel.setText("What should the title of your note be?")
        ui.noteNameLabel.adjustSize()

        # Declare label content for the ComboBox into selecting a notebook for binding purposes
        ui.notebookSelectorLabel.setText("Select a notebook for this note")
        ui.notebookSelectorLabel.adjustSize()

        # Enable the ComboBox
        ui.notebookSelector_comboBox.setEnabled(True)
        
        # Show an empty ComoBox upon launch of this dialog
        ui.notebookSelector_comboBox.addItem("")
        
        # Add the names of all notebook directories into the ComboBox
        ui.notebookSelector_comboBox.addItems(self.notebook_directories)

        # Declare label content for adding a note description
        ui.noteDescriptionLabel.setText("What should the description of your note be?")
        ui.noteDescriptionLabel.adjustSize()

        # Set a different pointer status for the save button
        ui.addNoteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Bind the add_note_button functionality to the button
        ui.addNoteButton.clicked.connect(self.add_note_button)

    def add_note_button(self):
        # Initialize the layout
        ui = self.ui

        # Store the note title
        note_title = ui.noteName_lineEdit.text()

        # Store the notebook value from 'notebook_selector' functionality
        selected_notebook = ui.notebookSelector_comboBox.currentText()

        # Store the note description content
        note_description = ui.noteDescription_textEdit.toPlainText()

        # Put all information into a Dictionary
        note_template = {
            "Title": note_title,
            "Notebook": selected_notebook,
            "Description": note_description
        }
        
        for path_value in self.notebook_path_information:
            if f"/{selected_notebook}/" in path_value + '/' and '.txt' not in path_value:
                # Store the note
                from core.Models.StoreNote import StoreNote
                obj = StoreNote()
                obj.store_note(path_value, note_template)

        self.accept()
