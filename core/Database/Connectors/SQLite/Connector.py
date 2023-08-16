"""

    Created by Colin Gelling on 06/03/2023
    Using Pycharm Professional

"""

from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from sqlite3 import Error

import os


class SQLiteConnector:

    cwd = os.getcwd()

    # set credential attributes
    db_type = None
    db_name = None
    db_path = None
    db_user = None
    db_pass = None

    # set connection attributes
    connection = None
    query = None

    def __init__(self):
        super(SQLiteConnector, self).__init__()

    @staticmethod
    def prepare():

        db_type = "QSQLITE"
        file_type = "sqlite"
        db_path = "/src/db"
        db_name = "LearningQt"
        db_user = "root"
        db_pass = "Admin1234"

        db_credentials = {
            'db_type': db_type,
            'file_type': file_type,
            'db_path': db_path,
            'db_name': db_name,
            'db_user': db_user,
            'db_pass': db_pass,
        }

        return dict(db_credentials)

    @staticmethod
    def store_credentials(db_type, db_name):
        SQLiteConnector.db_type = db_type
        SQLiteConnector.db_name = db_name

        return SQLiteConnector.db_type, SQLiteConnector.db_name

    @staticmethod
    def database_path():

        current_file = __file__

        # Get the absolute path of the current file
        current_file_path = os.path.abspath(current_file)

        # Split the path into directory components
        components = current_file_path.split(os.path.sep)

        project_name = 'note-manager'

        # Find the index of the directory you want to consider as the project root
        index = components.index(project_name)

        # Join the directory components up to the project root index
        project_root = os.path.sep.join(components[:index + 1])

        return f"{project_root}/src/db/note-manager.sqlite"

    @staticmethod
    def initialize_connection():

        """
            Create database functionality (initialization process, one task only)
            :return:
        """

        # set launch properties
        db_path = SQLiteConnector.database_path()
        db_type = "QSQLITE"

        # set database connection (driver)
        connection = QSqlDatabase.addDatabase(db_type, db_path)

        if not connection.isValid():
            raise Error("Connection could not be validated.")

        # only do something when the file has not been created earlier
        if not os.path.exists(db_path):

            print("Database file has not been found, initializing now.")

            try:

                # set the connection (create)
                connection.setDatabaseName(db_path)
                connection.open()

                # create user table
                from core.Database.Connectors.SQLite.CreateTables import CreateTable
                CreateTable.create_users()

                # final check if the execution was successful
                if os.path.exists(db_path):
                    print("Database connection has been created successfully!")
                    connection.close()

            except Error as e:
                raise Error(f"Could not create database: {e}")

    @staticmethod
    def open_connection():

        """
        This functionality is capable of opening the existing connection to the database.
        When the connection can be opened successfully, attributes are set in order for multiple usage possibilities in
        other functions.
        :return:
        """

        # include database path
        db_path = SQLiteConnector.database_path()

        # load driver by declaring path
        connection = QSqlDatabase.database(db_path, open=False)

        if not connection.isValid():
            raise Error("Connection could not be validated.")

        if not os.path.exists(db_path):
            raise Error("Database does not exist!")

        try:

            # reach the database
            connection.setDatabaseName(db_path)
            connection.open()

            # assign connection objects to class attributes for access to other functions
            SQLiteConnector.connection = connection
            SQLiteConnector.query = QSqlQuery(connection)

            # check if the connection could be opened
            if not connection.open():
                print(f'Error opening database: {connection.lastError().text()}')

        except Error as e:
            raise Error(f"Could not set connection: {e}")

    def close_connection(self):

        """
        This piece is capable of closing the connection to the database and cleaning up afterward.
        :return:
        """

        connection = self.connection
        if not connection.isValid():
            raise ValueError("Database connection is not available at this point.")

        # the connection should be closed, only when it was opened earlier
        if connection.isOpen():

            # close the connection
            connection.close()

            # set attributes to empty
            self.connection = None
            self.query = None

            # confirm if they are empty
            if self.connection and self.query:
                raise Warning("Database connections could not be emptied.")
