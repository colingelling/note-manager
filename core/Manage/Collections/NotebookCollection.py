"""

    Created by Colin Gelling on 07/11/2023
    Using Pycharm Professional

"""

import os


class ManageNotebookCollection:

    def __init__(self):
        super().__init__()

        self.notebook_resource = None
        self.notebook_collection = {}
        self.note_collection = {}

    def get_collection(self, notebook_selector, note_selector):

        # Set resource path value
        from core.Manage.Resources.NotebookResources import ManageNotebookResources
        obj = ManageNotebookResources()
        resource_path = obj.get_storage()

        # Collect notebooks and put them in a List
        self._collect_notebooks(resource_path, notebook_selector)

        # Prepare collecting notes, pick notebook_path from notebook_collection
        self._prepare_note_collection(note_selector)

        # Put the notes in the 'notes' sub-collection of self.notebook_collection
        self._add_notes_into_notebook_collection(self.notebook_collection, self.note_collection)

        # Return the result of the entire notebook collection
        return self.notebook_collection

    def _collect_notebooks(self, resource_path, notebook_selector):

        collection = {}

        # Checkout first layer directories based on the resource (notebooks)
        for root, dirs, files in os.walk(resource_path):
            for directory in dirs:

                # Put them together
                notebook_path = os.path.join(resource_path, directory)

                # Get all notebooks or only a specific one
                if notebook_selector == directory:
                    self._add_notebooks_to_collection(collection, notebook_path, directory)
                if notebook_selector == '*':
                    self._add_notebooks_to_collection(collection, notebook_path, directory)

            # Receive only the results within the first layer of directories instead of all files too
            break

        # Define the notebook_collection as a class attribute
        self.notebook_collection = collection

        return collection

    def _prepare_note_collection(self, note_selector):
        # Collect notes and put them in a List
        for notebook, sub_collection in self.notebook_collection.items():

            # Set notebook_path because self._collect_notes needs to search from that location
            notebook_path = sub_collection.get('notebook_path', '')

            # Check if it has value
            if notebook_path:
                note_information = self._collect_notes(notebook_path, note_selector)  # Find notes based on both params
                sub_collection['notes'] = note_information

    def _collect_notes(self, notebook_path, note_selector):

        note_collection = []

        # Open the notebook path and checkout the files
        for root, dirs, files in os.walk(notebook_path):
            for file in files:
                # Remove the extension from the file value before adding it into the original collection
                extension = '.txt'
                if extension in file:
                    note_path = f"{root}/{file}"
                    note = file.replace(extension, '')
                    # Change based on the selector value
                    if note_selector in file or note_selector == '*':
                        self._notes_dictionary(note_collection, note_path, note)

        return note_collection

    @staticmethod
    def _notes_dictionary(note_collection, note_path, note):
        # Add note to the list
        note_collection.append({
            'note_path': note_path,
            'note': note
        })

    @staticmethod
    def _create_collection(notebook_path, notebook_name):
        # Create a dictionary for a notebook and notes, using the parameters
        return {
            'notebook_path': notebook_path,
            'notebook': notebook_name,
            'notes': {}  # Initialize an empty dictionary for notes
        }

    def _add_notebooks_to_collection(self, collection, notebook_path, notebook):
        # Use the values and put them into the original notebooks dictionary
        notebook_collection = self._create_collection(notebook_path, notebook)
        collection[notebook] = notebook_collection

    @staticmethod
    def _add_notes_into_notebook_collection(notebook_collection, note_collection):

        # Open the notebook collection
        for notebook, collection in notebook_collection.items():
            # Get the existing notes list or create an empty one
            notes_list = collection.get('notes', [])
            # Extend the existing notes list with the new notes
            notes_list.extend(note_collection)
            # Update the 'notes' key in the collection
            collection['notes'] = notes_list

        return notebook_collection
