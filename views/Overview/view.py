"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""

from PyQt6.QtGui import QFontDatabase
from PyQt6.QtWidgets import QMainWindow

from core.Controllers.WindowController import WindowController

from views.Overview.components import ViewComponents


class Overview(QMainWindow, WindowController):

    def __init__(self):
        super().__init__()

        """
        Load resources and define window properties
        """

        self.ui = self.load_ui()

        QFontDatabase.addApplicationFont("src/gui/fonts/FontAwesome6-Free-Regular-400.otf")
        self.setWindowTitle(f"Overview: Recent notes")
        self.setFixedSize(1047, 834)

        self.load_style()

        self.view_components = ViewComponents()

        self.show_content()

    def load_ui(self):
        from src.gui.ui.management.OverviewWindow import Ui_OverviewWindow
        ui = Ui_OverviewWindow()
        ui.setupUi(self)

        return ui

    def load_style(self):
        with open("src/gui/css/overview.css", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            return self.setStyleSheet(stylesheet)

    def show_content(self):

        """
        Bind the Ui that was loaded, define ViewComponents and load them individually
        :return:
        """

        ui = self.ui

        ui.ContentWidget.setFixedSize(1015, 834)
        ui.ContentWidget.adjustSize()

        ui.TitleLabel.setText(self.windowTitle())
        ui.TitleLabel.adjustSize()

        ui.ManageMyNotesTitleLabel.setText("Manage my notes")
        ui.ManageMyNotesTitleLabel.adjustSize()

        plus_icon_unicode = " \uf067"

        options_btn = ui.OptionsDialogCreateButton
        options_btn.setText(plus_icon_unicode)

        from PyQt6.QtGui import QCursor
        from PyQt6.QtCore import Qt

        options_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        obj = WindowController()

        options_btn.clicked.connect(obj.show_create_options_dialog)

        components_obj = ViewComponents()
        components_obj.notebook_manager(obj, ui)
        components_obj.recent_activity(ui)
        components_obj.notepad(ui)
        components_obj.placeholder(ui)
