"""

    Created by Colin Gelling on 27/03/2024
    Using Pycharm Professional

"""

from functools import partial

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu


class ItemManager:

    def __init__(self):
        super().__init__()
        
    def item_actions(self, event, item, data):
        
        """
        
            1) Set the context-menu
            2) Unpack the context-menu List with object references
            3) Bind List elements and methods
            4) Iterate through both Lists in order to connect with the action methods
            5) Execute the context-menu
        
        """
        
        # 1
        contextmenu_package = self._context_menu()
        
        # 2
        context_menu, delete_action, edit_action = contextmenu_package
        
        # 3
        actions = [delete_action, edit_action]
        functions = [self._item_delete, self._item_edit]
        
        # 4
        for action, function in zip(actions, functions):
            action.triggered.connect(partial(function, item, data))
            
        # 5
        context_menu.exec(event.globalPosition().toPoint())
        
    @staticmethod
    def _context_menu():
        
        """
        
            1) Create the context-menu
            2) Declare actions for the context-menu
            3) Declare custom stylesheet
            4) Set the stylesheet on the context-menu
            5) Add actions to the contextmenu
            6) Return object references as a List
        
        """
        
        # 1
        context_menu = QMenu()
        
        # 2
        delete_action = QAction("Delete")
        edit_action = QAction("Edit")
        
        # 3
        style = (""
                  "QMenu {background: #e5e5e5; color: #333; border-radius: 6px; padding: 4px 3px 6px 2px;}"
                  "QMenu::item:selected {background: #fff;}"
                "")
        
        # 4
        context_menu.setStyleSheet(style)
        
        context_menu.setCursor(Qt.CursorShape.PointingHandCursor)

        # 5
        context_menu.addAction(delete_action)
        context_menu.addAction(edit_action)
        
        # 6
        return [context_menu, delete_action, edit_action]
        
    @staticmethod
    def _item_delete(item, data):
        
        # Use the readable item and the collected data to show dialog windows
        from core.Dialogs.NotebookRemoval import NotebookRemoval
        model = NotebookRemoval()
        model.show_dialogs(item, data)
    
    @staticmethod
    def _item_edit(notebook, path):
        
        pass
        
        # TODO:
        #  1) Find out on how to spot differences between TreeView -items
        #  (Maybe comparing 'item' with data from the get_notebook_information model)
        #  2) Do nothing if the item is a note, continue when it is a notebook
        #  3) In this case, add and open a new dialog window start throwing some logic to it in order to open the
        #  notebook for being able to change the name of it
