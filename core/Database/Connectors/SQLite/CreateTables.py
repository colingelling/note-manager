"""

    Created by Colin Gelling on 13/07/2023
    Using Pycharm Professional

"""

from core.Database.Connectors.SQLite.Connector import SQLiteConnector


class CreateTable(SQLiteConnector):
    def __init__(self):
        super().__init__()
        pass

    @staticmethod
    def create_users():

        # open the database connection (ready to use self.connection)
        from core.Database.Connectors.SQLite.Connector import SQLiteConnector
        SQLiteConnector.open_connection()
        connection = SQLiteConnector.connection

        if not connection.isValid():
            print("Connection is invalid.")

        # verify an open connection
        if not connection.isOpen():
            print('Database connection is not open.')

        if not SQLiteConnector.query:
            raise ValueError('Query attribute has not seen an object, queries could not be executed.')

        query = SQLiteConnector.query

        import sqlite3
        try:

            if query.exec("SELECT * FROM users"):

                print("Found 'users' table.")

            else:

                print("Creating table 'users'...")

                query.exec("""
                                    CREATE TABLE users (
                                       id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                                       firstname VARCHAR(40) NOT NULL,
                                       suffix VARCHAR(16) NOT NULL,
                                       lastname VARCHAR(40) NOT NULL,
                                       username VARCHAR(40) NOT NULL,
                                       email VARCHAR(40) NOT NULL,
                                       password VARCHAR(40) NOT NULL,
                                       created_at TEXT NOT NULL
                                   )
                                """)

        except sqlite3.Error as error:
            print("Could not create table 'users':", error)
