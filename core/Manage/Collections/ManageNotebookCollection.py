"""

    Created by Colin Gelling on 07/11/2023
    Using Pycharm Professional

"""

import os

from core.app_information import AppInformation


class ManageNotebookCollection:

    resource_path = None

    def __init__(self):
        super().__init__()

        self.notebook_resource = None
        self.notebook_collection = {}
        self.note_collection = []

    def get_collection(self, notebook_selector, note_selector):

        # Set resource path value
        self._set_resource_path()
        resource_path = self._get_resource_path()

        # Collect notebooks and put them in a List
        self._collect_notebooks(resource_path, notebook_selector)

        # Prepare collecting notes, pick notebook_path from notebook_collection
        self._prepare_note_collection(note_selector)

        # Put the notes in the 'notes' sub-collection of self.notebook_collection
        self._add_notes_into_notebook_collection(self.notebook_collection, self.note_collection)

        # Return notebook collection with the final result of having note values
        print(self.notebook_collection)

        # TODO: Find out if it would be better to change the notes nested list into a dictionary also in order to
        #  include the path towards a note in there

        """
          Like this:
          note_path: note/path,
          note: note
        """

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
            notebook_path = sub_collection['notebook_path']

            # Check if it has value
            if notebook_path:
                self._collect_notes(notebook_path, note_selector)  # Find notes based on both params

    def _collect_notes(self, notebook_path, note_selector):

        note_collection = []

        # Open the notebook path and checkout the files
        for root, dirs, files in os.walk(notebook_path):
            for file in files:
                # Remove the extension from the file value before adding it into the original collection
                extension = '.txt'
                if extension in file:
                    note = file.replace(extension, '')
                    # Change based on the selector value
                    if note_selector in file:
                        self._list_notes(note_collection, note)
                    if note_selector == '*':
                        self._list_notes(note_collection, note)

        # Define the note_collection as a class attribute
        self.note_collection = note_collection

        return note_collection

    @staticmethod
    def _list_notes(note_collection, note):
        # Add note to the list
        note_collection.append([
            note
        ])

    @staticmethod
    def _create_collection(notebook_path, notebook_name):
        # Create a dictionary for a notebook and notes, using the parameters
        return {
            'notebook_path': notebook_path,
            'notebook': notebook_name,
            'notes': []  # Initialize an empty dictionary for notes
        }

    def _add_notebooks_to_collection(self, collection, notebook_path, notebook):
        # Use the values and put them into the original notebooks dictionary
        notebook_collection = self._create_collection(notebook_path, notebook)
        collection[notebook] = notebook_collection

    @staticmethod
    def _add_notes_into_notebook_collection(notebook_collection, note_collection):

        # Open the notebook collection
        for notebook, collection in notebook_collection.items():

            notes_list = collection.get('notes', [])  # Get the existing notes list or create an empty one
            for note in note_collection:
                notes_list.extend(note)  # Put the note(s) that were found into the 'empty' list

            collection['notes'] = notes_list  # Update the 'notes' key in the collection

            return collection

    @staticmethod
    def _storage_path():  # TODO: Move to another location later
        # Retrieve storage path value and return it
        obj = AppInformation()
        storage = os.path.abspath(obj.application_storage())
        return storage

    def _set_resource_path(self):
        resource = 'notebooks'
        self.resource_path = f"{self._storage_path()}/{resource}"

    def _get_resource_path(self):
        return self.resource_path
