"""

    Created by Colin Gelling on 26/03/2024
    Using Pycharm Professional

"""


class Configurations:

    """
    This class is responsible for both the import and return of usable configuration values
    """

    @staticmethod
    def get_navigation_config():  # TODO: Possibly can go because of reader.read_configuration
        from core.Reader import Reader
        reader = Reader()
        resources = reader.read_configuration('config.navigation')
        return resources
