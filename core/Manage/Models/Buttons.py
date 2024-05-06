"""

    Created by Colin Gelling on 02/05/2024
    Using Pycharm Professional

"""


from PyQt6.QtWidgets import QPushButton


class ButtonOverride(QPushButton):
	def __init__(self, parent=None):
		super().__init__(parent)
		