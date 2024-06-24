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
        
        # Declare and describe an empty collection template
        filtered_collection = {
            "files": [],
            "path_values": []
        }
        
        # print(f"FileCollector's collection: '{collection}'")
        
        # Pack two collections of values together, iterate through them and filter on particular or all values
        # and return it eventually
        for note_file, note_path in zip(collection['files'], collection['path_values']):
            if note_file == selector + ".txt":
                filtered_collection["files"] = [note_file]
                filtered_collection["path_values"] = [note_path]
                return filtered_collection
            elif selector == '*':
                return collection
            elif not selector:
                return collection.clear()
            
        return collection
