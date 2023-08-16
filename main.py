"""

Created by Colin Gelling on 30/01/2023
Using Pycharm Professional

"""

from PyQt6 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)

    from bootstrap.bootstrapper import Bootstrapper
    Bootstrapper()

    sys.exit(app.exec())


# Instantiate the application
if __name__ == '__main__':
    import sys
    main()
