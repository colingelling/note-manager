"""

    Created by Colin Gelling on 26/06/2024
    Using Pycharm Professional

"""
import os
import shutil
from functools import partial

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QDialog
from PyQt6.uic.properties import QtCore

from core.Controllers.WindowController import WindowController


class EditNotebookView(QDialog, WindowController):

    def __init__(self, data):
        super().__init__()
        
        self.view_data = data

        self.ui = self.load_ui()

        self.window_title = "Editing a notebook"
        self.setWindowTitle(self.window_title)

        self.setFixedSize(800, 186)

        self.load_style()

        self.show_content()

    def load_ui(self):
        from src.gui.ui.dialogs.DialogEditNotebook.DialogEditNotebook import Ui_DialogEditNotebook
        ui = Ui_DialogEditNotebook()
        ui.setupUi(self)

        return ui

    def load_style(self):
        with open("src/gui/css/dialog-edit-notebook.css", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            return self.setStyleSheet(stylesheet)

    def show_content(self):
        ui = self.ui

        ui.titleWidget.setMaximumSize(744, 144)
        ui.editorWidget.setMaximumSize(744, 144)

        ui.headlineLabel.setText(self.window_title)
        ui.headlineLabel.adjustSize()
        
        print(f"View data: '{self.view_data}'")

        ui.notebookNameLabel.setText("In what do you want to change the name of the notebook shown below?")
        ui.notebookNameLabel.adjustSize()
        
        original_notebook_value = self.view_data['directory']
        original_notebook_path_value = self.view_data['directory_path_value']  # TODO: Returned to be empty
        original_file_path_values = self.view_data['file_path_values']
        
        ui.notebookName_lineEdit.setText(original_notebook_value)
        
        ui.saveChangesButton.setText("Save")
        ui.saveChangesButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        ui.saveChangesButton.clicked.connect(
            partial(self.edit_notebook_button, original_notebook_value, original_notebook_path_value, original_file_path_values)
        )

    def edit_notebook_button(self, notebook, notebook_path, file_path_values):
        
        # print(f"notebook value: '{notebook}', notebook_path value: '{notebook_path}', 'file_path_values: '{file_path_values}'")
        
        ui = self.ui
        
        # TODO: Split the following into these parts:
        #  1) Preparing data and updating values
        #  2) Handling the action; changing directory by creating, moving notes if there are any and finally removing
        
        new_notebook_name = ui.notebookName_lineEdit.text()
        
        new_notebook_path_value = None
        new_note_path_values = None
        
        if not notebook_path:
            return print("Original notebook path value has returned to be empty.")
        
        # TODO: Fix empty on second attempt within same window instance
        print(f"notebook_path: '{notebook_path}'")  # Appearing as '/'
        
        if f"/{notebook}" in notebook_path:
            path = notebook_path
            new_notebook_path = path.replace(notebook, new_notebook_name)

            if not os.listdir(notebook_path):
                os.rmdir(notebook_path)
                os.mkdir(new_notebook_path)
        #
        #         # TODO: Fix an issue where the new_notebook_path would be replaced in notebook_information resource
        #         #  This because of a crash after trying to change the name in the same app instance
        #         #  original_path_value = original_notebook_path[0]
        #         #  IndexError: list index out of range
        #
            else:
                print(f"Directory '{notebook_path}' is not empty, so the the path values of items inside need "
                      f"to be changed as well")

                path = notebook_path
                new_notebook_path_value = path.replace(
                    f"/{notebook}", f"/{new_notebook_name}"
                )

                print(f"new_notebook_path_value: '{new_notebook_path_value}'")  # passed successfully
        #
                new_note_path_values = [
                    value.replace(f"/{notebook}/", f"/{new_notebook_name}/")
                    for value in file_path_values
                ]

                print(f"New note path values: '{new_note_path_values}'")  # passed successfully

                # Create a directory containing the changed name
                os.mkdir(new_notebook_path_value)
                
                # TODO: It is possible to repeat the actions several times on the same item, but not on new ones at this
                #  stage because it wasn't pushed into the notebook information collection
        #
        #         # if os.path.isdir(new_notebook_path_value):
        #         #     self.view_data['notebook_path'] = new_notebook_path_value
        #
        #         print(f"self.view_data['notebook_path'] has been updated to: '{notebook_path}'")
        # #
        # #             self.view_data['notebook_path'][0] = new_notebook_path_value
        # #
                # Collect files from the old directory
                files = [
                    os.path.join(notebook_path, file_name)
                    for file_name in os.listdir(notebook_path)
                ]

                # Move the files from the old directory into the new one
                for file in files:
                    shutil.move(file, new_notebook_path_value)

                # Cleanup, delete the old directory
                if os.path.isdir(notebook_path):
                    os.removedirs(notebook_path)

                # # TODO: Update Overview's notebook_information
                # from views.Overview.view import Overview
                # Overview.notebook_information.update()
                
                
        
        #         print("-----------------------------------------------------------------------------")
        # else:
        #     print(f"Notebook path value has been changed, so it returned empty in the other statement block: '{notebook_path}'")
        
        self.close()
