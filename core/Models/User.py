"""

    Created by Colin Gelling on 06/03/2023
    Using Pycharm Professional

"""

from core.Database.Connectors.SQLite.Connector import SQLiteConnector


class User(SQLiteConnector):

    """
        This class contains pieces of functionality defined by global database relations.
        Actions in order to manage particular things like creating users, logging in and logging out
    """

    def __init__(self):
        SQLiteConnector.__init__(self)