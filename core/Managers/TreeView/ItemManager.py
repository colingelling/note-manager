"""

    Created by Colin Gelling on 27/03/2024
    Using Pycharm Professional

"""
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu


class ItemManager:

    def __init__(self):
        super().__init__()
        
    def load(self, index, event, ui):
        self._context_menu(event)
    
    @staticmethod
    def _context_menu(event):
        
        # Creating the context menu
        context_menu = QMenu()

        # Adding actions to the context menu
        action1 = QAction("Delete")
        action2 = QAction("Edit")

        # Adding action triggers
        context_menu.addAction(action1)
        context_menu.addAction(action2)

        # Executing the context menu
        context_menu.exec(event.globalPosition().toPoint())

        # TODO: Add right click menu

        # print(self.item_path)

        # if index.isValid():
        #     from core.Models.TreeView.Build import Build
        #     model = Build()
        #     menu = QMenu()
        #
        #     # Add actions to the menu
        #     action_edit = QAction("Edit", self)
        #     action_edit.triggered.connect(lambda: self.edit_item(item))
        #     menu.addAction(action_edit)
        #
        #     action_delete = QAction("Delete", self)
        #     action_delete.triggered.connect(lambda: self.delete_item(item))
        #     menu.addAction(action_delete)
        #
        #     # Show the menu at the cursor position
        #     menu.exec_(self.treeView.mapToGlobal(pos))

        # grid_layout = QGridLayout()
        # ui.treeWidget.setLayout(grid_layout)

        # for child_widget in ui.treeWidget.findChildren(QWidget):
        #     print(child_widget)
        #     if isinstance(child_widget, QVBoxLayout):
        #         print("Found layout:", child_widget)
        #         # Recursively list layouts within this layout
        #         print(ui.list_layouts(child_widget))
        #     else:
        #         widget = child_widget.objectName()
        #         print("Widget:", widget)

        # # Create QPushButton
        # button = QPushButton("Button")
        #
        # # Create QTreeWidgetItem
        # top_level_item = QTreeWidgetItem(ui.treeWidget)
        #
        # print(top_level_item)

        # # Add QPushButton as a child widget to the QTreeWidgetItem
        # top_level_item.setText(0, "Top Level Item")  # Set text for the item
        # top_level_item.addChild(QTreeWidgetItem())  # Add a child item (required for widget placement)
        # ui.treeWidget.setItemWidget(top_level_item, 0, button)  # Set the button as the widget for the item

        # layout = QHBoxLayout()
        # layout.addWidget(edit_button)
        #
        # widget = QWidget()
        # widget.setLayout(layout)
        #
        # layout.setStyleSheet("")
        #
        # ui.treeWidget.addWidget(layout)

        # # TODO: Find a way to revert back to the old idea about selecting notebooks and notes
        #
        # from core.Models.Collections.CollectNotebooks import CollectNotebooks
        # notebook_collector_model = CollectNotebooks()
        # notebooks = notebook_collector_model.get_notebooks()
        #
        # from core.Models.Collections.CollectNotes import CollectNotes
        # note_collector_model = CollectNotes()
        # notes =
        #
        # print(notebook_information)

        # TODO:
        #  1) Retrieve note_information (and declare notebook)
        #  2)

            # TODO: Import data model, add separated actions for individual notebooks/notes, like edit and delete
            #  1) Do a function call, e.g. item_actions
            #  2) Call functions inside of item_actions; item_delete, item_edit
            #  3) Find a method to pass the ui from components.py to item_delete and item_edit
            #  4) Add buttons as actions to the layout next to notebooks/notes, make them appear on hover
            #  5) The delete functionality removes the item from the list and as a directory and/or file
            #  6) Think about the edit functionality, do not include it for notes but for notebooks it could be
            #  triggered by clicking it followed by an opened dialog where someone could change the name of the
            #  notebook. When being saved, both the directory name and visual property inside the window would be
            #  changed. Do not forget to replace it in the collection of notebook information


