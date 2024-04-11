"""

    Created by Colin Gelling on 26/03/2024
    Using Pycharm Professional

"""


class OpenedNoteController:

    def __init__(self, file, child_view):
        self.passed_note = file
        self.view_obj = child_view

        self.notebook_storage_path = None
        self.notebook_information = None

    def prepare_data(self):
        self._set_notebook_storage()
        self._set_notebook_information()

        if self.passed_note and self.notebook_information:
            # Read file
            from core.Models.ReadNote import ReadNote
            read_model = ReadNote()
            note_information = read_model.read(self.passed_note, self.notebook_information)
            return dict(note_information)

    def _set_notebook_storage(self):
        from core.Handlers.NotebookStorageHandler import NotebookStorage
        access_model = NotebookStorage()
        self.notebook_storage_path = access_model.get_notebook_storage_path()

    def _set_notebook_information(self):
        # Retrieve note informational collection
        from core.Collections.NotebookCollection import NotebookCollection
        collection_model = NotebookCollection()

        absolute_file_path = self.passed_note

        # Find the index of the last '/'
        last_slash_index = absolute_file_path.rfind('/')
        second_last_slash_index = absolute_file_path.rfind('/', 0, last_slash_index)

        # Break the 'absolute_file_path' down to the file name including extension

        file = absolute_file_path[last_slash_index + 1:]
        directory = absolute_file_path[second_last_slash_index + 1:last_slash_index]

        # Set the notebook and note, also remove the extension
        notebook = directory
        note = file.strip('.txt')

        self.notebook_information = collection_model.get_notebook_information(notebook, note)
