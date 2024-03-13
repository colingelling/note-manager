"""

    Created by Colin Gelling on 31/01/2024
    Using Pycharm Professional

"""

import os

from PyQt6.QtGui import QFileSystemModel


class EditNote(QFileSystemModel):

    updated_note_title = None
    updated_parent_notebook = None
    updated_note_description = None

    def __init__(self, parent=None):
        super(EditNote, self).__init__(parent)

        self.file_path = None

    def _update_data(self, note_information, source_file, updated_title, updated_description):
        file_path = note_information['filePath']

        file_extension = ".txt"
        original_file = source_file + file_extension
        new_file = ''.join(updated_title + file_extension)

        temporary_file = self._prepare_temporary_note(file_path, original_file)
        updated_note_file = self._prepare_new_note(file_path, original_file, new_file)

        if EditNote.updated_note_title:

            note_information.update({
                'tempFile': temporary_file,
                'filePath': updated_note_file
            })

        if EditNote.updated_note_description:

            note_information.update({
                'fileDescription': updated_description
            })

    @staticmethod
    def _compare_titles(filename, changed_title):
        if changed_title != filename:
            return True

    @staticmethod
    def _compare_descriptions(note_description, file_description):
        if note_description != file_description:
            return True

    @staticmethod
    def _prepare_temporary_note(file_path, file):
        temp_file = file.replace(".txt", ".tmp.txt")
        path = file_path.replace(file, '.' + temp_file)
        return path

    @staticmethod
    def _make_temporary_note(original_file, temporary_file):
        return os.rename(original_file, temporary_file)

    @staticmethod
    def _prepare_new_note(file_path, source, target):
        if source != target and target not in file_path:
            path = file_path.replace(source, target)
            return path

    @staticmethod
    def _make_new_note(file_path, file_template):
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(file_template)

    @staticmethod
    def _update_note(file_path, template):
        with open(file_path, 'r+') as file:
            file.seek(0)
            file.truncate()
            file.write(template)

    def save_changes(self, note_information, title, description):

        # Retrieve path to note in order to edit it
        file_path = note_information['filePath']
        file_name = note_information['fileName']
        file_description = note_information['fileDescription']

        # Update the file template
        file_template = ''.join(title + "\n\n" + description)

        if file_name is not title:
            note_information.update({
                'fileName': title
            })

        EditNote.updated_note_description = self._compare_descriptions(description, file_description)
        EditNote.updated_note_title = self._compare_titles(title, file_name)

        self._update_data(note_information, file_name, title, description)

        temporary_file = note_information['tempFile']
        if file_path:
            if temporary_file:
                self._make_temporary_note(file_path, temporary_file)
                self._make_new_note(note_information['filePath'], file_template)

                from core.Models.DeleteNote import DeleteNote
                model = DeleteNote()
                model.delete(temporary_file)
