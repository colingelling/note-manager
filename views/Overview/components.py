"""

    Created by Colin Gelling on 20/12/2023
    Using Pycharm Professional

"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QVBoxLayout


class ViewComponents:

    tree_view = None

    def __init__(self):
        super().__init__()

        self.layout = None
        self.notebooks = None

    @staticmethod
    def notebook_manager(ui, resource):

        """
        This method builds a TreeView on top of a predefined layout using PyQt 's models and delegates
        """

        ui.notebookManagerWidget.setMinimumSize(400, 600)

        ui.notebookManagerHeaderWidget.setMinimumSize(395, 40)
        ui.notebookManagerHeaderWidget.setMaximumSize(395, 40)

        ui.notebookManagerTitleLabel.setText("Manage my notes")
        ui.notebookManagerTitleLabel.adjustSize()

        plus_icon_unicode = " \uf067"

        options_btn = ui.createButton
        options_btn.setText(plus_icon_unicode)
        options_btn.setToolTip("Create")

        options_btn.setGeometry(335, 5, 51, 31)

        options_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # TODO: Maybe let the controller handle this type of situations?
        from core.Controllers.WindowController import WindowController
        options_btn.clicked.connect(WindowController.options_dialog)

        # TODO: Next thing to do is to rebuild notebook_information using selector functionality like last year

        from core.Delegates.NotebookManager import NotebookManager
        from core.Models.TreeView.Build import Build

        tree_model = Build(resource)

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

        # Declare event handler
        from core.Managers.TreeView.EventManager import EventManager
        manager = EventManager(tree_view, ui)
        tree_view.setMouseTracking(True)
        tree_view.mouseMoveEvent = manager.mouseMoveEvent

        # Bind the items from tree_view to open window functionality
        tree_view.clicked.connect(tree_model.open_note)

        # Set up the layout and parent widget
        layout = QVBoxLayout()
        parent_widget = ui.treeWidget
        layout.addWidget(tree_view)
        parent_widget.setLayout(layout)

    @staticmethod
    def activity_table(ui):
        """
        Preparation and corrected properties # TODO
        :param ui:
        :return:
        """

        ui.activityTableLabel.setText("Recent activity")
        ui.activityTableLabel.adjustSize()

        ui.activityTableWidget.setMinimumSize(16777215, 264)
        ui.activityTableWidget.setMaximumSize(16777215, 16777215)

        ui.activityTable.setMinimumSize(16777215, 264)
        ui.activityTable.setMaximumSize(16777215, 264)

    @staticmethod
    def embedded_notes(ui):
        """
        Preparation and corrected properties # TODO
        :param ui:
        :return:
        """

        ui.embeddedNotesWidget.setMinimumSize(467, 300)
        ui.embeddedNotesWidget.setMaximumSize(16777215, 300)

    @staticmethod
    def notepad(ui):
        """
        Preparation and corrected properties # TODO
        :param ui:
        :return:
        """

        ui.embeddedNotesLabel.setText("Embedded notes")

        ui.notepadWidget.setMinimumSize(467, 300)
        ui.notepadWidget.setMaximumSize(16777215, 300)

        ui.notepad_textEdit.setPlaceholderText(
            "This is the notepad, you can type here (and it will be saved automatically)"
        )
