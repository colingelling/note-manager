"""

    Created by Colin Gelling on 26/07/2024
    Using Pycharm Professional

"""


class EditNotebook:
	def __init__(self):
		self.dialog_buttons = None
		self.removal_request = None
	
	@staticmethod
	def show_dialog(item_value, notebook_value, notebook_path_value, note_path_values):
		
		data = {  # Also returned to have empty values, except for the 'item'
			"notebook": item_value,
			"notebook_path": notebook_path_value,
			"note_path_values": note_path_values
		}
		
		from core.Controllers.WindowController import WindowController
		controller = WindowController()
		return controller.edit_notebook_dialog(data)
	