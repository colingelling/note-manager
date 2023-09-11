"""

    Created by Colin Gelling on 06/09/2023
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QDialog

from core.Controllers.WindowController import WindowController


class OptionsDialogCreate(QDialog, WindowController):

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.initUi()

        self.show_content()

    def load_ui(self):
        from src.gui.ui.management.components.OptionsDialogCreate.OptionsDialogCreate import Ui_OptionsDialogCreate
        ui = Ui_OptionsDialogCreate()
        ui.setupUi(self)

        return ui

    def initUi(self):
        with open("src/gui/css/options-dialog-create.css", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            return self.setStyleSheet(stylesheet)

    def show_content(self):
        ui = self.ui

        from views.Overview import OverView
        view = OverView()
        window_title = view.create_dialog_title

        ui.HeadlineLabel.setText(window_title)
        ui.HeadlineLabel.adjustSize()
