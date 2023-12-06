"""

    Created by Colin Gelling on 06/12/2023
    Using Pycharm Professional

"""


from PyQt6.QtWidgets import QMainWindow


class CreatingOptions(QMainWindow):

    options_dialog_title = "What do you want to add?"

    def __init__(self):
        super().__init__()

    @staticmethod
    def show_create_options_dialog():

        # Create access to the next Dialog class (view)
        from views.components.OptionsDialogCreate import OptionsDialogCreate
        # from views.Overview import Overview
        component = OptionsDialogCreate()

        # Set the title for the Window bound to the Dialog class
        component.setWindowTitle(CreatingOptions.options_dialog_title)

        # Connect the notebook signal to the function for storing the notebook as a directory
        from core.Modules.Storage.FolderCreation import FolderCreation
        obj = FolderCreation()
        component.add_notebook_signal.connect(obj.save_notebook)

        # Connect the note signal to the function for storing the notebook as a directory
        from core.Modules.Storage.FileCreation import FileCreation
        obj = FileCreation()
        component.add_note_signal.connect(obj.save_note)

        # Execute the next window Dialog
        component.exec()
