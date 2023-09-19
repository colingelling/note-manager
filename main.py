"""

Created by Colin Gelling on 30/01/2023
Using Pycharm Professional

"""

from PyQt6 import QtWidgets


def main():
    # Create an application
    app = QtWidgets.QApplication(sys.argv)

    # Define and load the Bootstrapper
    from bootstrap.bootstrapper import Bootstrapper
    Bootstrapper()

    # Connect the cleanup function to the aboutToQuit signal (Temporarily)
    app.aboutToQuit.connect(Bootstrapper.cleanup)

    # Startup
    sys.exit(app.exec())


# Instantiate the application
if __name__ == '__main__':
    import sys
    main()
