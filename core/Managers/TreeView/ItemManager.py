"""

    Created by Colin Gelling on 27/03/2024
    Using Pycharm Professional

"""

from functools import partial

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu, QMessageBox


class ItemManager:

    def __init__(self):
        super().__init__()
        
    def load(self, index, event):
        # Dependency declaration
        contextmenu_package = self._context_menu()
        
        # Unpacking the list with object references
        context_menu, delete_action, edit_action = contextmenu_package
        
        # Declaration and binding
        actions = [delete_action, edit_action]
        functions = [self._item_delete, self._item_edit]
        
        # Iteration through both lists using one as key, the other as value in order to connect the action functions
        for action, function in zip(actions, functions):
            # TODO: Pass
            action.triggered.connect(partial(function, index.data(Qt.ItemDataRole.DisplayRole)))
            
        # Execute the menu
        context_menu.exec(event.globalPosition().toPoint())
        
    @staticmethod
    def _context_menu():
        
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
    def _item_delete(item):
        print(f"Delete action triggered on item: '{item}' \n")
        
        ItemManager.show_warning(item)
    
    @staticmethod
    def _item_edit(item):
        print(f"Edit action triggered on item: '{item}'")
        
    @staticmethod
    def show_warning(item):
        warning_box = QMessageBox()
        warning_box.setIcon(QMessageBox.Icon.Warning)
        warning_box.setText("Are you sure you want to delete this item?")
        warning_box.setInformativeText(f"You are about to delete the following item: '{item}'. \n\n"
                                       f"Are you sure? This action cannot be undone!")
        warning_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        warning_box.setDefaultButton(QMessageBox.StandardButton.No)
        
        warning_box.exec()
