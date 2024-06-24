"""

    Created by Colin Gelling on 26/03/2024
    Using Pycharm Professional

"""

from pathlib import Path

from core.Collectables.NotebookCollector import NotebookCollector
from core.Manage.NotebookStorage import NotebookStorage
from core.Models.ReadNote import ReadNote


class OpenedNoteController:

    def __init__(self, file):
        self.passed_note = file

        self.notebook_storage_path = None
        
        self.notebook_information = None
        self.notebooks = None
        
        self.notebook_storage_access_model = NotebookStorage()
        self.read_model = ReadNote()

    def get_view_data(self):
        self._set_notebook_storage()
        self._set_notebook_information()
        
        model = self.read_model
        
        if not self.passed_note:
            return print("There is an issue with the note being passed as it seems not to have any value")
        
        if not self.notebook_information:
            return print("There is an issue with the retrieval of the notebook collection, currently it doesn't "
                         "contain value")
        
        note_information = model.read(self.notebook_information)
        
        data = [
            note_information,
            self.notebooks
        ]
        
        return data

    def _set_notebook_storage(self):
        model = self.notebook_storage_access_model
        self.notebook_storage_path = model.get_notebook_storage_path()

    def _set_notebook_information(self):
        # Retrieve note informational collection

        absolute_path = self.passed_note

        # Find the index of the last '/'
        last_slash_index = absolute_path.rfind('/')
        second_last_slash_index = absolute_path.rfind('/', 0, last_slash_index)

        # Break the 'absolute_file_path' down to the file name including extension
        directory = absolute_path[second_last_slash_index + 1:last_slash_index]
        
        notebook_name = directory
        note_name = Path(absolute_path).stem
        
        # Collect notebook information based on filters
        model_instance_a = NotebookCollector()
        self.notebook_information = model_instance_a.get_notebook_information(notebook_name, note_name)
        
        model_instance_b = NotebookCollector()
        self.notebooks = model_instance_b.get_notebook_information('*', '')  # still overrides line above
