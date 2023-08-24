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
        from views.Overview import OverView

        if WindowController.active_window:
            WindowController.active_window.close()

        overview_window = OverView()
        overview_window.show()

        WindowController.active_window = overview_window
