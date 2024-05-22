"""

    Created by Colin Gelling on 02/05/2024
    Using Pycharm Professional

"""

import os
from functools import partial

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox, QPushButton


class NotebookRemoval:
	def __init__(self):
		self.dialog_buttons = None
		self.removal_request = None
	
	def show_dialogs(self, item, data):
		
		"""
		
		1) Show the first dialog and pass the name of the item that has been triggered (context-menu)
		2) Verify that each path value is a directory or file on system-level
		3) Clicking on the 'Yes' button within show_warning(item) will set the removal_request property to 'Yes', to
		indicate that it has been clicked. Then the statement below verifies the state followed by iteration and another
		checkup to see if the notebook directory is empty or not. Either remove the directory, or first the file and the
		directory after.
		
		"""
		
		# 1
		self.show_warning(item)
		
		# 2
		notebook_path = [element for element in data if os.path.isdir(element)]
		note_path = [element for element in data if os.path.isfile(element)]
		
		# 3
		if self.removal_request == "Yes":
			for value in notebook_path:
				if not os.listdir(value):
					self._remove_path_dir(value)
				else:
					self.show_final_warning(item, notebook_path, note_path)
	
	def show_warning(self, item):
		
		"""
		
			1) Initialize the (type) dialog object
			2) Assign stylesheet to the dialog
			3) Assign introduction content
			4) Remove standard buttons
			5) Create new buttons
			6) Change the mouse cursor on hover
			7) Add buttons into the dialog
			8) Assign stylesheet to the buttons
			9) Execute the dialog
			10) Check button states and set it to 'Yes' if it has been clicked
		
		"""
		
		# 1
		dialog = QMessageBox()
		
		# 2
		self.set_styling(dialog)
			
		# 3
		dialog.setIcon(dialog.Icon.Warning)
		dialog.setText(f"Are you sure you want to delete {item}?")
		dialog.setInformativeText(
			# f"You are about to delete the following notebook: '{notebook}'. \n\n"
		    "Are you sure? This action cannot be undone!"
		)
		
		# 4
		self._remove_default_buttons(dialog)
		
		# 5
		button_a = QPushButton("Yes")
		button_b = QPushButton("Abort")
		
		# 6
		button_a.setCursor(Qt.CursorShape.PointingHandCursor)
		button_b.setCursor(Qt.CursorShape.PointingHandCursor)
		
		# 7
		dialog.addButton(button_a, QMessageBox.ButtonRole.ActionRole)
		dialog.addButton(button_b, QMessageBox.ButtonRole.RejectRole)
		
		# 8
		button_a.setStyleSheet("QPushButton {margin: 3rem;border-bottom: 3px solid rgba(108, 170, 93, 0.99)}")
		button_b.setStyleSheet("QPushButton {border-bottom: 3px solid rgba(191, 69, 69, 0.97)}")
		
		# 9
		dialog.exec()
		
		# 10
		button = dialog.clickedButton()
		if button == button_a:
			self.removal_request = "Yes"
		else:
			self.removal_request = "No"
		
	@staticmethod
	def set_styling(dialog):
		
		"""
			1) Declare stylesheet
			2) Assign stylesheet to the dialog (passed)
		"""
		
		style = (""
		         "QMessageBox {background: #fff; padding: 1em;}"
		         "QMessageBox QLabel {color: #333;}"
		         "QMessageBox QPushButton {padding: 8px 14px; color: #333; border-radius: 0px;}"
		         "")
		
		dialog.setStyleSheet(style)
		
	@staticmethod
	def _remove_default_buttons(dialog):
		# Return a removal of the standard buttons
		return dialog.setStandardButtons(dialog.StandardButton.NoButton)
		
	def show_final_warning(self, notebook, notebook_path_information, note_path_information):
		
		"""
		
			1) Initialize the (type) dialog object
			2) Assign stylesheet to the dialog
			3) Assign introduction content
			4) Remove standard buttons
			5) Create a new button
			6) Declare a standard button
			7) Set the standard button
			8) Locate the button object of the standard one
			9) Remove button icon
			10) Add stylesheet to both buttons
			11) Change the mouse cursor on hover for both
			12) Add the buttons into the dialog window
			13) Pass both types of path information to the next function when it has been clicked to confirm deletion if
			the notebook wasn't empty
			14) Execute the dialog
		
		"""
		
		# 1
		dialog = QMessageBox()
		
		# 2
		self.set_styling(dialog)

		# 3
		dialog.setIcon(dialog.Icon.Critical)
		dialog.setText(f"Notebook '{notebook}' cannot be removed directly!")
		dialog.setInformativeText("The notebook you want to remove is not empty, what do you want to do?")
		
		# 4
		self._remove_default_buttons(dialog)
		
		# 5
		confirm_removal_button = QPushButton(f"Continue the removal of {notebook}")

		# 6
		cancel_button = QMessageBox.StandardButton.Cancel

		# 7
		dialog.setStandardButtons(cancel_button)

		# 8
		cancel_button_obj = dialog.button(cancel_button)

		# 9
		cancel_button_obj.setIcon(QIcon())

		# 10
		cancel_button_obj.setStyleSheet("QPushButton {border-bottom: 3px solid rgba(191, 69, 69, 0.97)}")
		confirm_removal_button.setStyleSheet("QPushButton {border-bottom: 3px solid rgba(44, 165, 111, 0.95)}")

		# 11
		cancel_button_obj.setCursor(Qt.CursorShape.PointingHandCursor)
		confirm_removal_button.setCursor(Qt.CursorShape.PointingHandCursor)
		
		# 12
		dialog.addButton(confirm_removal_button, QMessageBox.ButtonRole.ActionRole)
		
		# 13
		for path in notebook_path_information:
			confirm_removal_button.clicked.connect(
				partial(self._remove_pair, notebook_path_information, note_path_information)
			)
		
		# 14
		dialog.exec()
	
	@staticmethod
	def _remove_path_dir(path):
		if os.path.isdir(path):
			os.rmdir(path)
	
	def _remove_pair(self, notebook_path_information, note_path_information):
		# Remove file(s) first
		for value in note_path_information:
			os.remove(value)
		
		# Remove the notebook directory secondly
		for value in notebook_path_information:
			self._remove_path_dir(value)
		
			