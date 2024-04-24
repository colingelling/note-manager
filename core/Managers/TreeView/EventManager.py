"""

    Created by Colin Gelling on 20/03/2024
    Using Pycharm Professional

"""

from PyQt6.QtCore import QModelIndex, Qt
from PyQt6.QtWidgets import QTreeView

from core.Managers.TreeView.ItemManager import ItemManager


class EventManager:

    def __init__(self, tree_view, notebook_information, ui):
        
        self.tree_view = tree_view
        self.ui = ui
        
        self.notebook_information = notebook_information
    
    def mousePressEvent(self, event):
        # When the right mouse button has been clicked
        if event.button() == Qt.MouseButton.RightButton:
            # Get index position of the item
            index = self.tree_view.indexAt(event.pos())
            item_name = index.data(Qt.ItemDataRole.DisplayRole)
            
            for collection in self.notebook_information:
                for key, value in collection.items():
                    if not value.endswith('.txt') and key == item_name:
                        data = {
                            "notebook": key,
                            "notebook_path": value
                        }
            
                        item_manager = ItemManager()
                        item_manager.item_actions(event, data)
        else:
            # Return to the normal behavior
            QTreeView.mousePressEvent(self.tree_view, event)
