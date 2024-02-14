"""

    Created by Colin Gelling on 20/12/2023
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QVBoxLayout, QSizePolicy, QTableWidgetItem


class ViewComponents:

    tree_view = None

    def __init__(self):
        super().__init__()

        self.layout = None
        self.notebooks = None

    @staticmethod
    def notebook_manager(ui):

        """
        This method builds a TreeView on top of a predefined layout using PyQt 's models and delegates
        """

        from core.Delegates.NotebookManager import NotebookManager
        from core.Models.BuildTree import BuildTree

        root_path = "/home/colin/Desktop/note-manager/notebooks"
        tree_model = BuildTree(root_path)

        root_index = tree_model.index(tree_model.rootPath())
        tree_view = tree_model.build(root_index)

        tree_view.setModel(tree_model)
        tree_view.setRootIndex(root_index)

        tree_view.setModel(tree_model)

        # Create and attach the NotebookManager delegate
        delegate = NotebookManager()
        delegate.set_widget(tree_view)
        tree_view.setItemDelegate(delegate)

        tree_view.setStyleSheet(
            'background-color: #fff;'
            'color: #000;'
            'border: 0;'
            'margin: 0;'
            'selection-color: #000; '
            'selection-background-color: rgba(0, 0, 0, 0);'
        )

        # Bind the items from tree_view to open window functionality
        tree_view.clicked.connect(tree_model.open_note)

        # Set up the layout and parent widget
        layout = QVBoxLayout()
        parent_widget = ui.treeWidget
        layout.addWidget(tree_view)
        parent_widget.setLayout(layout)

    @staticmethod
    def statistics_table(ui):
        """
        Preparation and corrected properties # TODO
        :param ui:
        :return:
        """

        # ui.statisticsTableWidget.setMinimumSize(850, 210)

        ui.statisticsTableLabel.setGeometry(9, 18, 0, 0)
        ui.statisticsTableLabel.setText("Recent activity")
        ui.statisticsTableLabel.adjustSize()

        # Set size policy for the table view
        ui.tableWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        ui.tableWidget.setMinimumSize(850, 180)
        ui.tableWidget.setGeometry(8, 47, 0, 0)

    @staticmethod
    def placeholder(ui):
        """
        Preparation and corrected properties # TODO
        :param ui:
        :return:
        """

        pass

    @staticmethod
    def notepad(ui):
        """
        Preparation and corrected properties # TODO
        :param ui:
        :return:
        """

        pass
