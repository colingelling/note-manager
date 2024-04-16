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
            self.on_hovered_item_changed(index, event)
        else:
            # Return to the normal behavior
            QTreeView.mousePressEvent(self.tree_view, event)
            
    def mouseMoveEvent(self, event):
        hovered_index = self.tree_view.indexAt(event.pos())
        if hovered_index != self.hovered_index:  # TODO: Improve later
            self.hovered_index = hovered_index
            self.on_hovered_item_changed(self.hovered_index, event)
            
        QTreeView.mouseMoveEvent(self.tree_view, event)

    def on_hovered_item_changed(self, index, event):

        if index.isValid():
            print("Hovered item:", index.data(Qt.ItemDataRole.DisplayRole) + "\n")

            manager = ItemManager()
            manager.load(index, event, self.ui)
