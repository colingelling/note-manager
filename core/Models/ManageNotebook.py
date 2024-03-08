import os


class ManageNotebooks:
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_notebooks():
        root_path = "/home/colin/Desktop/note-manager/notebooks"  # TODO: Replace with source logic

        # Verify that the combined path value is existing and has been created already
        if os.path.exists(root_path):
            # List one-level directories in the specific path
            directories = [d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))]

            return list(directories)
