"""

    Created by Colin Gelling on 06/12/2023
    Using Pycharm Professional

"""


class StoreNote:

    def __init__(self):
        super().__init__()

    @staticmethod
    def store_note(path, template):

        filename = None

        title = None
        notebook = None
        description = None

        for key, value in template.items():
            if 'Title' in key:
                filename = f"{value}.txt"

        for key, value in template.items():
            if 'Title' in key:
                title = f"{key}: {value}"
            if 'Notebook' in key:
                notebook = f"{key}: {value}"
            if 'Description' in key:
                description = f"{key}: {value}"

        note_template = f"{title}\n{notebook}\n{description}"

        import os
        note_path = os.path.join(path, filename)
        with open(note_path, "w") as note_file:
            note_file.write(note_template)

        print(f"Note saved to: '{note_path}'")
