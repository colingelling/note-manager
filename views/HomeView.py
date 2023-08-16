"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow

from core.Controllers.WindowController import WindowController


class HomeView(QMainWindow, WindowController):

    switch_home = QtCore.pyqtSignal()
    switch_register = QtCore.pyqtSignal()
    switch_login = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.setWindowTitle(f"Home")

        self.setup_navigation()
        self.show_content()

    def load_ui(self):
        from src.gui.ui.home.HomeWindow import Ui_HomeWindow
        ui = Ui_HomeWindow()
        ui.setupUi(self)
        return ui

    def setup_navigation(self):

        ui = self.ui

        button_home = QAction("Home", self)
        button_register = QAction("Register", self)
        button_login = QAction("Login", self)

        # noinspection PyUnresolvedReferences
        button_home.triggered.connect(self.switch_home_window)
        # noinspection PyUnresolvedReferences
        button_register.triggered.connect(self.switch_register_window)
        # noinspection PyUnresolvedReferences
        button_login.triggered.connect(self.switch_login_window)

        menubar = ui.menuBar
        menubar.addAction(button_home)
        menubar.addAction(button_register)
        menubar.addAction(button_login)

    def show_content(self):

        ui = self.ui

        # Begin: tab widget (tab 1)

        first_tab_headline = 'Welcome'

        ui.tabWidget.setTabText(0, first_tab_headline)

        # Same thing for this, prevent cutting the label/add dynamic length according to text
        ui.homeIntroTitleFrameTab_1.adjustSize()

        # Divide the text over multiple lines instead of one limited by an x amount of characters
        ui.homeIntroLongTextTab_1.setMinimumWidth(600)
        ui.homeIntroLongTextTab_1.setWordWrap(1)
        ui.homeIntroLongTextTab_1.setText(
            "This application is a practice program in order to learn the Python language including OOP terms and most "
            "of all knowing what to do with PyQt6."
            "This application serves the ability to register an account whether you can sign in afterwards."
        )

        ui.homeIntroLongTextTab_1.adjustSize()

        # End: tab widget (tab 1)

        # Begin: tab widget (tab 2)
        # Also the following block has the same rules as the code described above this text

        second_tab_headline = 'Application language information'
        ui.tabWidget.setTabText(1, second_tab_headline)

        ui.homeIntroTitleFrameTab_2.adjustSize()

        ui.homeIntroLongTextTab_2.setMinimumWidth(600)
        ui.homeIntroLongTextTab_2.setWordWrap(1)
        ui.homeIntroLongTextTab_2.setText(
            "This program is made with Python and the PyQt(6) library. The elements are put in by using Qt Designer,"
            "which is a UI element addition application itself. This stores .ui files per window, and these are "
            "converted in the background as .py files because of the fact that it is easier to work with."
        )

        ui.homeIntroLongTextTab_2.adjustSize()

        # End: tab widget (tab 2)

    def switch_home_window(self):
        self.switch_home.emit()

    def switch_register_window(self):
        self.switch_register.emit()

    def switch_login_window(self):
        self.switch_login.emit()
