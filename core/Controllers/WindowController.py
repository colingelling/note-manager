"""

    Created by Colin Gelling on 26/04/2023
    Using Pycharm Professional

"""


class WindowController:

    active_window = None

    @staticmethod
    def show_home_window():
        from views.HomeView import HomeView

        if WindowController.active_window:
            WindowController.active_window.close()

        home_window = HomeView()
        home_window.show()

        WindowController.active_window = home_window
