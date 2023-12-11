

class ManageDisplay:

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_notebooks():
        from core.Manage.Collections.NotebookCollection import NotebookCollection
        collection_obj = NotebookCollection()

        # Set a source directory within storage, followed by selecting a notebook
        notebook_information = collection_obj.get_collection('*', '*')

        return notebook_information
