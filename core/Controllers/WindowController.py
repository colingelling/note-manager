"""

    Created by Colin Gelling on 26/04/2023
    Using Pycharm Professional

"""


class WindowController:

    overview_instance = None

    active_window = None

    @staticmethod
    def overview_window():
        if WindowController.overview_instance is None:
            from views.Overview.view import Overview
            WindowController.overview_instance = Overview()
            WindowController.overview_instance.show()

            WindowController.active_window = WindowController.overview_instance

    @staticmethod
    def options_dialog():
        from views.Dialogs.options_dialog import OptionsDialog
        options_dialog = OptionsDialog()
        options_dialog.show()

        WindowController.active_window = options_dialog

    @staticmethod
    def create_notebook_dialog():
        from views.Dialogs.create_notebook import CreateNotebookDialog
        notebook_creation_dialog = CreateNotebookDialog()

        if WindowController.active_window:
            WindowController.active_window.hide()

        notebook_creation_dialog.show()
        WindowController.active_window = notebook_creation_dialog

    @staticmethod
    def create_note_dialog():
        from views.Dialogs.create_note import CreateNoteDialog
        note_creation_dialog = CreateNoteDialog()

        if WindowController.active_window:
            WindowController.active_window.hide()

        note_creation_dialog.show()
        WindowController.active_window = note_creation_dialog

    @staticmethod
    def opened_note_dialog(file):
        from views.Dialogs.opened_note import OpenedNote
        opened_note_dialog = OpenedNote(file)
        opened_note_dialog.show()

        WindowController.active_window = opened_note_dialog
