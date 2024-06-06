"""

    Created by Colin Gelling on 21/03/2024
    Using Pycharm Professional

"""

import os

from core.Collectables.DirectoryCollector import DirectoryCollector
from core.Collectables.FileCollector import FileCollector


class NotebookCollector:
    def __init__(self):
        super().__init__()
        # self.notebook_information = {}
        #
        # self.directory_collection_template = {}
        # self.file_collection_template = {}
        #
        # self.directory_information = []
        # self.file_information = []
        self.directory_collector = DirectoryCollector()
        self.file_collector = FileCollector()
        
        self.notebook_information = {}
    
    def get_notebook_information(self, notebook_selector, note_selector):
        
        """
        3) Collect both name and path values according to file information based on directory information
        4) Check the selector values and collect only the values that match with it
        5) Translate key values and replace them with names related to notebooks and notes
        6) Return the final result of the dictionary

        """
        
        directory_collector = self.directory_collector
        file_collector = self.file_collector
        
        # Retrieve root storage path -> application storage
        from core.Manage.NotebookStorage import NotebookStorage
        handler = NotebookStorage()
        resource_path = handler.get_notebook_storage_path()
        
        # Verify existence of the root storage path and collect directory names and their path values
        if not os.path.isdir(resource_path):
            return print(f"'{resource_path}' is not a directory")
            
        directory_information = directory_collector.directory_information_collection(resource_path)
        filtered_notebook_information = directory_collector.directory_filter(directory_information, notebook_selector)
            
        file_information = file_collector.file_information_collection(filtered_notebook_information)
        filtered_note_information = file_collector.file_filter(file_information, note_selector)
        
        self._set_notebook_information(filtered_notebook_information, 'directories', 'notebooks')
        self._set_notebook_information(filtered_notebook_information, 'path_values', 'notebook_path_values')
        self._set_notebook_information(filtered_note_information, 'files', 'notes')
        self._set_notebook_information(filtered_note_information, 'path_values', 'note_path_values')
        
        if not self.notebook_information:
            return print("Something went wrong with processing the data")
            
        return self.notebook_information
    
    def _set_notebook_information(self, collection, filter_value, name):
        values = {
            key: contents for key, contents in collection.items() if f"{filter_value}" in key
        }
        
        self.notebook_information.update({name: next(iter(values.values()), [])})
            