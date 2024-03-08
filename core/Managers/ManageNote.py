"""

    Created by Colin Gelling on 06/03/2024
    Using Pycharm Professional

"""


class ManageNote:
    def __init__(self):
        super().__init__()

    @staticmethod
    def handle_changes(note_information, ui):
        note_title = ui.noteTitle_lineEdit.text()
        parent_notebook = ui.selector_comboBox.currentText()
        note_description = ui.noteDescription_textEdit.toPlainText()

        from core.Models.EditNote import EditNote
        model = EditNote()
        return model.save_changes(note_information, note_title, parent_notebook, note_description)
