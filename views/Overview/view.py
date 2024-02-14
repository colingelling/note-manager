"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QFontDatabase, QCursor
from PyQt6.QtCore import Qt

from core.Controllers.WindowController import WindowController


class Overview(QMainWindow, WindowController):

    view_name = "Overview"
    view_subject = "Manage my notebooks"

    def __init__(self):
        super().__init__()

        """
        Load resources and define window properties
        """

        self.ui = self.load_ui()

        QFontDatabase.addApplicationFont("src/gui/fonts/FontAwesome6-Free-Regular-400.otf")
        self.setWindowTitle(f"{Overview.view_name}: {Overview.view_subject}")
        self.setMinimumSize(1147, 844)

        self.load_style()

        self.show_content()

    def load_ui(self):
        from src.gui.ui.Overview.OverviewWindow import Ui_OverviewWindow
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

        ui.notebookManagerTitleLabel.setText("Manage my notes")
        ui.notebookManagerTitleLabel.adjustSize()

        plus_icon_unicode = " \uf067"

        options_btn = ui.createButton
        options_btn.setText(plus_icon_unicode)
        options_btn.setToolTip("Create options")

        options_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        options_btn.clicked.connect(WindowController.options_dialog)

        from views.Overview.components import ViewComponents
        components_obj = ViewComponents()
        components_obj.notebook_manager(ui)
        components_obj.statistics_table(ui)
