"""

    Created by Colin Gelling on 20/12/2023
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QVBoxLayout


class ViewComponents:

    tree_view = None

    def __init__(self):
        super().__init__()

        self.layout = None
        self.notebooks = None

    def notebook_manager(self, ui):

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
            'background-color: #fff; '
            'color: #000; '
            'border: 0; '
            'selection-color: #000; '
            'selection-background-color: rgba(0, 0, 0, 0);'
        )

        # Bind the items from tree_view to open window functionality
        tree_view.clicked.connect(tree_model.open_note)

        # Set up the layout and parent widget
        layout = QVBoxLayout()
        parent_widget = ui.NotebookWidget
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
