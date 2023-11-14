"""

    Created by Colin Gelling on 06/11/2023
    Using Pycharm Professional

"""

from PyQt6.QtCore import Qt


class ShowNoteManager:

    # layout properties
    horizontal_layout_container = None
    horizontal_layout = None

    def __init__(self):
        super().__init__()

        # flag to check if layout has been created
        self.layout_created = False

        # property for the notebook manager layout element
        self.manager_layout = None

    def create_layout(self, ui):
        # create the layout only the first time
        if not self.layout_created:
            # create a layout inside the NotebookWidget
            from PyQt6 import QtWidgets
            self.manager_layout = QtWidgets.QVBoxLayout()  # Create a common layout

            # Set alignment to top
            self.manager_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

            # Create a container widget for the horizontal layout
            self.horizontal_layout_container = QtWidgets.QWidget()

            # Create the horizontal layout
            self.horizontal_layout = QtWidgets.QHBoxLayout()

            # Set the horizontal layout for the container widget
            self.horizontal_layout_container.setLayout(self.horizontal_layout)

            # Add the container widget (with the horizontal layout) to the vertical layout
            self.manager_layout.addWidget(self.horizontal_layout_container)

            # define and set the layout
            ui.NotebookWidget.setLayout(self.manager_layout)

            # alter the flag
            self.layout_created = True

            if not self.manager_layout:
                print("Layout does not exist")
