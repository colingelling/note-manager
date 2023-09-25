"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QCursor
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel

from core.Controllers.WindowController import WindowController


class Overview(QMainWindow, WindowController):

    options_dialog_title = "What do you want to add?"

    # class-level variable to store the DialogCreateNotebook instance
    create_notebook_dialog = None

    new_notebook_label = None

    horizontal_layout_container = None

    horizontal_layout = None

    icon_label = None

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
        options_dialog.add_notebook_signal.connect(self.create_layout)

        # Connect the notebook signal to the function for creating the notebook
        options_dialog.add_notebook_signal.connect(self.add_notebook)

        # Connect the notebook signal to the function for storing the notebook as a directory
        options_dialog.add_notebook_signal.connect(self.save_notebook)

        options_dialog.exec()

    def create_layout(self):
        # create the layout only the first time
        if not self.layout_created:
            # create a layout inside the NotebookWidget
            from PyQt6 import QtWidgets
            self.notebook_layout = QtWidgets.QVBoxLayout()

            # Set alignment to top
            self.notebook_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

            # Create a container widget for the horizontal layout
            self.horizontal_layout_container = QtWidgets.QWidget()

            # Create the horizontal layout
            self.horizontal_layout = QtWidgets.QHBoxLayout()

            # Set the horizontal layout for the container widget
            self.horizontal_layout_container.setLayout(self.horizontal_layout)

            # Add the container widget (with the horizontal layout) to the vertical layout
            self.notebook_layout.addWidget(self.horizontal_layout_container)

            # define and set the layout
            ui = self.ui
            ui.NotebookWidget.setLayout(self.notebook_layout)

            # alter the flag
            self.layout_created = True

    def add_notebook(self, notebook_name):
        # Create a label with the notebook name, including HTML-style formatting
        label_text = f'<span style="font-size: 14px;">{notebook_name}</span>'

        # Create a QLabel with the formatted text
        self.new_notebook_label = QLabel(label_text)

        # Set the icon
        notebook_arrow_unicode = "\uf0da"

        # Create a QLabel for the icon
        self.icon_label = QLabel(notebook_arrow_unicode)
        self.icon_label.setStyleSheet("font-size: 8px;")

        # Create a horizontal layout for the icon and text
        layout = QtWidgets.QHBoxLayout()

        # Add the icon label to the layout and align it to the left
        layout.addWidget(self.icon_label)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Add some spacing between the icon and text
        layout.addSpacing(1)

        layout.setContentsMargins(4, 0, 4, 0)  # Adjust the left and right margins as needed

        # Add the label with notebook name to the layout and align it to the left
        layout.addWidget(self.new_notebook_label)

        # Create a QWidget to hold the layout
        container = QtWidgets.QWidget()
        container.setLayout(layout)

        # Set font style
        container.setStyleSheet("color: #000;")

        # Add the container to the layout where you want to display it
        self.notebook_layout.addWidget(container)

        # Handle mouse events for the icon_label
        self.icon_label.mousePressEvent = self.toggle_notebook_icon

    def save_notebook(self, notebook_name):

        if self.new_notebook_label.isWidgetType():
            print(f"The label with value '{ notebook_name }' has been found")

            import os
            notebook_directory = os.path.expanduser("~/Desktop/note-manager/notebooks/")
            os.makedirs(notebook_directory, exist_ok=True)

            # Create a directory for the notebook
            notebook_path = os.path.join(notebook_directory, notebook_name)
            os.makedirs(notebook_path, exist_ok=True)

    def toggle_notebook_icon(self, event):
        # Toggle the icon's orientation when the icon_label is clicked
        current_icon = self.icon_label.text()
        if current_icon == "\uf0da":
            self.icon_label.setText("\uf0d7")  # Change to a different icon (pointing down)
        else:
            self.icon_label.setText("\uf0da")  # Change back to the original icon (pointing right)
