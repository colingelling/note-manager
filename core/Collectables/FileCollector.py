"""

    Created by Colin Gelling on 04/06/2024
    Using Pycharm Professional

"""

import os


class FileCollector:
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def file_information_collection(resources):
        """
        Declare a dictionary containing lists, use the absolute path values from the main dictionary in order to get
        system-level file information, add these to the dictionary lists and return the entire dictionary
        """
        
        path_values = resources['path_values']
        
        template = {
            "files": [],
            "path_values": []
        }
        
        collection = template
        
        scanned_results = [element for value in path_values for element in os.scandir(value) if element.is_file()]
        
        # for element in os.scandir(next(iter(path_values))):
        #     print(f"element: '{element}'")
        #     if element.is_file():
        #         print(f"element is a file: '{element}'")

        # scanned_results = [element for element in os.scandir(next(iter(path_values))) if element.is_file()]
        
        for output in scanned_results:
            file = output.name
            file_path = output.path
            collection["files"].append(file)
            collection["path_values"].append(file_path)

        return collection
    
    @staticmethod
    def file_filter(collection, selector):
        
        """
          Assign usable attributes to each value type and set the matching pair based on the selector value, return the
          collection after
        """
        
        filtered_collection = {
            "files": [],
            "path_values": []
        }
        
        for note_name, note_path in zip(collection['files'], collection['path_values']):
            if note_name == selector + ".txt":
                filtered_collection['files'] = [note_name]
                filtered_collection['path_values'] = [note_path]
                return filtered_collection
            
        return collection
        
        # # Iterate through the lists associated with file names and absolute path keys simultaneously, two types of
        # # values join the iteration process and use the attributes to keep them separated
        # for notebook_name, notebook_path in collection.items():
        #     for note_name, note_path in zip(
        #             self.file_information['files'],
        #             self.file_information['path_values']
        #     ):
        #
        #         if note_name == selector:
        #             collection.clear()
        #
        #             collection['files'] = note_name
        #             collection['path_values'] = note_path
        #
        #             return collection
        #         elif selector == '*':
        #             return collection
