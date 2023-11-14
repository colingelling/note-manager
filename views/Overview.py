"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""

import os

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QCursor
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel

from core.Controllers.WindowController import WindowController


class Overview(QMainWindow, WindowController):

    options_dialog_title = "What do you want to add?"

    # class-level variable to store the DialogCreateNotebook instance
    create_notebook_dialog = None

    # label properties
    icon_label = None
    notebook_label = None
    note_label = None

    # # layout properties
    # horizontal_layout_container = None
    # horizontal_layout = None

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.setWindowTitle(f"Overview: Recent notes")

        # set stylesheet
        self.initUi()

        # # flag to check if layout has been created
        # self.layout_created = False

        # self.manager_layout = None

        # Check whether a layout for the notebooks and notes exist or not
        from core.Modules.Layout.ShowNoteManager import ShowNoteManager
        ui = self.ui
        note_manager = ShowNoteManager()
        note_manager.create_layout(ui)

        from core.Manage.Collections.ManageDirectoryCollections import ManageDirectoryCollections
        collection = ManageDirectoryCollections()

        # TODO: List all notebooks and files
        collection.directory_finder('notebooks', '*')

        # print(collection.notebook_collection)
        # TODO: This is outside the loop from the function above
        # print(collection.notebook_collection)  # TODO: Only shows one result

        # TODO: Specifying source and target file (handy for edit purposes)
        # source_path = collection.directory_finder('notebooks', 'A notebook')
        #
        # collection.file_finder(source_path, 'txt')
        #
        # if collection.content:
        #     for pair in collection.content.items():
        #         print(pair)
        #         for value in pair:
        #             print(value)

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

        # self.setGeometry(467, 100, 1148, 834)  # Initial position and size of the window
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
        ui.OptionsDialogCreateButton.clicked.connect(self.show_create_options_dialog)

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

    def show_create_options_dialog(self):
        # Create access to the next Dialog class (view)
        from views.components.OptionsDialogCreate import OptionsDialogCreate
        Overview.options_dialog = OptionsDialogCreate()

        # Shorter variable
        options_dialog = Overview.options_dialog

        # Set the title for the Window bound to the Dialog class
        options_dialog.setWindowTitle(self.options_dialog_title)

        # Connect the notebook signal to the function for storing the notebook as a directory
        options_dialog.add_notebook_signal.connect(self.save_notebook)

        # Connect the note signal to the function for storing the notebook as a directory
        options_dialog.add_note_signal.connect(self.save_note)

        # Execute the next window Dialog
        options_dialog.exec()



    def save_notebook(self, notebook_title):

        from core.app_information import AppInformation
        app_information = AppInformation()
        root_folder = app_information.application_storage()

        notebook_directory = "notebooks"

        import os
        notebook_destination = os.path.expanduser(f"{root_folder}/{notebook_directory}")
        os.makedirs(notebook_destination, exist_ok=True)

        # Create a directory for the notebook
        notebook_path = os.path.join(notebook_destination, notebook_title)
        os.makedirs(notebook_path, exist_ok=True)

        print(f"Notebook saved to: '{notebook_path}'")

    def save_note(self, new_note):

        """
        Set the fundamental ground with the help of specific information for storing the note, extract note data from
        the signal slot following by creating the note file according to a template.
        :param new_note:
        :return:
        """

        # Get access to the application information -class
        from core.app_information import AppInformation
        app_information = AppInformation()

        # Retrieve the application storage path
        app_storage = app_information.application_storage()

        # Verify existence
        if not app_storage:
            return print("An issue has appeared which caused that the application storage folder could not be created!")

        # Set base path value
        import os
        notebook_destination = os.path.expanduser(f"{app_storage}/notebooks")
        os.makedirs(notebook_destination, exist_ok=True)

        # Convert string from signal back into usable Dictionary format
        import json
        note_dict = json.loads(new_note)

        # Retrieve the selected notebook value
        notebook = note_dict["Notebook"]

        # Set the directory value according to the selected notebook value
        notebook_directory = notebook

        # Final destination of the note that was created should be in 'notebook_destination/notebook/'
        note_path = f"{notebook_destination}/{notebook_directory}"  # TODO: The '/' is a duplicate

        # Retrieve other data from the signal
        title = note_dict["Title"]
        description = note_dict["Description"]

        # Declare a filename based on the note title
        filename = f"{title}.txt"

        # Set full path to the note file
        note_file_path = os.path.join(note_path, filename)

        # Content for the note, including the title, notebook, and description
        note_template = f"Title: {title}\nNotebook: {notebook}\nDescription: {description}\n"

        # Create the note file and fill it with the template
        with open(note_file_path, "w") as note_file:
            note_file.write(note_template)

        print(f"Note saved to: '{note_file_path}'")
