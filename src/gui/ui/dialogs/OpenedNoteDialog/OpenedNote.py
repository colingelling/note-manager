# Form implementation generated from reading ui file '/home/colin/Python/Projects/Pycharm/Development/Repositories/note-manager/src/gui/ui/dialogs/OpenedNoteDialog/OpenedNote.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OpenedNoteDialog(object):
    def setupUi(self, OpenedNoteDialog):
        OpenedNoteDialog.setObjectName("OpenedNoteDialog")
        OpenedNoteDialog.resize(821, 706)
        OpenedNoteDialog.setMinimumSize(QtCore.QSize(0, 706))
        self.gridLayout = QtWidgets.QGridLayout(OpenedNoteDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.TitleWidget = QtWidgets.QWidget(parent=OpenedNoteDialog)
        self.TitleWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleWidget.sizePolicy().hasHeightForWidth())
        self.TitleWidget.setSizePolicy(sizePolicy)
        self.TitleWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.TitleWidget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.TitleWidget.setAutoFillBackground(False)
        self.TitleWidget.setObjectName("TitleWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.TitleWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.noteTitle_label = QtWidgets.QLabel(parent=self.TitleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noteTitle_label.sizePolicy().hasHeightForWidth())
        self.noteTitle_label.setSizePolicy(sizePolicy)
        self.noteTitle_label.setObjectName("noteTitle_label")
        self.verticalLayout_2.addWidget(self.noteTitle_label)
        self.noteTitle_lineEdit = QtWidgets.QLineEdit(parent=self.TitleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noteTitle_lineEdit.sizePolicy().hasHeightForWidth())
        self.noteTitle_lineEdit.setSizePolicy(sizePolicy)
        self.noteTitle_lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.noteTitle_lineEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.noteTitle_lineEdit.setObjectName("noteTitle_lineEdit")
        self.verticalLayout_2.addWidget(self.noteTitle_lineEdit)
        self.gridLayout.addWidget(self.TitleWidget, 1, 0, 1, 1)
        self.DescriptionWidget = QtWidgets.QWidget(parent=OpenedNoteDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DescriptionWidget.sizePolicy().hasHeightForWidth())
        self.DescriptionWidget.setSizePolicy(sizePolicy)
        self.DescriptionWidget.setMinimumSize(QtCore.QSize(0, 500))
        self.DescriptionWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.DescriptionWidget.setObjectName("DescriptionWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.DescriptionWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.noteDescription_label = QtWidgets.QLabel(parent=self.DescriptionWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noteDescription_label.sizePolicy().hasHeightForWidth())
        self.noteDescription_label.setSizePolicy(sizePolicy)
        self.noteDescription_label.setObjectName("noteDescription_label")
        self.verticalLayout.addWidget(self.noteDescription_label)
        self.noteDescription_textEdit = QtWidgets.QTextEdit(parent=self.DescriptionWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noteDescription_textEdit.sizePolicy().hasHeightForWidth())
        self.noteDescription_textEdit.setSizePolicy(sizePolicy)
        self.noteDescription_textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.noteDescription_textEdit.setObjectName("noteDescription_textEdit")
        self.verticalLayout.addWidget(self.noteDescription_textEdit)
        self.gridLayout.addWidget(self.DescriptionWidget, 2, 0, 1, 1)

        self.retranslateUi(OpenedNoteDialog)
        QtCore.QMetaObject.connectSlotsByName(OpenedNoteDialog)

    def retranslateUi(self, OpenedNoteDialog):
        _translate = QtCore.QCoreApplication.translate
        OpenedNoteDialog.setWindowTitle(_translate("OpenedNoteDialog", "Dialog"))
        self.noteTitle_label.setText(_translate("OpenedNoteDialog", "TextLabel"))
        self.noteDescription_label.setText(_translate("OpenedNoteDialog", "TextLabel"))
