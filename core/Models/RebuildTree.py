"""

    Created by Colin Gelling on 23/01/2024
    Using Pycharm Professional

"""


class RebuildTree:

    def __init__(self):
        super().__init__()

    @staticmethod
    def rebuild(view):
        model = view.model()
        model.removeRows(0, model.rowCount())

        index = model.index(model.root_path)
        tree_view = model.build(index)
        tree_view.expandAll()
