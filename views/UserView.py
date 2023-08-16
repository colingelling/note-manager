"""

    Created by Colin Gelling on 01/01/2023
    Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow

from core.Controllers.WindowController import WindowController


class UserView(QMainWindow, WindowController):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # set layout
        self.ui = self.load_ui()

        # set navigation
        self.setup_navigation()

        # show view content
        self.content()

    def load_ui(self):
        from src.gui.ui.user.UserWindow import Ui_UserWindow
        ui = Ui_UserWindow()
        ui.setupUi(self)
        return ui

    def setup_navigation(self):

        # set ui within scope
        ui = self.ui

        user_logout = QAction("Logout", self)

        menubar = ui.menuBar
        menubar.addMenu("Settings")
        menubar.addAction(user_logout)  # TODO: Trigger logout function, return back to the HomeView

    def content(self):
        # set ui within scope
        ui = self.ui

        ui.welcomeUser.setText(f"Welcome")

        ui.userIntroductionLabel.setText("You're successfully logged in now, this area is all about showing you "
                                         "some data coming from the database behind this app.")

        ui.userDataTitleLabel.setText("Displayed user information")

        ui.userDataNameTitleLabel.setText("Name:")  # TODO: firstname, suffix + lastname
        ui.userDataCreatedLabel.setText("Account created on:")  # TODO: created_at

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()
