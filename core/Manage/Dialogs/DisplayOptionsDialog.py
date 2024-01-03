"""

    Created by Colin Gelling on 06/12/2023
    Using Pycharm Professional

"""


from PyQt6.QtWidgets import QMainWindow


class ShowOptionsDialog(QMainWindow):

    options_dialog_title = "What do you want to add?"

    def __init__(self):
        super().__init__()

    # @staticmethod
    def prepare_options_dialog(self):

        # Create access to the next Dialog class (view)
        from views.Dialogs.display_options import DisplayOptionsDialog
        component = DisplayOptionsDialog()

        # Set the title for the Window bound to the Dialog class
        component.setWindowTitle(ShowOptionsDialog.options_dialog_title)

        # Execute the next window Dialog
        component.exec()
