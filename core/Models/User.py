"""

    Created by Colin Gelling on 06/03/2023
    Using Pycharm Professional

"""

from sqlite3 import Error

from core.Database.Connectors.SQLite.Connector import SQLiteConnector


class User(SQLiteConnector):

    """
        This class contains pieces of functionality defined by global database relations.
        Actions in order to manage particular things like creating users, logging in and logging out
    """

    user_data = {}
    user_ids = []

    def __init__(self):
        SQLiteConnector.__init__(self)

    @staticmethod
    def create_user(form_information):

        # receive both keys and values from form field data (put into Dictionary)
        form_data = dict(form_information)

        # iterate over individual values
        form_values = [form_data.get(key) for key in form_data]

        # remove password from values list
        password = form_values.pop()

        # support package functionality
        import bcrypt  # TODO: find a solution in order to install this package first automatically

        # hash password
        field_to_encrypt = password
        change_format = "{}".format(field_to_encrypt)
        encrypted_password = field_to_encrypt.encode('utf-8')
        salt_object = bcrypt.gensalt(rounds=16)
        hashed_str = bcrypt.hashpw(encrypted_password, salt_object)
        password_hash = hashed_str.decode("utf-8")

        # open the connection
        db_class = SQLiteConnector()
        db_class.open_connection()

        # bind attributes to credentials (set all form fields here)
        firstname = form_data['firstname']
        suffix = form_data['suffix']
        lastname = form_data['lastname']
        username = form_data['username']
        email = form_data['email']

        connection = db_class.connection
        if not connection.isValid():
            raise ValueError("Connection is invalid.")

        import sqlite3
        try:

            from datetime import datetime

            # set the collection of user credentials to use within a query
            query_data = {
                'firstname': firstname,
                'suffix': suffix,
                'lastname': lastname,
                'username': username,
                'email': email,
                'password': password_hash,
                'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # build the SQL query string
            columns = ', '.join(query_data.keys())
            placeholders = ', '.join([':{}'.format(key) for key in query_data.keys()])
            query_string = f"INSERT INTO users ({columns}) VALUES ({placeholders})"

            # prepare the query
            query = SQLiteConnector.query
            query.prepare(query_string)

            # bind values to query
            for key in query_data.keys():
                if key != 'created_at':
                    query.bindValue(":" + key, query_data[key])

            # bind the created_at value separately
            query.bindValue(":created_at", query_data['created_at'])

            # execute the query
            if not query.exec():
                raise Error("Error adding user:", query.lastError().text())

            connection.commit()

            print("User has been created, you can go to the login window now!")

        except sqlite3.Error as error:
            print("This program could not create the user:", error)

    @staticmethod
    def login_user(form_information, window_switch):

        from core.Database.Connectors.SQLite.Connector import SQLiteConnector
        db_class = SQLiteConnector()

        # open the connection
        db_class.open_connection()

        # verify connection
        connection = db_class.connection
        if not connection.isValid():
            raise ValueError("Connection is invalid.")

        # set attributes
        user = None
        password = None

        # retrieve keys and value pairs and assign them to attributes within this scope
        form_data = dict(form_information)
        user = form_data.get('user')
        password = form_data.get('password')

        if not user or not password:
            raise ValueError("The username or email address and password are missing")

        query_string = f"SELECT id, email, username, password FROM users WHERE email = '{user}' " \
                       f"OR username = '{user}'"

        query = db_class.query
        query.prepare(query_string)

        # verify that the query can be executed or that there is an issue here
        if not query.exec():
            raise Error("Error executing the query:", query.lastError().text())

        # filter trough every row of results according to the command execution
        if not query.next():
            print("No user found with the provided email or username.")
            return False

        # get the column names of the data that was received
        column_names = [query.record().fieldName(i) for i in range(query.record().count())]

        # retrieve password from the database
        password_index = column_names.index('password')
        hashed_password = query.value(password_index)
        entered_password = password

        import bcrypt

        # compare entered password with stored hashed password
        salt = hashed_password[:29].encode('utf-8')  # extract salt from stored hashed password
        hashed_entered_password = bcrypt.hashpw(entered_password.encode('utf-8'), salt)  # combine

        # are the passwords matching?
        if not hashed_password.encode('utf-8') == hashed_entered_password:
            print("Password does not match with the user. Login failed.")
            return False  # Indicate login failure

        print("Password matched. User passed the login checks and has been send to the authenticated window.")

        window_switch.emit()

        return True  # Indicate login success



    def get_user_ids(self):

        # probably could be moved to

        # set an open connection
        self.open_connection()

        # declare the connection
        connection = self.connection

        # check if the connection is usable
        if not connection.isValid():
            raise Error("Connection is not valid.")

        query_string = f"SELECT id FROM users"
        query = self.query
        query.prepare(query_string)

        # execute the query (getting all results)
        if not query.exec():
            raise Error("Error executing the query:", query.lastError().text())

        # filter trough every row of results according to the command execution
        if not query.next():
            print("No user found with the provided email or username.")
            return

        # get the column names of the data that was received
        column_names = [query.record().fieldName(i) for i in range(query.record().count())]

        # get the values of that column
        user_ids = {column: query.value(query.record().indexOf(column)) for column in column_names}
        self.user_ids = user_ids

        for user_id in user_ids:
            print(user_id)
