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
            
            index = self.tree_view.indexAt(event.pos())  # 1
            item_name = index.data(Qt.ItemDataRole.DisplayRole)  # 1
            
            directory_information = {name: path for name, path in self.notebook_information[0].items()}  # 2
            file_information = {name: path for name, path in self.notebook_information[1].items()}  # 2
            
            selected_directory_information = [path for path in directory_information.values() if f"/{item_name}" in path]  # 3
            selected_file_information = [path for path in file_information.values() if f"/{item_name}/" in path]  # 3
            
            # 4 - block
            collection = []
            for directory_path in selected_directory_information:
                collection.append(directory_path)
                for file_path in selected_file_information:
                    collection.append(file_path)
            
            # 5
            item_manager = ItemManager()
            item_manager.item_actions(event, item_name, collection)
            
        else:
            
            # Return to the normal behavior
            QTreeView.mousePressEvent(self.tree_view, event)
