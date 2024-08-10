"""

    Created by Colin Gelling on 04/06/2024
    Using Pycharm Professional

"""

import os


class DirectoryCollector:
    def __init__(self):
        super().__init__()
        
    @staticmethod
    def directory_information_collection(source):
        
        """
        Declare a dictionary with lists and add system-level received values into those lists, eventually return the
        dictionary
        """
        
        collection = {
            "directories": [],
            "path_values": []
        }
        
        for root, dirs, files in os.walk(source):
            for directory in dirs:
                collection["directories"].append(directory)
                collection["path_values"].append(os.path.join(source, directory + "/"))
        
        return collection
    
    @staticmethod
    def directory_filter(collection, selector):
        
        """
          Assign usable attributes to each value type and set the matching pair based on the selector value, return the
          collection pair after
        """
        
        if selector == '*':
            return collection
        
        filtered_collection = {
            "directories": [],
            "path_values": []
        }
        
        for notebook_name, notebook_path in zip(collection['directories'], collection['path_values']):
            if notebook_name == selector:
                filtered_collection['directories'] = [notebook_name]
                filtered_collection['path_values'] = [notebook_path]
                return filtered_collection
            elif selector == '*':
                return collection
            elif not selector:
                return collection.clear()
        