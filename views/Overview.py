"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QCursor
from PyQt6.QtWidgets import QMainWindow

from core.Controllers.WindowController import WindowController


class Overview(QMainWindow, WindowController):

    notebook_collection = None

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.setWindowTitle(f"Overview: Recent notes")

        # set stylesheet
        self.initUi()

        # Check whether a layout for the notebooks and notes exist or not
        from core.Manage.Modules.Layout.NotebookDisplay.ManageLayout import ManageLayout
        obj = ManageLayout()
        self.layout = obj.create_layout(self.ui)

        self.show_content()

    def load_ui(self):
        from src.gui.ui.management.OverviewWindow import Ui_OverviewWindow
        ui = Ui_OverviewWindow()
        ui.setupUi(self)

        return ui

    def initUi(self):
        with open("src/gui/css/overview.css", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            return self.setStyleSheet(stylesheet)

    def show_content(self):

        ui = self.ui

        QFontDatabase.addApplicationFont("src/gui/fonts/FontAwesome6-Free-Regular-400.otf")

        self.setFixedSize(1047, 834)  # Fixed size, don't allow the user to resize the window

        ui.TitleLabel.setText(self.windowTitle())
        ui.TitleLabel.adjustSize()

        ui.ContentWidget.setFixedSize(1015, 834)
        ui.ContentWidget.adjustSize()

        ui.ManageMyNotesTitleLabel.setText("Manage my notes")
        ui.ManageMyNotesTitleLabel.adjustSize()

        plus_icon_unicode = " \uf067"
        ui.OptionsDialogCreateButton.setText(plus_icon_unicode)

        ui.OptionsDialogCreateButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        from core.Manage.Dialogs.ShowOptionsDialog import ShowOptionsDialog
        ui.OptionsDialogCreateButton.clicked.connect(ShowOptionsDialog.prepare_options_dialog)

        # Retrieve the notebook collection
        from core.Manage.Modules.Layout.NotebookDisplay.ManageDisplay import ManageDisplay
        obj = ManageDisplay()
        collection = obj.get_notebooks()
        self.notebook_collection = collection

        # Build the Note Manager  TODO: Temporary referring to object
        from core.Manage.Modules.Layout.NotebookDisplay.ManageNotebooks import ManageNotebooks
        obj = ManageNotebooks()
        obj.add_notebooks(self.layout, collection)

        ui.LastAddedNotesTable.setFixedWidth(817)

        ui.NotepadLabel.setText("Notepad")
        ui.NotepadLabel.adjustSize()

        ui.LastAddedNotesLabel.setText("Recent activity")
        ui.LastAddedNotesLabel.adjustSize()

        ui.widget.setStyleSheet("padding: 0.5em;")
        ui.widget.setFixedSize(400, 247)
        ui.widget.setGeometry(250, 390, 0, 100)
        ui.widget.adjustSize()

        ui.widget_2.setFixedSize(380, 247)
        ui.widget_2.adjustSize()

        ui.widget_2.setStyleSheet("padding: 0.5em;")
        ui.widget_2.setGeometry(660, 390, 0, 100)

        ui.NotepadLabel.setStyleSheet("padding: 0; margin-top: 1.2em;")
        ui.NotepadLabel.adjustSize()

        ui.NotepadtextEdit.adjustSize()
        ui.NotepadtextEdit.setStyleSheet("background: #fff; margin-top: 24px; color: #000;")
        ui.NotepadtextEdit.setFixedSize(355, 210)
