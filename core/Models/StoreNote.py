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
        description = None

        for key, value in template.items():
            if 'Title' in key:
                filename = ''.join(value)
            if 'Description' in key:
                description = ''.join(value)

        template = f"{filename}" + "\n\n" + f"{description}"

        import os
        note_path = os.path.join(path, filename + ".txt")
        with open(note_path, "w") as note_file:
            note_file.write(template)

        print(f"A new note was saved to: '{note_path}'")
