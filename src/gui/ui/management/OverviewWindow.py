# Form implementation generated from reading ui file '/home/colin/Python/Projects/Pycharm/Development/Repositories/note-manager/src/gui/ui/management/OverviewWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OverviewWindow(object):
    def setupUi(self, OverviewWindow):
        OverviewWindow.setObjectName("OverviewWindow")
        OverviewWindow.resize(800, 600)
        self.WindowWidget = QtWidgets.QWidget(parent=OverviewWindow)
        self.WindowWidget.setObjectName("WindowWidget")
        self.ContentWidget = QtWidgets.QWidget(parent=self.WindowWidget)
        self.ContentWidget.setGeometry(QtCore.QRect(10, 9, 781, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContentWidget.sizePolicy().hasHeightForWidth())
        self.ContentWidget.setSizePolicy(sizePolicy)
        self.ContentWidget.setObjectName("ContentWidget")
        self.OverviewTable = QtWidgets.QTableView(parent=self.ContentWidget)
        self.OverviewTable.setGeometry(QtCore.QRect(250, 100, 531, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OverviewTable.sizePolicy().hasHeightForWidth())
        self.OverviewTable.setSizePolicy(sizePolicy)
        self.OverviewTable.setObjectName("OverviewTable")
        self.NoteManagementWidget_2 = QtWidgets.QWidget(parent=self.ContentWidget)
        self.NoteManagementWidget_2.setGeometry(QtCore.QRect(0, 100, 241, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NoteManagementWidget_2.sizePolicy().hasHeightForWidth())
        self.NoteManagementWidget_2.setSizePolicy(sizePolicy)
        self.NoteManagementWidget_2.setMinimumSize(QtCore.QSize(212, 0))
        self.NoteManagementWidget_2.setObjectName("NoteManagementWidget_2")
        self.widget = QtWidgets.QWidget(parent=self.NoteManagementWidget_2)
        self.widget.setGeometry(QtCore.QRect(0, 0, 241, 31))
        self.widget.setObjectName("widget")
        self.ManageMyNotesTitleLabel = QtWidgets.QLabel(parent=self.widget)
        self.ManageMyNotesTitleLabel.setGeometry(QtCore.QRect(10, 10, 67, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ManageMyNotesTitleLabel.sizePolicy().hasHeightForWidth())
        self.ManageMyNotesTitleLabel.setSizePolicy(sizePolicy)
        self.ManageMyNotesTitleLabel.setObjectName("ManageMyNotesTitleLabel")
        self.widget_4 = QtWidgets.QWidget(parent=self.widget)
        self.widget_4.setGeometry(QtCore.QRect(180, 0, 41, 31))
        self.widget_4.setObjectName("widget_4")
        self.OptionsDialogCreateButton = QtWidgets.QPushButton(parent=self.widget_4)
        self.OptionsDialogCreateButton.setGeometry(QtCore.QRect(0, 0, 41, 31))
        self.OptionsDialogCreateButton.setObjectName("OptionsDialogCreateButton")
        self.NoteOverviewWidget = QtWidgets.QWidget(parent=self.NoteManagementWidget_2)
        self.NoteOverviewWidget.setGeometry(QtCore.QRect(0, 30, 241, 201))
        self.NoteOverviewWidget.setObjectName("NoteOverviewWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.NoteOverviewWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.NotebookWidget = QtWidgets.QWidget(parent=self.NoteOverviewWidget)
        self.NotebookWidget.setObjectName("NotebookWidget")
        self.gridLayout.addWidget(self.NotebookWidget, 0, 0, 1, 1)
        self.HeaderWidget = QtWidgets.QWidget(parent=self.ContentWidget)
        self.HeaderWidget.setGeometry(QtCore.QRect(0, 0, 781, 51))
        self.HeaderWidget.setObjectName("HeaderWidget")
        self.TitleLabel = QtWidgets.QLabel(parent=self.HeaderWidget)
        self.TitleLabel.setGeometry(QtCore.QRect(10, 20, 67, 17))
        self.TitleLabel.setObjectName("TitleLabel")
        self.IndividualNoteLabel = QtWidgets.QLabel(parent=self.WindowWidget)
        self.IndividualNoteLabel.setGeometry(QtCore.QRect(110, 430, 67, 17))
        self.IndividualNoteLabel.setObjectName("IndividualNoteLabel")
        self.NoteGroupLabel = QtWidgets.QLabel(parent=self.WindowWidget)
        self.NoteGroupLabel.setGeometry(QtCore.QRect(100, 400, 67, 17))
        self.NoteGroupLabel.setObjectName("NoteGroupLabel")
        self.widget_3 = QtWidgets.QWidget(parent=self.WindowWidget)
        self.widget_3.setGeometry(QtCore.QRect(220, 380, 61, 201))
        self.widget_3.setObjectName("widget_3")
        self.widget_5 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_5.setGeometry(QtCore.QRect(0, 30, 61, 31))
        self.widget_5.setObjectName("widget_5")
        self.EditNoteGroupButton = QtWidgets.QPushButton(parent=self.widget_5)
        self.EditNoteGroupButton.setGeometry(QtCore.QRect(10, 0, 21, 25))
        self.EditNoteGroupButton.setObjectName("EditNoteGroupButton")
        self.DeleteNoteGroupButton = QtWidgets.QPushButton(parent=self.widget_5)
        self.DeleteNoteGroupButton.setGeometry(QtCore.QRect(30, 0, 21, 25))
        self.DeleteNoteGroupButton.setObjectName("DeleteNoteGroupButton")
        self.treeView = QtWidgets.QTreeView(parent=self.WindowWidget)
        self.treeView.setGeometry(QtCore.QRect(420, 400, 256, 192))
        self.treeView.setObjectName("treeView")
        OverviewWindow.setCentralWidget(self.WindowWidget)

        self.retranslateUi(OverviewWindow)
        QtCore.QMetaObject.connectSlotsByName(OverviewWindow)

    def retranslateUi(self, OverviewWindow):
        _translate = QtCore.QCoreApplication.translate
        OverviewWindow.setWindowTitle(_translate("OverviewWindow", "MainWindow"))
        self.ManageMyNotesTitleLabel.setText(_translate("OverviewWindow", "TextLabel"))
        self.OptionsDialogCreateButton.setText(_translate("OverviewWindow", "+"))
        self.TitleLabel.setText(_translate("OverviewWindow", "TextLabel"))
        self.IndividualNoteLabel.setText(_translate("OverviewWindow", "TextLabel"))
        self.NoteGroupLabel.setText(_translate("OverviewWindow", "TextLabel"))
        self.EditNoteGroupButton.setText(_translate("OverviewWindow", "E"))
        self.DeleteNoteGroupButton.setText(_translate("OverviewWindow", "D"))
