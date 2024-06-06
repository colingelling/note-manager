"""

    Created by Colin Gelling on 20/03/2024
    Using Pycharm Professional

"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTreeView

from core.Manage.TreeView.ItemManager import ItemManager


class Events:

    def __init__(self, tree_view, notebook_information, ui):
        
        self.tree_view = tree_view
        self.ui = ui
        
        self.notebook_information = notebook_information
    
    def mousePressEvent(self, event):
        
        """
        
            1) Locate the item's index position and set the readable name
            2) Set collections containing both the item name and system-level location towards notebook directories
            3) List collections containing system-level locations towards note files
            4) Loop through both path collections and add the elements to a new List
            5) Call other functionality such as a context-menu and bound actions
        
        """
        
        if event.button() == Qt.MouseButton.RightButton:
            
            # 1
            index = self.tree_view.indexAt(event.pos())
            item_name = index.data(Qt.ItemDataRole.DisplayRole)
        
            # 2
            directory_information = [
                value for key, collection in self.notebook_information.items()
                if key == 'notebook_path_values'
                for value in collection
                if f"/{item_name}" in value
            ]
            
            file_information = [
                value for key, collection in self.notebook_information.items()
                if key == 'note_path_values'
                for value in collection
                if f"/{item_name}/" in value
            ]
    
            # 4
            collection = []
            for directory_path in directory_information:
                collection.append(directory_path)
                for file_path in file_information:
                    collection.append(file_path)

            # 5
            item_manager = ItemManager()
            item_manager.item_actions(event, item_name, collection)
            
        else:
            
            # Return to the normal behavior
            QTreeView.mousePressEvent(self.tree_view, event)
