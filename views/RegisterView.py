"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow

from core.Controllers.WindowController import WindowController


class RegisterView(QMainWindow, WindowController):

    switch_home = QtCore.pyqtSignal()
    switch_register = QtCore.pyqtSignal()
    switch_login = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.setWindowTitle(f"Register")

        self.setup_navigation()

        # show the ui elements
        self.show_content()

    def load_ui(self):
        from src.gui.ui.register.RegisterWindow import Ui_RegisterWindow
        ui = Ui_RegisterWindow()
        ui.setupUi(self)
        return ui

    def setup_navigation(self):

        ui = self.ui

        button_home = QAction("Home", self)
        button_register = QAction("Register", self)
        button_login = QAction("Login", self)

        # noinspection PyUnresolvedReferences
        button_home.triggered.connect(self.switch_home_window)
        # noinspection PyUnresolvedReferences
        button_register.triggered.connect(self.switch_register_window)
        # noinspection PyUnresolvedReferences
        button_login.triggered.connect(self.switch_login_window)

        menubar = ui.menuBar
        menubar.addAction(button_home)
        menubar.addAction(button_register)
        menubar.addAction(button_login)

    def show_content(self):

        ui = self.ui

        ui.RegisterViewTitleLabel.setText("Register")
        ui.RegisterViewTitleLabel.adjustSize()

        ui.RegisterViewDescriptionLabel.setText("Create an account")
        ui.RegisterViewDescriptionLabel.adjustSize()

        from PyQt6.QtCore import Qt

        ui.RegisterFormFirstnameLabel.setText("Firstname")
        ui.RegisterFormFirstnameLabel.adjustSize()
        ui.RegisterFormFirstnameLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        ui.RegisterFormFirstnameLineEdit.setFocus()

        ui.RegisterFormSuffixLabel.setText("Suffix")
        ui.RegisterFormSuffixLabel.adjustSize()
        ui.RegisterFormSuffixLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        ui.RegisterFormLastnameLabel.setText("Lastname")
        ui.RegisterFormLastnameLabel.adjustSize()
        ui.RegisterFormLastnameLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        ui.RegisterFormUsernameLabel.setText("Username")
        ui.RegisterFormUsernameLabel.adjustSize()
        ui.RegisterFormUsernameLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        ui.RegisterFormEmailLabel.setText("Email address")
        ui.RegisterFormEmailLabel.adjustSize()
        ui.RegisterFormEmailLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        ui.RegisterFormPasswordLabel_1.setText("Password")
        ui.RegisterFormPasswordLabel_1.adjustSize()
        ui.RegisterFormPasswordLineEdit_1.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        ui.RegisterFormPasswordLineEdit_1.setEchoMode(ui.RegisterFormPasswordLineEdit_1.EchoMode.Password)

        ui.RegisterFormPasswordLabel_2.setText("Confirm password")
        ui.RegisterFormPasswordLabel_2.adjustSize()
        ui.RegisterFormPasswordLineEdit_2.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        ui.RegisterFormPasswordLineEdit_2.setEchoMode(ui.RegisterFormPasswordLineEdit_2.EchoMode.Password)

        # Set the tab order among line edits
        self.setTabOrder(ui.RegisterFormFirstnameLineEdit, ui.RegisterFormSuffixLineEdit)
        self.setTabOrder(ui.RegisterFormSuffixLineEdit, ui.RegisterFormLastnameLineEdit)
        self.setTabOrder(ui.RegisterFormLastnameLineEdit, ui.RegisterFormUsernameLineEdit)
        self.setTabOrder(ui.RegisterFormUsernameLineEdit, ui.RegisterFormEmailLineEdit)
        self.setTabOrder(ui.RegisterFormEmailLineEdit, ui.RegisterFormPasswordLineEdit_1)
        self.setTabOrder(ui.RegisterFormPasswordLineEdit_1, ui.RegisterFormPasswordLineEdit_2)

        ui.RegisterFormSubmitBtn.setText("Register")
        ui.RegisterFormSubmitBtn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        ui.RegisterFormSubmitBtn.clicked.connect(self.pre_submit)

    def pre_submit(self):

        """
            Prepare the submit process. Creating a Dictionary and filling it with the form field data before forwarding.
            :return:
        """

        ui = self.ui

        firstname = ui.RegisterFormFirstnameLineEdit.text()
        suffix = ui.RegisterFormSuffixLineEdit.text()
        lastname = ui.RegisterFormLastnameLineEdit.text()
        username = ui.RegisterFormUsernameLineEdit.text()
        email = ui.RegisterFormEmailLineEdit.text()
        password = ui.RegisterFormPasswordLineEdit_1.text()
        confirmed_password = ui.RegisterFormPasswordLineEdit_2.text()

        form_information = {
            'firstname': firstname,
            'suffix': suffix,
            'lastname': lastname,
            'username': username,
            'email': email,
            'password': password,
            'confirmed_password': confirmed_password
        }

        # forward to the actual submit process
        from core.Models.User import User
        model = User()
        return model.create_user(form_information)

    def switch_home_window(self):
        self.switch_home.emit()

    def switch_register_window(self):
        self.switch_register.emit()

    def switch_login_window(self):
        self.switch_login.emit()
