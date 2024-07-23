"""

    Created by Colin Gelling on 26/07/2024
    Using Pycharm Professional

"""


class EditNotebook:
	def __init__(self):
		self.dialog_buttons = None
		self.removal_request = None
	
	@staticmethod
	def show_dialog(item, path_values):
		
		notebook_path = [notebook_path for notebook_path in path_values if '.txt' not in notebook_path]
		note_path_collection = [note_path for note_path in path_values if '.txt' in note_path]
		
		data = {
			"notebook": item,
			"notebook_path": notebook_path,
			"note_path_values": note_path_collection
		}
		
		from core.Controllers.WindowController import WindowController
		controller = WindowController()
		return controller.edit_notebook_dialog(data)
	