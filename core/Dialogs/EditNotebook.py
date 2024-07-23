"""

    Created by Colin Gelling on 26/07/2024
    Using Pycharm Professional

"""


class EditNotebook:
	def __init__(self):
		self.dialog_buttons = None
		self.removal_request = None
	
	@staticmethod
	def show_dialog(item, path):
		data = {
			"notebook": item,
			"notebook_path": path
		}
		
		from core.Controllers.WindowController import WindowController
		controller = WindowController()
		return controller.edit_notebook_dialog(data)
	