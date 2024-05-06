"""

    Created by Colin Gelling on 27/03/2024
    Using Pycharm Professional

"""

import os.path
from functools import partial

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu


class ItemManager:

    def __init__(self):
        super().__init__()
        
    def item_actions(self, event, data):
        # Dependency declaration
        contextmenu_package = self._context_menu()
        
        # Unpacking the list with object references
        context_menu, delete_action, edit_action = contextmenu_package
        
        # Declaration and binding
        actions = [delete_action, edit_action]
        functions = [self._item_delete, self._item_edit]
        
        # Unpack and assign data elements
        notebook = data.get('notebook')
        notebook_path = data.get('notebook_path')
        
        # Iteration through both lists using one as key, the other as value in order to connect the action functions
        for action, function in zip(actions, functions):
            action.triggered.connect(partial(function, notebook, notebook_path))
            
        # Execute the menu
        context_menu.exec(event.globalPosition().toPoint())
        
    @staticmethod
    def _context_menu():
        
        # TODO: Context-menu not working on and when new notebook(s) has been created in the same window instance
        
        # Creating the context menu
        context_menu = QMenu()
        
        # Declaring actions (will appear in the contextmenu)
        delete_action = QAction("Delete")
        edit_action = QAction("Edit")

        # Adding actions to the contextmenu
        context_menu.addAction(delete_action)
        context_menu.addAction(edit_action)
        
        # Return object references as a list
        return [context_menu, delete_action, edit_action]
        
    @staticmethod
    def _item_delete(notebook, path):
        print(f"Delete action triggered on item: '{notebook}' \n")
        
        from core.Dialogs.NotebookRemoval import NotebookRemoval
        model = NotebookRemoval()
        
        warn = model.show_warning(notebook)
        
        if not warn:
            return print("An error occurred, please try again")
        
        if os.path.isdir(path):
            directory_content = [os.path.join(root, file) for root, dirs, files in os.walk(path) for file in files]
            
            if directory_content:
                print("Directory is not empty, delete the files first before trying again")
                # TODO: Return tiny dialog with an 'OK' button
                model.show_error()
            else:
                # TODO: has an issue with removing the last directory, also deletes the actual
                #  'notebooks' directory. QTreeView would show project-files from this point
                os.rmdir(path)
                
        # TODO:
        #  1) Find out on how to spot differences between TreeView -items
        #  (Maybe comparing 'item' with data from the get_notebook_information model)
        #  2) Do nothing if the item is a note, continue when it is a notebook
        #  (Expand on the warning dialog, add delete functionality behind the 'Yes' button)
        #  3) Maybe include notes later
    
    @staticmethod
    def _item_edit(notebook, path):
        print(f"Edit action triggered on item: '{notebook}'")
        
        # TODO:
        #  1) Find out on how to spot differences between TreeView -items
        #  (Maybe comparing 'item' with data from the get_notebook_information model)
        #  2) Do nothing if the item is a note, continue when it is a notebook
        #  3) In this case, add and open a new dialog window start throwing some logic to it in order to open the
        #  notebook for being able to change the name of it
