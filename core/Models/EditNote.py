"""

    Created by Colin Gelling on 31/01/2024
    Using Pycharm Professional

"""

import os

from PyQt6.QtGui import QFileSystemModel


class EditNote(QFileSystemModel):

    def __init__(self, parent=None):
        super(EditNote, self).__init__(parent)

        self.file_path = None

    def save_changes(self, obj, data, title, parent_notebook, description):
        
        # Extract data set
        unpacked_data = {key: value for collection in data for key, value in collection.items()}

        # Declare data values as properties
        file_path = unpacked_data['filePath']
        file_name = unpacked_data['fileName']
        parent_directory = unpacked_data['parentDirectory']
        file_content = unpacked_data['fileContent']

        # Verify that the main dictionary's fileName matches to the original name of the note being opened, then replace
        # the original with the new value
        if file_name is not title:
            unpacked_data.update({
                'fileName': title
            })
        
        old_file_path = file_path
            
        if parent_notebook is not parent_directory:
            
            unpacked_data.update({
                'parentDirectory': parent_notebook
            })
            
            if f"/{parent_notebook}/" not in file_path:
                new_file_path = old_file_path.replace(f"/{parent_directory}/", f"/{parent_notebook}/")
                unpacked_data.update({'filePath': new_file_path})
        
        path_data = {
            'old_file_path': old_file_path,
            'new_file_path': unpacked_data['filePath']
        }

        # Prepare the file values 'absolute path' of both the temporarily saved copy of the original and the new file
        updated_files = self._prepare_updated_files(path_data, file_name, title)

        temporary_file = None
        updated_file = None

        # Assigning values from dictionary (updated_files) in order to use them
        for key, value in updated_files.items():
            if key == 'temp_file':
                temporary_file = value
            if key == 'updated_file':
                updated_file = value

        # Update the main dictionary, add the temporary
        for key, value in unpacked_data.items():
            if key == 'filePath' and value == file_path:
                unpacked_data.update({
                    'filePath': updated_file
                })

        # Store the description content in the main dictionary
        unpacked_data.update({
            'fileContent': description
        })

        # Make a backup of the original file
        self._make_temporary_note(old_file_path, temporary_file)

        # Set the file template containing the content description for the new file
        file_template = ''.join(title + "\n\n" + description)

        # Verify that the creation of temporary_file has been succeeded. When true, create a new file in order to
        # replace the original but with correct values
        if os.path.exists(temporary_file):
            self._make_new_note(updated_file, file_template)
        else:
            message = "Application closed due to an issue where the backup of the original file did not succeed."
            exit(message)  # TODO: Refer to a popup dialog displaying the text above

        # Verify that the new file version has been created. If true, the temporarily saved copy of the original
        # will be removed
        if os.path.exists(updated_file):
            # We do not need the temporarily stored file anymore
            from core.Models.DeleteNote import DeleteNote
            model = DeleteNote()
            model.delete(temporary_file)
        else:
            # Revert changes
            self._revert_backup(temporary_file, file_path)
        
        # Whenever the parent notebook has been set to change, close the window after task completion
        if parent_notebook is not parent_directory:
            return obj.close_window()

    def _prepare_updated_files(self, data, file_name, updated_title):

        """
        Prepare both the temporarily stored file as a copy of the original file and the new file based on the changed
        values, the file values are in absolute path format.
        """
        
        old_path = data['old_file_path']
        new_path = data['new_file_path']

        temporary_file = self._prepare_temporary_note(old_path, file_name)
        updated_file = self._prepare_new_note(new_path, file_name, updated_title)

        return {'temp_file': temporary_file, 'updated_file': updated_file}

    @staticmethod
    def _prepare_temporary_note(file, name):

        """
        Return the temporary note file value
        """

        return file.replace(name + '.txt', '.' + name + '.tmp.txt')

    @staticmethod
    def _make_temporary_note(original_file, temporary_file):

        """
        Return and rename the original file to match the value of temporary file on system-level
        """

        return os.rename(original_file, temporary_file)

    @staticmethod
    def _prepare_new_note(original_path, original_name, updated_name):

        """
        Declare and return the newer version of the note file
        """

        file_extension = ".txt"

        original_file = original_name + file_extension
        new_file = updated_name + file_extension

        return original_path.replace(original_file, new_file)

    @staticmethod
    def _make_new_note(file_path, file_template):

        """
        Use the prepared newer version of the note file to create it on system-level and fill it with content
        """

        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(file_template)

    @staticmethod
    def _revert_backup(temporary_file, original_file):

        """

        Return and rename the temporary file back to the original file on system-level

        """

        return os.rename(temporary_file, original_file)
