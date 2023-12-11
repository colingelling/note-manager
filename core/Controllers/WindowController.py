"""

    Created by Colin Gelling on 26/04/2023
    Using Pycharm Professional

"""


class WindowController:

    active_window = None

    """
    
        Methods support loading multiple windows between switches triggered by the user
        
    """

    @staticmethod
    def show_overview_window():
        from views.Overview import Overview

        if WindowController.active_window:
            WindowController.active_window.close()

        overview_window = Overview()
        overview_window.show()

        WindowController.active_window = overview_window

    @staticmethod
    def show_create_options_dialog():
        from views.components.OptionsDialog import OptionsDialogCreate

        if WindowController.active_window:
            WindowController.active_window.close()

        dialog_window = OptionsDialogCreate()
        dialog_window.show()

        WindowController.active_window = OptionsDialogCreate

    @staticmethod
    def show_create_notebook_dialog():
        from views.components.OptionsDialog import OptionsDialogCreate

        if WindowController.active_window:
            WindowController.active_window.close()

        dialog_window = OptionsDialogCreate()
        dialog_window.show()

        WindowController.active_window = OptionsDialogCreate
