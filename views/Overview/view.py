"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QFontDatabase

from core.Controllers.WindowController import WindowController


class Overview(QMainWindow, WindowController):

    view_name = "Overview"
    view_subject = "My notebooks"

    def __init__(self, view_data):
        super().__init__()

        """
        Load resources and define window properties
        """

        self.view_data = dict(view_data)

        self.ui = self.load_ui()

        QFontDatabase.addApplicationFont("src/gui/fonts/FontAwesome6-Free-Regular-400.otf")
        self.setWindowTitle(f"{Overview.view_name}: {Overview.view_subject}")
        self.setMinimumSize(1400, 844)

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

        ui.windowWidget.setMinimumSize(16777215, 844)
        ui.windowWidget.setMaximumSize(16777215, 16777215)

        ui.contentWidget.setMinimumSize(16777215, 826)
        ui.contentWidget.setMaximumSize(16777215, 16777215)

        ui.topContentWidget.setMinimumSize(16777215, 325)
        ui.topContentWidget.setMaximumSize(16777215, 325)

        ui.midContentWidget.setMinimumSize(16777215, 315)
        ui.midContentWidget.setMaximumSize(16777215, 315)

        notebook_storage_path = None

        for key, value in self.view_data.items():
            if 'notebook_storage_path' in key:
                notebook_storage_path = value

        from views.Overview.components import ViewComponents
        components_obj = ViewComponents()
        components_obj.notebook_manager(ui, notebook_storage_path)
        components_obj.activity_table(ui)
        components_obj.embedded_notes(ui)
        components_obj.notepad(ui)
