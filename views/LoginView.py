"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow

from core.Controllers.WindowController import WindowController
from core.Models.User import User


class LoginView(QMainWindow, WindowController, User):

    switch_home = QtCore.pyqtSignal()
    switch_register = QtCore.pyqtSignal()
    switch_login = QtCore.pyqtSignal()

    switch_user = QtCore.pyqtSignal()

    def __init__(self):
        super(LoginView, self).__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_ui()

        self.setWindowTitle(f"Login")

        # load content
        self.setup_navigation()
        self.show_content()

    def load_ui(self):
        from src.gui.ui.login.LoginWindow import Ui_LoginWindow
        ui = Ui_LoginWindow()
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
        # set ui
        ui = self.ui

        ui.LoginViewTitleLabel.setText("Login")
        ui.LoginViewTitleLabel.adjustSize()

        ui.LoginViewDescriptionLabel.setText("Sign in to your account")
        ui.LoginViewDescriptionLabel.adjustSize()

        ui.LoginFormUsernameLabel.setText("Username or email address")
        ui.LoginFormUsernameLabel.adjustSize()

        ui.LoginFormPasswordLabel.setText("Password")
        ui.LoginFormPasswordLabel.adjustSize()
        ui.LoginFormPasswordLineEdit.setEchoMode(ui.LoginFormPasswordLineEdit.EchoMode.Password)

        self.setTabOrder(ui.LoginFormUsernameLineEdit, ui.LoginFormPasswordLineEdit)
        ui.LoginFormUsernameLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        ui.LoginFormPasswordLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        ui.LoginFormSubmitBtn.setText("Sign in")
        ui.LoginFormSubmitBtn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        ui.LoginFormSubmitBtn.clicked.connect(self.pre_submit)

    def pre_submit(self):

        """
            Prepare the submit process. Creating a Dictionary and filling it with the form field data before forwarding.
            :return:
        """

        ui = self.ui

        # bind field values
        user = ui.LoginFormUsernameLineEdit.text()
        password = ui.LoginFormPasswordLineEdit.text()

        # collect them
        form_information = {
            'user': user,
            'password': password,
        }

        window_switch = self.switch_user_window

        # forward to the actual submit process
        from core.Models.User import User
        model = User()

        # pass the switch_user signal directly
        login_successful = model.login_user(form_information, self.switch_user)

        if login_successful:
            # Emit the signal to switch the window after successful login
            self.switch_user.emit()

    def switch_home_window(self):
        self.switch_home.emit()

    def switch_register_window(self):
        self.switch_register.emit()

    def switch_login_window(self):
        self.switch_login.emit()

    def switch_user_window(self):
        self.switch_user.emit('user_authenticated')
