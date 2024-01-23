"""

    Created by Colin Gelling on 20/12/2023
    Using Pycharm Professional

"""

from core.Delegates.NotebookManager import NotebookManager


class ViewComponents:

    tree_view = None

    def __init__(self):
        super().__init__()

        self.layout = None
        self.notebooks = None

    def notebook_manager(self, controller, ui):

        parent_widget = ui.NotebookWidget

        from PyQt6.QtWidgets import QVBoxLayout
        layout = QVBoxLayout()

        from core.Models.BuildTree import BuildTree
        model = BuildTree()

        root_index = model.index(model.root_path)
        tree_view = model.build(root_index)

        tree_view.setModel(model)

        # Create and attach the NotebookManager delegate
        delegate = NotebookManager()
        delegate.set_widget(tree_view)
        tree_view.setItemDelegate(delegate)

        tree_view.setStyleSheet(
            'background-color: #fff; '
            'color: #000; '
            'border: 0; '
            'selection-color: #000; '
            'selection-background-color: rgba(0, 0, 0, 0);'
            )

        # Set the tree_view object
        data_obj = controller.accessible_data
        data_obj.tree_view = tree_view

        layout.addWidget(tree_view)
        parent_widget.setLayout(layout)

    @staticmethod
    def recent_activity(ui):
        """
        Preparation and corrected properties # TODO
        :param ui:
        :return:
        """

        ui.LastAddedNotesLabel.setText("Recent activity")
        ui.LastAddedNotesLabel.adjustSize()

        ui.LastAddedNotesTable.setFixedWidth(817)

    @staticmethod
    def placeholder(ui):
        """
        Preparation and corrected properties # TODO
        :param ui:
        :return:
        """

        ui.PlaceholderWidget.setStyleSheet("padding: 0.5em;")
        ui.PlaceholderWidget.setFixedSize(400, 247)
        ui.PlaceholderWidget.setGeometry(250, 390, 0, 100)
        ui.PlaceholderWidget.adjustSize()

    @staticmethod
    def notepad(ui):
        """
        Preparation and corrected properties # TODO
        :param ui:
        :return:
        """

        ui.NotepadLabel.setText("Notepad")
        ui.NotepadLabel.adjustSize()

        ui.NotepadWidget.setFixedSize(380, 247)
        ui.NotepadWidget.adjustSize()

        ui.NotepadWidget.setStyleSheet("padding: 0.5em;")
        ui.NotepadWidget.setGeometry(660, 390, 0, 100)

        ui.NotepadLabel.setStyleSheet("padding: 0; margin-top: 1.2em;")
        ui.NotepadLabel.adjustSize()

        ui.NotepadtextEdit.adjustSize()
        ui.NotepadtextEdit.setStyleSheet("background: #fff; margin-top: 24px; color: #000;")
        ui.NotepadtextEdit.setFixedSize(355, 210)
