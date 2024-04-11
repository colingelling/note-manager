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

    def save_changes(self, data, title, description):

        # Declare and retrieve values from the data model
        file_path = data['filePath']
        file_name = data['fileName']
        file_content = data['fileContent']

        # Verify that the main dictionary's fileName matches to the original name of the note being opened, then replace
        # the original with the new value
        if file_name is not title:
            data.update({
                'fileName': title
            })

        # Prepare the file values 'absolute path' of both the temporally saved copy of the original and the new file
        updated_files = self._prepare_updated_files(file_path, file_name, title)

        temporary_file = None
        updated_file = None

        # Assigning values from dictionary (updated_files)
        for key, value in updated_files.items():
            if key == 'temp_file':
                temporary_file = value
            if key == 'updated_file':
                updated_file = value

        # Update the main dictionary, add the temporary
        for key, value in dict(data).items():
            if key == 'filePath' and value == file_path:
                data.update({
                    'filePath': updated_file
                })

        # Store the description content in the main dictionary
        data.update({
            'fileContent': description
        })

        # Make a backup from the original file
        self._make_temporary_note(file_path, temporary_file)

        # Set the file template containing the content that will be put inside the new file
        file_template = ''.join(title + "\n\n" + description)

        # Verify that the creation of temporary_file has been succeeded. When true, create a new file in order to
        # replace the original but with the correct values.
        if os.path.exists(temporary_file):
            self._make_new_note(updated_file, file_template)
        else:
            message = "Application closed due to an issue where the backup of the original file did not succeed."
            exit(message)  # TODO: Refer to a popup dialog displaying the text above

        # Verify that the new version of the file has been created, when true the temporally saved copy of the original
        # will be removed
        if os.path.exists(updated_file):
            # We do not need the temporarily stored file anymore
            from core.Models.DeleteNote import DeleteNote
            model = DeleteNote()
            model.delete(temporary_file)
        else:
            # Revert changes
            self._revert_backup(temporary_file, file_path)

    def _prepare_updated_files(self, file_path, file_name, updated_title):

        """
        Prepare both the temporarily stored file as a copy of the original file and the new file based on the changed
        values, the file values are in absolute path format.
        """

        temporary_file = self._prepare_temporary_note(file_path, file_name)
        updated_file = self._prepare_new_note(file_path, file_name, updated_title)

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
