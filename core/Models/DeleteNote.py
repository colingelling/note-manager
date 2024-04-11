import os


class DeleteNote:
    def __init__(self):
        super().__init__()

    @staticmethod
    def delete(file):

        """
        Use file value and attempt to delete it on system-level
        """

        try:
            if os.path.isfile(file):
                os.remove(file)
        except Exception as e:
            print(f"An error occurred: {e}")
            
