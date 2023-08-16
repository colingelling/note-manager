"""

    Created by Colin Gelling on 26/4/2023
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
        home_window.switch_register.connect(WindowController.show_register_window)
        home_window.switch_login.connect(WindowController.show_login_window)
        home_window.show()

        WindowController.active_window = home_window

    @staticmethod
    def show_register_window():
        from views.RegisterView import RegisterView

        if WindowController.active_window:
            WindowController.active_window.close()

        register_window = RegisterView()
        register_window.switch_home.connect(WindowController.show_home_window)
        register_window.switch_login.connect(WindowController.show_login_window)
        register_window.show()

        WindowController.active_window = register_window

    @staticmethod
    def show_login_window():
        from views.LoginView import LoginView

        if WindowController.active_window:
            WindowController.active_window.close()

        login_window = LoginView()
        login_window.switch_home.connect(WindowController.show_home_window)
        login_window.switch_register.connect(WindowController.show_register_window)
        login_window.switch_user.connect(WindowController.show_user_window)

        login_window.show()

        WindowController.active_window = login_window

    @staticmethod
    def show_user_window():
        from views.UserView import UserView

        if WindowController.active_window:
            WindowController.active_window.close()

        user_window = UserView()
        user_window.show()

        WindowController.active_window = user_window
