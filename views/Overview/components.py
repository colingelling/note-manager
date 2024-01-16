"""

    Created by Colin Gelling on 20/12/2023
    Using Pycharm Professional

"""


class ViewComponents:
    def __init__(self):
        super().__init__()

        self.layout = None
        self.notebooks = None

    def notebook_manager(self, ui):
        """
        Prepare some visual properties such as the title, add a 'creator' button for the ability to add a notebook and/or
        note followed by building and updating the view -component.
        :param ui:
        :return:
        """

    @staticmethod
    def recent_activity(ui):
        """
        Preparation and corrected properties # TODO
        :param ui:
        :return:
        """

        ui.LastAddedNotesLabel.setText("Recent activity")
        ui.LastAddedNotesLabel.adjustSize()

        ui.LastAddedNotesTable.setFixedWidth(817)

    @staticmethod
    def placeholder(ui):
        """
        Preparation and corrected properties # TODO
        :param ui:
        :return:
        """

        ui.PlaceholderWidget.setStyleSheet("padding: 0.5em;")
        ui.PlaceholderWidget.setFixedSize(400, 247)
        ui.PlaceholderWidget.setGeometry(250, 390, 0, 100)
        ui.PlaceholderWidget.adjustSize()

    @staticmethod
    def notepad(ui):
        """
        Preparation and corrected properties # TODO
        :param ui:
        :return:
        """

        ui.NotepadLabel.setText("Notepad")
        ui.NotepadLabel.adjustSize()

        ui.NotepadWidget.setFixedSize(380, 247)
        ui.NotepadWidget.adjustSize()

        ui.NotepadWidget.setStyleSheet("padding: 0.5em;")
        ui.NotepadWidget.setGeometry(660, 390, 0, 100)

        ui.NotepadLabel.setStyleSheet("padding: 0; margin-top: 1.2em;")
        ui.NotepadLabel.adjustSize()

        ui.NotepadtextEdit.adjustSize()
        ui.NotepadtextEdit.setStyleSheet("background: #fff; margin-top: 24px; color: #000;")
        ui.NotepadtextEdit.setFixedSize(355, 210)
