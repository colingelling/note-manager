"""

    Created by Colin Gelling on 11/12/2023
    Using Pycharm Professional

"""

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QLabel


class ManageNotes:

    def __init__(self):
        super().__init__()

    @staticmethod
    def add_notes(manager_layout, notebook, collection):

        for notebook_key, notebook_value in collection.items():
            if 'notes' in notebook_key:
                note_collection = notebook_value
                for item in note_collection:
                    note = item['note']

                    widget = QWidget()

                    notebook_label = QLabel(note)
                    notebook_label.setStyleSheet("color: #000")
                    notebook_label.setContentsMargins(13, 0, 0, 0)

                    # Create a horizontal layout for the icon and text
                    layout = QtWidgets.QHBoxLayout()

                    layout.setContentsMargins(4, 0, 4, 0)  # Adjust the left and right margins as needed

                    # Add the label with notebook name to the layout and align it to the left
                    layout.addWidget(notebook_label)

                    widget.setLayout(layout)

                    manager_layout.addWidget(widget)

                    note_label = QLabel(note)
                    note_label.setStyleSheet("color: #000")
