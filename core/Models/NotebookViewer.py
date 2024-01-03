"""

    Created by Colin Gelling on 19/12/2023
    Using Pycharm Professional

"""
from PyQt6 import QtCore
from PyQt6.QtCore import QObject

from core.Manage.Modules.Layout.NotebookManager import NotebookManager


class NotebookViewer(QObject):

    notebooksUpdated = QtCore.pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        self.obj = NotebookManager()
        self.notebooks = None

    def set_layout(self, ui):
        obj = self.obj
        return obj.create_layout(ui)

    def build(self, layout, notebooks):
        obj = self.obj
        return obj.add_notebooks(notebooks)

    def rebuild(self, layout, notebooks):
        obj = self.obj

        # TODO:
        #  {
        #    "A notebook": {
        #      "notebook_path": "/home/colin/Desktop/note-manager/notebooks/A notebook",
        #      "notebook": "A notebook",
        #      "notes": [
        #        {
        #          "note_path": "/home/colin/Desktop/note-manager/notebooks/A notebook/Second note.txt",
        #          "note": "Second note"
        #        },
        #        {
        #          "note_path": "/home/colin/Desktop/note-manager/notebooks/A notebook/First note.txt",
        #          "note": "First note"
        #        }
        #      ]
        #    }
        #  }

        # TODO - Add the following:
        #  viewer_obj.rebuild() -> Clears the notebook manager by removing widgets, and rebuilds by executing
        #  BuildNotebooksList.add_notebooks

        # TODO:
        #  1) Check signal
        #  2) Remove existing widgets from the notebook manager
        #  3) Add notebooks to the layout (rebuild them)

        # Remove existing widgets from the layout
        # TODO: Working, directly removing everything in the notebook -manager visually -> Need to check on signal from
        #  add_notebook_button
        for widget in obj.widgets:
            obj.layout.removeWidget(widget)
            widget.deleteLater()  # Ensure proper cleanup

        # Clear the list of widgets
        obj.widgets = []

        print(f"Layout {layout}")

        # obj.add_notebooks(notebooks)  # layout issues

        # TODO: Current issue is that the layout is unavailable

        self.notebooks = notebooks
