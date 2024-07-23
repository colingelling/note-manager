"""

    Created by Colin Gelling on 26/06/2024
    Using Pycharm Professional

"""
import os
from functools import partial

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QDialog

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

        ui.notebookNameLabel.setText("In what do you want to change the name of the notebook shown below?")
        ui.notebookNameLabel.adjustSize()
        
        original_notebook = self.view_data['notebook']
        original_notebook_path = self.view_data['notebook_path']
        
        ui.notebookName_lineEdit.setText(original_notebook)
        
        ui.saveChangesButton.setText("Save")
        ui.saveChangesButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        ui.saveChangesButton.clicked.connect(
            partial(self.edit_notebook_button, original_notebook, original_notebook_path)
        )

    def edit_notebook_button(self, original_notebook, original_notebook_path):
        ui = self.ui

        # Set text value
        new_notebook_name = ui.notebookName_lineEdit.text()
        
        original_path_value = original_notebook_path[0]
        
        if f"/{original_notebook}" in original_path_value:
            new_notebook_path = original_path_value.replace(original_notebook, new_notebook_name)
            
            if not os.listdir(original_path_value):
                os.rmdir(original_path_value)
                os.mkdir(new_notebook_path)
                
                # TODO: Fix an issue where the new_notebook_path would be replaced in notebook_information resource
                #  This because of a crash after trying to change the name in the same app instance
                #  original_path_value = original_notebook_path[0]
                #  IndexError: list index out of range
                
            else:
                print(f"Directory '{original_path_value}' is not empty, so the the path values of items inside need to "
                      f"be changed as well")
                
                # TODO: Change path of notes inside, and then change notebook path
                
                print(f"View data contains: '{self.view_data}'")
                
                # TODO: There is an issue occurring with the view_data;
                #  path values towards note files are in the same list as the notebook path

        self.close()
