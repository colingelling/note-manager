"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QCursor
from PyQt6.QtWidgets import QMainWindow

from core.Controllers.WindowController import WindowController


class Overview(QMainWindow, WindowController):

    options_dialog_title = "What do you want to add?"

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.setWindowTitle(f"Overview: Recent notes")

        # set stylesheet
        self.initUi()

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

        self.setGeometry(467, 100, 1148, 834)  # Initial position and size of the window
        self.setFixedSize(1047, 834)  # Fixed size, don't allow the user to resize the window

        ui.TitleLabel.setText(self.windowTitle())
        ui.TitleLabel.adjustSize()

        ui.ContentWidget.setFixedWidth(1027)
        ui.ContentWidget.adjustSize()

        ui.ManageMyNotesTitleLabel.setText("Manage my notes")
        ui.ManageMyNotesTitleLabel.adjustSize()

        plus_icon_unicode = " \uf067"
        ui.OptionsDialogCreateButton.setText(plus_icon_unicode)

        ui.OptionsDialogCreateButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        ui.OptionsDialogCreateButton.clicked.connect(self.show_create_options_dialog)

        # Default group
        ui.NoteGroupLabel.setText("My first notebook")
        ui.NoteGroupLabel.adjustSize()

        # Default individual
        ui.IndividualNoteLabel.setText("My first note")
        ui.IndividualNoteLabel.adjustSize()

        ui.OverviewTable.setFixedWidth(817)

        edit_icon_unicode = "\uf044"
        ui.EditNoteGroupButton.setText(edit_icon_unicode)

        ui.EditNoteGroupButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        ui.EditNoteGroupButton.adjustSize()

        delete_icon_unicode = "\uf2ed"
        ui.DeleteNoteGroupButton.setText(delete_icon_unicode)

        ui.DeleteNoteGroupButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        ui.DeleteNoteGroupButton.adjustSize()

    def show_create_options_dialog(self):
        from views.components.OptionsDialogCreate import OptionsDialogCreate
        dialog = OptionsDialogCreate()
        dialog.setWindowTitle(self.options_dialog_title)
        dialog.exec()

    def add_note_group(self, notebook_name):
        ui = self.ui

        # Create a layout for the NotebookWidget
        from PyQt6 import QtWidgets
        notebook_layout = QtWidgets.QVBoxLayout()

        # Set the layout for the NotebookWidget
        ui.NotebookWidget.setLayout(notebook_layout)

        # Store the layout for future reference (optional)
        ui.NotebookWidgetLayout = notebook_layout

        # Set the text of NoteGroupLabel
        ui.NoteGroupLabel.setText(notebook_name)

        # If you want to adjust the size of the label (optional)
        ui.NoteGroupLabel.adjustSize()

        # Get the layout of the NotebookWidget
        notebook_layout = ui.NotebookWidgetLayout  # Use the stored layout

        # Add the NoteGroupLabel to the NotebookWidget layout
        notebook_layout.addWidget(ui.NoteGroupLabel)
