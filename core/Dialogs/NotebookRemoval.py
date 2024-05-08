"""

    Created by Colin Gelling on 02/05/2024
    Using Pycharm Professional

"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox, QPushButton


class NotebookRemoval:
	def __init__(self):
		self.message_box = QMessageBox()
	
	def show_warning(self, notebook):
		"""
		Set introduction related properties
		"""
		
		self.message_box.setIcon(self.message_box.Icon.Warning)
		self.message_box.setText("Are you sure you want to delete this item?")
		self.message_box.setInformativeText(
			f"You are about to delete the following notebook: '{notebook}'. \n\n"
		    f"Are you sure? This action cannot be undone!"
		)
		
		"""
		Declare the buttons and set some options to them
		"""
		
		yes_button = QMessageBox.StandardButton.Yes
		cancel_button = QMessageBox.StandardButton.Cancel
		
		self.message_box.setStandardButtons(yes_button | cancel_button)
		self.message_box.setDefaultButton(yes_button)
		
		yes_button_obj = self.message_box.button(yes_button)
		cancel_button_obj = self.message_box.button(cancel_button)
		
		yes_button_obj.setCursor(Qt.CursorShape.PointingHandCursor)
		cancel_button_obj.setCursor(Qt.CursorShape.PointingHandCursor)
		
		yes_button_obj.setIcon(QIcon())
		cancel_button_obj.setIcon(QIcon())
		
		"""
		Add stylesheet
		"""
		
		style = (""
		             "QMessageBox {background: #fff; padding: 1em;}"
		             "QMessageBox QLabel {color: #333;}"
		             "QMessageBox QPushButton {padding: 8px 14px; color: #333; border-radius: 0px;}"
		             "")
		
		yes_button_obj.setStyleSheet("QPushButton {margin: 3rem;border-bottom: 3px solid rgba(108, 170, 93, 0.99)}")
		cancel_button_obj.setStyleSheet("QPushButton {border-bottom: 3px solid rgba(191, 69, 69, 0.97)}")
		
		self.message_box.setStyleSheet(style)
		
		"""
		Execute and return the dialog
		"""
		
		button_clicked = self.message_box.exec()
		if button_clicked == yes_button:
			return yes_button
		else:
			self.message_box.accept()
	
	def show_error(self, notebook):
		self.message_box.setIcon(QMessageBox.Icon.Critical)
		self.message_box.setText(f"Notebook '{notebook}' cannot be removed directly!")
		self.message_box.setInformativeText("The notebook you want to remove is not empty, what do you want to do?")
		
		# Remove the standard buttons first
		self.message_box.setStandardButtons(self.message_box.StandardButton.NoButton)
		
		manage_notes = QPushButton("Manage my notes in this notebook")
		
		cancel_button = QMessageBox.StandardButton.Cancel
		
		self.message_box.setStandardButtons(cancel_button)
		
		cancel_button_obj = self.message_box.button(cancel_button)
		
		cancel_button_obj.setIcon(QIcon())
		
		cancel_button_obj.setStyleSheet("QPushButton {border-bottom: 3px solid rgba(191, 69, 69, 0.97)}")
		manage_notes.setStyleSheet("QPushButton {border-bottom: 3px solid rgba(44, 165, 111, 0.95)}")
		
		cancel_button_obj.setCursor(Qt.CursorShape.PointingHandCursor)
		manage_notes.setCursor(Qt.CursorShape.PointingHandCursor)
		
		# TODO: Implement WindowController's manage_notes_dialog method to refer to
		# manage_notes.clicked.connect(dialog_model.note_manager_dialog)
		
		self.message_box.addButton(manage_notes, QMessageBox.ButtonRole.ActionRole)
		
		self.message_box.exec()
			