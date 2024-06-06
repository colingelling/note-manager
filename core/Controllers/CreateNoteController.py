"""

    Created by Colin Gelling on 11/04/2024
    Using Pycharm Professional

"""


class CreateNoteController:
	def __init__(self):
		super().__init__()
	
	def get_view_data(self):
		
		notebook_information = self._get_notebooks()
		
		return notebook_information
	
	@staticmethod
	def _get_notebooks():
		from core.Collectables.NotebookCollector import NotebookCollection
		collection_obj = NotebookCollection()
		return collection_obj.get_notebook_information('*', '*')
