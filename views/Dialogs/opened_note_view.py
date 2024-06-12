"""

    Created by Colin Gelling on 30/01/2024
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QDialog, QMenuBar, QMenu, QWidget, QHBoxLayout, QSizePolicy

from functools import partial

from core.Controllers.WindowController import WindowController
from core.Manage.NoteChanges import ManageNote
# from core.Models.ReadNote import ReadNote


class OpenedNoteView(QDialog, WindowController):

    file_name = ''
    file_path = ''
    parent_directory = ''
    file_content = ''

    def __init__(self, view_data):
        super().__init__()
        self.view_data = view_data

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.setMinimumSize(996, 867)

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

        # Declaration of view_data elements
        for key, value in dict(self.view_data).items():
            if key == "fileName":
                self.file_name = value
            if key == "filePath":
                self.file_path = value
            if key == "parentDirectory":
                self.parent_directory = value
            if key == "fileContent":
                self.file_content = value

        # Set window title
        # TODO: Does not update actively, window has to be refreshed manually before seeing change
        if self.file_name:
            self.setWindowTitle(window_subj + ": " + self.file_name)

        ui = self.ui

        menubar = QMenuBar(self)
        file_menu = QMenu("Actions", self)
        save_note = file_menu.addAction("Save changes")

        # TODO: Is the ability to delete going to stay here? Original plan is to make (hovered) buttons in the
        #  notebook manager on the Overview
        delete_note = file_menu.addAction("Delete the note")

        menubar.addMenu(file_menu)

        spacer_widget = QWidget()
        spacer_widget.setMinimumSize(865, 25)
        spacer_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        # TODO: Button out of proportion when window has been scaled to match the full size

        layout = QHBoxLayout()
        layout.addWidget(spacer_widget)
        layout.addWidget(menubar)
        layout.setContentsMargins(0, 0, 0, 0)

        widget = QWidget()
        widget.setLayout(layout)

        self.ui.gridLayout.addWidget(widget, 0, 0, 1, 1)

        file_menu.setStyleSheet("color: #000;")
        menubar.setStyleSheet("color: #000;")

        ui.TitleWidget.setMinimumWidth(955)
        ui.DescriptionWidget.setMinimumWidth(955)

        ui.noteTitle_lineEdit.setMinimumSize(955, 45)
        ui.noteDescription_textEdit.setMinimumSize(955, 562)

        # Filling input fields
        ui.noteTitle_lineEdit.setText(self.file_name)
        ui.noteDescription_textEdit.setPlainText(self.file_content)
        
        ui.moveNoteTitle_label.setText("Notebook")
        
        ui.moveNote_comboBox.setMinimumSize(100, 45)
        ui.moveNote_comboBox.setMaximumSize(16777215, 45)
        
        ui.moveNote_comboBox.setCurrentText(self.parent_directory)

        # TODO: Temporary, find out why indexes could be empty at first. Also why 'dict()' would be
        #  a requirement to use sometimes
        if self.view_data:
            manager = ManageNote()
            save_note.triggered.connect(partial(manager.handle_changes, self.view_data, ui))
            delete_note.triggered.connect(partial(manager.handle_delete, OpenedNoteView, self.view_data['filePath']))

    @staticmethod
    def close_window():
        active_window = WindowController.active_window
        active_window.close()
