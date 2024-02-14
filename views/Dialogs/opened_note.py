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

        file_content = read_model.read_note(self.file_path)

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

        title_content = []
        notebook_content = []
        description_content = []

        empty_state = ''

        for element in file_content:

            splitter = '|'
            value = element.split(splitter)

            """
                 Separate 'keys' from values, values 'Title' and 'Notebook' together are one block
            """

            if "Title" in element:
                # print(f"Title: {value[1]}")
                title_content.append(value[1])
            elif "Notebook" in element:
                # print(f"Notebook: {value[1]}")
                notebook_content.append(value[1])

            """
              'Description' also is one block since the full content including special characters, spaces and additional
              values would be added
            """

            if "Description" in element:
                stripped = value[1].strip()
                description_content.append(stripped)
            elif element.strip() == empty_state:
                description_content.append('\n\n')
            else:
                description_content.append(element)

        # Remove first 4 elements from list
        title_list = ''.join(title_content)
        notebook_list = ''.join(notebook_content)
        description_list = ''.join(description_content[4:])

        self.setWindowTitle(f"Viewing note: {title_list}")

        ui.noteTitle_lineEdit.setText(title_list)
        ui.selector_comboBox.addItem(notebook_list)
        ui.noteDescription_textEdit.setPlainText(description_list)

        # TODO: Retrieve the list of notebooks using the collection from the 'create note' window
        ui.selector_comboBox.setMinimumWidth(974)

        note_path = self.file_path
        save_note.triggered.connect(lambda: ManageNote.save_note_changes(ui, note_path))
