"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QMainWindow

from core.Controllers.WindowController import WindowController


class OverView(QMainWindow, WindowController):

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.setWindowTitle(f"Overview: Recent notes")

        self.setup_navigation()
        self.show_content()

    def load_ui(self):
        from src.gui.ui.notes.OverviewWindow import Ui_OverviewWindow
        ui = Ui_OverviewWindow()
        ui.setupUi(self)

        with open("src/gui/css/overview.css", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            self.setStyleSheet(stylesheet)

        return ui

    def setup_navigation(self):

        ui = self.ui

    def show_content(self):

        ui = self.ui

        ui.WindowTitleLabel.setText(self.windowTitle())
        ui.WindowTitleLabel.adjustSize()
