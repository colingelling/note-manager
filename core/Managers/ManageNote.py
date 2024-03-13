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
        note_description = ui.noteDescription_textEdit.toPlainText()

        from core.Models.EditNote import EditNote
        model = EditNote()
        return model.save_changes(note_information, note_title, note_description)

    @staticmethod
    def handle_delete(obj, file):

        """

        The object 'obj' should contain a close_window() method that will close the active window, which has been set to
        OpenedNote because it's coming from the WindowController. Next the targeted file will be removed from the file
        system.

        """

        opened_note_instance = obj
        opened_note_instance.close_window()

        from core.Models.DeleteNote import DeleteNote
        model = DeleteNote()
        return model.delete(file)
