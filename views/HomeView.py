"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QMainWindow

from core.Controllers.WindowController import WindowController


class HomeView(QMainWindow, WindowController):

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

    def show_content(self):

        ui = self.ui
