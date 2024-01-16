"""

    Created by Colin Gelling on 26/04/2023
    Using Pycharm Professional

"""


class WindowController:

    overview_instance = None
    create_notebook_instance = None
    create_note_instance = None

    active_window = None

    """

        Methods support loading multiple windows between switches triggered by the user

    """

    @staticmethod
    def show_overview_window():
        if WindowController.overview_instance is None:
            from views.Overview.view import Overview
            WindowController.overview_instance = Overview()

        if WindowController.active_window:
            WindowController.active_window.hide()

        WindowController.overview_instance.show()
        WindowController.active_window = WindowController.overview_instance

    @staticmethod
    def show_create_options_dialog():
        from views.Dialogs.display_options import DisplayOptionsDialog

        dialog = DisplayOptionsDialog()
        dialog.show()

        WindowController.active_window = dialog

    @staticmethod
    def show_create_notebook_dialog():
        if WindowController.create_notebook_instance is None:
            from views.Dialogs.create_notebook import CreateNotebookDialog
            WindowController.create_notebook_instance = CreateNotebookDialog()

        WindowController.create_notebook_instance.show()
        WindowController.active_window = WindowController.create_notebook_instance

    @staticmethod
    def show_create_note_dialog():
        if WindowController.create_note_instance is None:
            from views.Dialogs.create_note import CreateNoteDialog
            WindowController.create_note_instance = CreateNoteDialog()

        WindowController.create_note_instance.show()
        WindowController.active_window = WindowController.create_note_instance
