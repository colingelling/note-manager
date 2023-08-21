"""

Created by Colin Gelling on 03/05/2023
Using Pycharm Professional

"""


class Bootstrapper:

    """
        This class provides important background functionality needed by the app in order to function properly
    """

    def __init__(self):
        super().__init__()

        self.setup_controller()

    @staticmethod
    def setup_controller():
        from core.Controllers.WindowController import WindowController
        class_instance = WindowController()
        class_method = class_instance.show_home_window()
        return class_method
