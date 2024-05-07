"""

    Created by Colin Gelling on 02/05/2024
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QMessageBox, QPushButton


class NotebookRemoval:
	def __init__(self):
		self.message_box = QMessageBox()
		
	def show_error(self, notebook):
		self.message_box.setIcon(QMessageBox.Icon.Critical)
		self.message_box.setText(f"Notebook '{notebook}' cannot be removed directly!")
		self.message_box.setInformativeText("The notebook you want to remove is not empty, what do you want to do?")
		
		# Remove the standard buttons first
		self.message_box.setStandardButtons(self.message_box.StandardButton.NoButton)
		
		close_dialog = QPushButton("Close this dialog")
		
		# Connect the close button's clicked signal to the message box's reject method
		close_dialog.clicked.connect(self.message_box.reject)
		
		# Add the close button to the dialog with the RejectRole
		self.message_box.addButton(close_dialog, QMessageBox.ButtonRole.RejectRole)
		
		manage_notes = QPushButton("Manage my notes in this notebook")
		
		# TODO: Implement WindowController's manage_notes_dialog method to refer to
		# manage_notes.clicked.connect(dialog_model.note_manager_dialog)
		self.message_box.addButton(manage_notes, QMessageBox.ButtonRole.ActionRole)
		
		self.message_box.exec()
	
	def show_warning(self, notebook):
		self.message_box.setIcon(self.message_box.Icon.Warning)
		self.message_box.setText("Are you sure you want to delete this item?")
		self.message_box.setInformativeText(f"You are about to delete the following notebook: '{notebook}'. \n\n"
		                               f"Are you sure? This action cannot be undone!")
		
		yes_button = QMessageBox.StandardButton.Yes
		no_button = QMessageBox.StandardButton.No
		
		self.message_box.setStandardButtons(yes_button | no_button)
		self.message_box.setDefaultButton(no_button)
		
		button_clicked = self.message_box.exec()
		if button_clicked == yes_button:
			return yes_button
		else:
			self.message_box.accept()
			