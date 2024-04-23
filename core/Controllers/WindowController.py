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
            from core.Controllers.OverviewController import OverviewController
            from views.Overview.view import Overview

            # Set the view controller and collect the data for the view itself
            view_controller = OverviewController()
            view_data = view_controller.get_view_data()

            # Assign the view and fill it with the data that was collected, show it after as an application window
            WindowController.overview_instance = Overview(view_data)
            WindowController.overview_instance.show()

            # Set active view status
            WindowController.active_window = WindowController.overview_instance

    @staticmethod
    def options_dialog():
        from views.Dialogs.options_dialog import OptionsDialog
        
        view = OptionsDialog()
        view.show()

        WindowController.active_window = view

    @staticmethod
    def create_notebook_dialog():
        from views.Dialogs.create_notebook import CreateNotebookDialog
        
        view = CreateNotebookDialog()
        view.show()

        if WindowController.active_window:
            WindowController.active_window.hide()
        
        # Reassign view object
        WindowController.active_window = view

    @staticmethod
    def create_note_dialog():
        from core.Controllers.CreateNoteController import CreateNoteController
        from views.Dialogs.create_note import CreateNoteDialog

        # Set the view controller and collect the data for the view itself
        view_controller = CreateNoteController()
        view_data = view_controller.get_view_data()
        
        # Assign the view and fill it with the data that was collected, show it after as an application window
        view = CreateNoteDialog(view_data)
        view.show()
        
        # Hide (supposed to be) 'options_dialog' when it is active
        if WindowController.active_window:
            WindowController.active_window.hide()
        
        # Set active view status
        WindowController.active_window = view

    @staticmethod
    def opened_note_dialog(file):
        from core.Controllers.OpenedNoteController import OpenedNoteController
        from views.Dialogs.opened_note import OpenedNote

        # Set the view controller, overview_instance is the view object which doesn't contain the view data yet
        view_controller = OpenedNoteController(file)
        view_data = view_controller.get_view_data()

        # Reassign the view object, this time with the view data containing something
        view = OpenedNote(view_data)
        view.show()
        
        # Set active view status
        WindowController.active_window = view
