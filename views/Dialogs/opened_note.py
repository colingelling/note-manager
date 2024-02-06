"""

    Created by Colin Gelling on 30/01/2024
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QDialog, QMenuBar, QMenu


class OpenedNote(QDialog):

    def __init__(self, file):
        super().__init__()
        self.file_path = file

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
        ui = self.ui

        from core.Models.ManageNote import ManageNote
        read_model = ManageNote()

        title, notebook, description = read_model.read_note_values(self.file_path)

        self.setWindowTitle(f"Viewing note: {title}")

        menubar = QMenuBar(self)

        file_menu = QMenu("Note", self)
        file_menu.addAction("Reset")
        file_menu.addAction("Save")

        menubar.addMenu(file_menu)

        ui.gridLayout.setMenuBar(menubar)

        file_menu.setStyleSheet("color: #000;")
        menubar.setStyleSheet("color: #000;")

        ui.noteTitle_lineEdit.setMinimumWidth(974)
        ui.selectorWidget.setMinimumWidth(974)
        ui.noteDescription_textEdit.resize(974, 523)

        ui.noteTitle_label.setText("Title")
        ui.noteTitle_label.adjustSize()
        ui.noteTitle_lineEdit.setText(title)
        ui.noteDescription_textEdit.setText(description)

        ui.selector_label.setText("Change the notebook")
        ui.selector_label.adjustSize()

        ui.selector_comboBox.setMinimumWidth(974)
        ui.selector_comboBox.addItem("Placeholder")

        ui.noteDescription_label.setText("Description")
        ui.noteDescription_label.adjustSize()
