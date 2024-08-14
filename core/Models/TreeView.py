"""

    Created by Colin Gelling on 16/01/2024
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QTreeView


class TreeView:

    def __init__(self, root_path):
        super(TreeView, self).__init__()

        self.root_path = root_path

        self.tree_view = None
        self.index_model = None

    def build(self, root_index):
        from core.Manage.TreeView.DataHandler import DataHandler
        data_model = DataHandler(self.root_path)

        # Instantiate QTreeView and set the data onto it
        self.tree_view = QTreeView()
        self.tree_view.setModel(data_model)
        
        data_model.layoutChanged.connect(self.layoutChanged)
        data_model.layoutChanged.emit()

        # Customize default fields, columns and rows
        self.customize_tree(self.tree_view)

        return self.tree_view

    def layoutChanged(self):
        print("hoi")
        
    @staticmethod
    def customize_tree(tree):
        # Hide column names
        header = tree.header()
        header.setSectionHidden(0, False)
        header.setSectionHidden(1, True)
        header.setSectionHidden(2, True)
        header.setSectionHidden(3, True)

        # Hide column-headers
        return header.hide()
