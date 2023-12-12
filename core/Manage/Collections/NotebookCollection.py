"""

    Created by Colin Gelling on 07/11/2023
    Using Pycharm Professional

"""

import os


class NotebookCollection:

    def __init__(self):
        super().__init__()

        self.notebook_resource = None
        self.notebook_collection = {}
        self.note_collection = {}

    def get_collection(self, notebook_selector, note_selector):
        resource_path = self._get_resource_path()

        self.notebook_collection = self._collect_notebooks(resource_path, notebook_selector)
        self._prepare_note_collection(note_selector)
        self._add_notes_into_notebook_collection()

        return self.notebook_collection

    @staticmethod
    def _get_resource_path():
        from core.Manage.Resources.NotebookResource import ManageNotebookResources
        obj = ManageNotebookResources()
        return obj.get_storage()

    def _collect_notebooks(self, resource_path, notebook_selector):
        collection = {}

        for root, dirs, files in os.walk(resource_path):
            for directory in dirs:
                notebook_path = os.path.join(resource_path, directory)

                if notebook_selector == directory or notebook_selector == '*':
                    notebook_collection = self._add_notebooks_to_collection(notebook_path, directory)
                    collection[directory] = notebook_collection

            break

        return collection

    @staticmethod
    def _add_notebooks_to_collection(notebook_path, notebook_name):
        return {
            'notebook_path': notebook_path,
            'notebook': notebook_name,
            'notes': {}
        }

    def _prepare_note_collection(self, note_selector):
        for notebook, sub_collection in self.notebook_collection.items():
            notebook_path = sub_collection.get('notebook_path', '')

            if notebook_path:
                note_information = self._collect_notes(notebook_path, note_selector)
                sub_collection['notes'] = note_information

    def _collect_notes(self, notebook_path, note_selector):
        note_collection = []

        for root, dirs, files in os.walk(notebook_path):
            for file in files:
                extension = '.txt'

                if extension in file:
                    note_path = f"{root}/{file}"
                    note = file.replace(extension, '')

                    if note_selector in file or note_selector == '*':
                        self._notes_dictionary(note_collection, note_path, note)

        return note_collection

    @staticmethod
    def _collect_notebook(notebook):
        """
        1) Filter notebooks
        2) Select notebook from notebook_collection
        3) Iterate through inner dictionary
        4) Select specific key
        5) Add the new notebook information to a dictionary
        6) Return added notebook information
        :param notebook:
        :return:
        """

        from views.Overview import Overview
        view_obj = Overview()

        for notebook_key, collection in view_obj.notebook_collection.items():
            if notebook == notebook_key:
                for key, value in collection.items():
                    if "notebook_path" in key:
                        new_notebook = {
                            "notebook": notebook,
                            "notebook_path": value
                        }

                        return new_notebook

    def set_notebook(self, notebook):
        return self._collect_notebook(notebook)

    @staticmethod
    def _notes_dictionary(note_collection, note_path, note):
        note_collection.append({
            'note_path': note_path,
            'note': note
        })

    def _add_notes_into_notebook_collection(self):
        for notebook, collection in self.notebook_collection.items():
            notes_list = collection.get('notes', [])
            notes_list.extend(self.note_collection)
            collection['notes'] = notes_list
