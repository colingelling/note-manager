"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QCursor
from PyQt6.QtWidgets import QMainWindow, QPushButton

from core.Controllers.WindowController import WindowController


class Overview(QMainWindow, WindowController):

    options_dialog_title = "What do you want to add?"

    # class-level variable to store the DialogCreateNotebook instance
    create_notebook_dialog = None

    new_notebook_button = None

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.setWindowTitle(f"Overview: Recent notes")

        # set stylesheet
        self.initUi()

        # flag to check if layout has been created
        self.layout_created = False

        self.notebook_layout = None

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
        Overview.options_dialog = OptionsDialogCreate()

        options_dialog = Overview.options_dialog
        options_dialog.setWindowTitle(self.options_dialog_title)

        # Check whether a layout for the notebooks exist or not
        options_dialog.add_notebook_signal.connect(self.create_notebook_layout)

        # Connect the notebook signal to the function for creating the notebook
        options_dialog.add_notebook_signal.connect(self.add_notebook)

        # Connect the notebook signal to the function for storing the notebook as a directory
        options_dialog.add_notebook_signal.connect(self.save_notebook)

        options_dialog.exec()

    def create_notebook_layout(self):
        # create the layout only the first time
        if not self.layout_created:
            # create a layout for the NotebookWidget
            from PyQt6 import QtWidgets
            self.notebook_layout = QtWidgets.QVBoxLayout()

            # define and set the layout
            ui = self.ui
            ui.NotebookWidget.setLayout(self.notebook_layout)

            # alter the flag
            self.layout_created = True

    def add_notebook(self, notebook_name):

        # Create a QPushButton with the notebook name
        self.new_notebook_button = QPushButton(notebook_name)

        # Add the button to the layout where you want to display them
        self.notebook_layout.addWidget(self.new_notebook_button)

    def save_notebook(self, notebook_name):

        if self.new_notebook_button.isWidgetType():
            print(f"The button with value '{ notebook_name }' has been found")

            import os
            notebook_directory = os.path.expanduser("~/Desktop/note-manager/notebooks/")
            os.makedirs(notebook_directory, exist_ok=True)

            # Create a directory for the notebook
            notebook_path = os.path.join(notebook_directory, notebook_name)
            os.makedirs(notebook_path, exist_ok=True)
