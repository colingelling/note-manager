"""

    Created by Colin Gelling on 30/01/2024
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QDialog, QMenuBar, QMenu, QWidget, QHBoxLayout, QSizePolicy

from functools import partial

from core.Controllers.WindowController import WindowController
from core.Managers.ManageNote import ManageNote
from core.Models.ReadNote import ReadNote


class OpenedNote(QDialog, WindowController):

    def __init__(self, file):
        super().__init__()
        self.file_path = file

        # Read file
        self.note_information = ReadNote().read(self.file_path)

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.setMinimumSize(996, 764)

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
        # TODO: This is not being updated actively, someone has to reload the window dynamically before seeing change
        for key, value in self.note_information.items():
            if "Name" in key:
                self.setWindowTitle(window_subj + ": " + value)

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

        # TODO: Out of proportion when window has been scaled to match the full size

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

        ui.noteTitle_lineEdit.setMinimumSize(955, 30)
        ui.noteDescription_textEdit.setMinimumSize(955, 562)

        ui.noteTitle_label.setText("Title")
        ui.noteTitle_label.adjustSize()

        ui.noteDescription_label.setText("Description")
        ui.noteDescription_label.adjustSize()

        # Declaration of usable information
        note_information = self.note_information
        items = ReadNote().prepared_list(note_information)

        # Set the original informational versions of the values
        ui.noteTitle_lineEdit.setText(items[0])
        ui.noteDescription_textEdit.setPlainText(items[1])

        manager = ManageNote()
        save_note.triggered.connect(partial(manager.handle_changes, note_information, ui))
        delete_note.triggered.connect(partial(manager.handle_delete, OpenedNote, note_information['filePath']))

    @staticmethod
    def close_window():
        active_window = WindowController.active_window
        active_window.close()
