"""

Created by Colin Gelling on 03/05/2023
Using Pycharm Professional

"""
# import os.path


class Bootstrapper:

    """
        This class provides important background functionality needed by the app in order to function properly
        This functionality has the purpose of loading multiple features within the background
    """

    def __init__(self):
        super().__init__()

        self.setup_controller()

    """
    
        Methods are instantiating classes and returning particular method(s)
        :return: 
    
    """

    @staticmethod
    def setup_controller():
        from core.Controllers.WindowController import WindowController
        class_instance = WindowController()
        class_method = class_instance.show_overview_window()
        return class_method

    # @staticmethod
    # def cleanup():
    #
    #     # TODO: Temporary function, remove any leftover things that were created by the app
    #
    #     try:
    #         # The directory to clean
    #         notemanager_directory = os.path.expanduser("~/Desktop/note-manager")
    #
    #         # Delete the entire directory and its contents
    #         if os.path.exists(notemanager_directory):
    #             import shutil
    #             shutil.rmtree(notemanager_directory)
    #     except Exception as e:
    #         print(f"Error while cleaning up: {e}")
