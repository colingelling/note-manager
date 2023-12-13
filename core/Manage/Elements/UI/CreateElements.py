"""

    Created by Colin Gelling on 11/12/2023
    Using Pycharm Professional

"""


class CreateElements:

    notebook_manager_layout = None

    def __init__(self):
        super().__init__()

    def create_notebooks(self, notebook_information):
        set_layout = self._set_layout()
        layout = self._get_layout(set_layout)

        print(f"Layout: '{layout}'")
        print(f"Notebook that was created: '{notebook_information}'")

    @staticmethod
    def _set_layout():
        from views.Overview import Overview
        obj = Overview()
        layout = obj.layout
        return layout

    @staticmethod
    def _get_layout(layout):
        return layout
