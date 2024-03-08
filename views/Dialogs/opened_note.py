"""

    Created by Colin Gelling on 30/01/2024
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QDialog, QMenuBar, QMenu

from core.Managers.ManageNote import ManageNote
from core.Models.ReadNote import ReadNote


class OpenedNote(QDialog):

    def __init__(self, file):
        super().__init__()
        self.file_path = file

        # Read file
        self.note_information = ReadNote().read(self.file_path)

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.setFixedSize(996, 764)

        self.load_style()

        self.show_content()

    def load_ui(self):
        from src.gui.ui.dialogs.OpenedNoteDialog.OpenedNote import Ui_OpenedNoteDialog
        ui = Ui_OpenedNoteDialog()
        ui.setupUi(self)

        return ui

    def load_style(self):
        with open("src/gui/css/opened-note.css", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            return self.setStyleSheet(stylesheet)

    def show_content(self):

        window_subj = 'Viewing note'
        self.setWindowTitle(window_subj)

        # Set window title
        for key, value in self.note_information.items():
            if "Name" in key:
                self.setWindowTitle(window_subj + ": " + value)

        ui = self.ui

        menubar = QMenuBar(self)

        file_menu = QMenu("Actions", self)
        reset_note = file_menu.addAction("Reset")
        save_note = file_menu.addAction("Save")
        delete_note = file_menu.addAction("Delete")

        menubar.addMenu(file_menu)

        ui.gridLayout.setMenuBar(menubar)

        file_menu.setStyleSheet("color: #000;")
        menubar.setStyleSheet("color: #000;")

        ui.noteTitle_lineEdit.setMinimumWidth(974)
        ui.selectorWidget.setMinimumWidth(974)
        ui.noteDescription_textEdit.resize(974, 523)

        ui.noteTitle_label.setText("Title")
        ui.noteTitle_label.adjustSize()

        ui.selector_label.setText("Change the notebook")
        ui.selector_label.adjustSize()

        ui.noteDescription_label.setText("Description")
        ui.noteDescription_label.adjustSize()

        # TODO: Separate this block

        note_information = self.note_information

        description_content = []
        parent_notebook = None
        note_title = None

        for key, value in note_information.items():

            if "Name" in key:
                note_title = ''.join(value)

            if "Notebook" in key:
                parent_notebook = ''.join(value)

            if "Description" in key:
                description_content.append(value)

        description_string = ''.join(description_content)

        # End TODO

        ui.noteTitle_lineEdit.setText(note_title)

        from core.Models.ManageNotebook import ManageNotebooks
        model = ManageNotebooks()
        notebooks = model.get_notebooks()

        for notebook in notebooks:
            ui.selector_comboBox.addItem(notebook)
            if notebook == parent_notebook:
                ui.selector_comboBox.setCurrentText(notebook)

        ui.noteDescription_textEdit.setPlainText(description_string)

        # TODO: Retrieve the list of notebooks using the collection from the 'create note' window
        ui.selector_comboBox.setMinimumWidth(974)

        manager = ManageNote()

        from functools import partial
        save_note.triggered.connect(partial(manager.handle_changes, note_information, ui))
