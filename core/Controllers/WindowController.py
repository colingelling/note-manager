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
            from core.Controllers.OverviewController import OverviewController

            # Declare view object with empty view_data value
            WindowController.overview_instance = Overview('')

            # Set the view controller, overview_instance is the view object which doesn't contain the view data yet
            view_controller = OverviewController(WindowController.overview_instance)
            view_data = view_controller.processed_data()

            # Reassign the view object, this time with the view data containing something
            WindowController.overview_instance = Overview(view_data)
            WindowController.overview_instance.show()

            # Set active view status
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
