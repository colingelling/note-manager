"""

    Created by Colin Gelling on 06/12/2023
    Using Pycharm Professional

"""


class CreateNote:

    def __init__(self):
        super().__init__()

    @staticmethod
    def save_note(new_note):

        """
        Set the fundamental ground with the help of specific information for storing the note, extract note data from
        the signal slot following by creating the note file according to a template.
        :param new_note:
        :return:
        """

        # Get access to the application information -class
        from config.resources.set_storage import ApplicationStorage
        app_information = ApplicationStorage()

        # Retrieve the application storage path
        app_storage = app_information.application_storage()

        # Verify existence
        if not app_storage:
            return print("An issue has appeared which caused that the application storage folder could not be created!")

        # Set base path value
        import os
        notebook_destination = os.path.expanduser(f"{app_storage}/notebooks")
        os.makedirs(notebook_destination, exist_ok=True)

        # Convert string from signal back into usable Dictionary format
        import json
        note_dict = json.loads(new_note)

        # Retrieve the selected notebook value
        notebook = note_dict["Notebook"]

        # Set the directory value according to the selected notebook value
        notebook_directory = notebook

        # Final destination of the note that was created should be in 'notebook_destination/notebook/'
        note_path = f"{notebook_destination}/{notebook_directory}"  # TODO: The '/' is a duplicate

        # Retrieve other data from the signal
        title = note_dict["Title"]
        description = note_dict["Description"]

        # Declare a filename based on the note title
        filename = f"{title}.txt"

        # Set full path to the note file
        note_file_path = os.path.join(note_path, filename)

        # Content for the note, including the title, notebook, and description
        note_template = f"Title: {title}\nNotebook: {notebook}\nDescription: {description}\n"

        # Create the note file and fill it with the template
        with open(note_file_path, "w") as note_file:
            note_file.write(note_template)

        print(f"Note saved to: '{note_file_path}'")

        from core.Manage.Modules.Layout.NotebookDisplay.ManageNotes import ManageNotes
        obj = ManageNotes()
        return obj.update_note()
