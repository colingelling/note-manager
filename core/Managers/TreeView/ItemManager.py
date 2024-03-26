"""

    Created by Colin Gelling on 21/03/2024
    Using Pycharm Professional

"""


class ItemManager:

    def __init__(self):
        super().__init__()

    @staticmethod
    def item_changed(index, ui):

        pass

        # # TODO: Find a way to revert back to the old idea about selecting notebooks and notes
        #
        # from core.Models.Collections.CollectNotebooks import CollectNotebooks
        # notebook_collector_model = CollectNotebooks()
        # notebooks = notebook_collector_model.get_notebooks()
        #
        # from core.Models.Collections.CollectNotes import CollectNotes
        # note_collector_model = CollectNotes()
        # notes =
        #
        # print(notebook_information)

        # TODO:
        #  1) Retrieve note_information (and declare notebook)
        #  2)

            # TODO: Import data model, add separated actions for individual notebooks/notes, like edit and delete
            #  1) Do a function call, e.g. item_actions
            #  2) Call functions inside of item_actions; item_delete, item_edit
            #  3) Find a method to pass the ui from components.py to item_delete and item_edit
            #  4) Add buttons as actions to the layout next to notebooks/notes, make them appear on hover
            #  5) The delete functionality removes the item from the list and as a directory and/or file
            #  6) Think about the edit functionality, do not include it for notes but for notebooks it could be
            #  triggered by clicking it followed by an opened dialog where someone could change the name of the
            #  notebook. When being saved, both the directory name and visual property inside the window would be
            #  changed. Do not forget to replace it in the collection of notebook information


