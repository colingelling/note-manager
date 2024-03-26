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

    def mouseMoveEvent(self, event):
        hovered_index = self.tree_view.indexAt(event.pos())
        if hovered_index != self.hovered_index:
            self.hovered_index = hovered_index
            self.on_hovered_item_changed(self.hovered_index)
        QTreeView.mouseMoveEvent(self.tree_view, event)

    def on_hovered_item_changed(self, index):

        if index.isValid():
            print("Hovered item:", index.data(Qt.ItemDataRole.DisplayRole) + "\n")

            manager = ItemManager()
            manager.item_changed(index, self.ui)
