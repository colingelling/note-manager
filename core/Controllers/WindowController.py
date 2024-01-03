"""

    Created by Colin Gelling on 26/04/2023
    Using Pycharm Professional

"""


class WindowController:

    first_view_instance = None
    third_view_instance = None
    fourth_view_instance = None

    active_window = None

    """

        Methods support loading multiple windows between switches triggered by the user

    """

    @staticmethod
    def show_overview_window():
        if WindowController.first_view_instance is None:
            from views.Overview.view import Overview
            WindowController.first_view_instance = Overview()

        if WindowController.active_window:
            WindowController.active_window.hide()

        WindowController.first_view_instance.show()
        WindowController.active_window = WindowController.first_view_instance

    @staticmethod
    def show_create_options_dialog():
        from views.Dialogs.display_options import DisplayOptionsDialog

        dialog = DisplayOptionsDialog()
        dialog.show()

        WindowController.active_window = dialog

    @staticmethod
    def show_create_notebook_dialog():
        if WindowController.third_view_instance is None:
            from views.Dialogs.create_notebook import CreateNotebookDialog
            WindowController.third_view_instance = CreateNotebookDialog()

        WindowController.third_view_instance.show()
        WindowController.active_window = WindowController.third_view_instance

    @staticmethod
    def show_create_note_dialog():
        if WindowController.fourth_view_instance is None:
            from views.Dialogs.create_note import CreateNoteDialog
            WindowController.fourth_view_instance = CreateNoteDialog()

        WindowController.fourth_view_instance.show()
        WindowController.active_window = WindowController.fourth_view_instance
