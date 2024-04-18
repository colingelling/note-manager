"""

    Created by Colin Gelling on 20/03/2024
    Using Pycharm Professional

"""

from PyQt6.QtCore import QModelIndex, Qt
from PyQt6.QtWidgets import QTreeView

from core.Managers.TreeView.ItemManager import ItemManager


class EventManager:

    def __init__(self, tree_view, ui):
        
        self.tree_view = tree_view
        self.ui = ui

        self.hovered_index = QModelIndex()
    
    def mousePressEvent(self, event):
        # When the right mouse button has been clicked
        if event.button() == Qt.MouseButton.RightButton:
            # Get index position of the item
            index = self.tree_view.indexAt(event.pos())
            self.item_actions(index, event)
        else:
            # Return to the normal behavior
            QTreeView.mousePressEvent(self.tree_view, event)
    
    @staticmethod
    def item_actions(index, event):
        
        """
        Manage each item individually and pass the objects to the load functionality
        """
        
        if index.isValid():
            manager = ItemManager()
            manager.load(index, event)
