# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BD(object):
    def setupUi(self, BD):
        BD.setObjectName("BD")
        BD.resize(1099, 687)
        BD.setMinimumSize(QtCore.QSize(11, 11))
        BD.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(BD)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 1081, 531))
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.table_name = QtWidgets.QComboBox(self.centralwidget)
        self.table_name.setGeometry(QtCore.QRect(10, 50, 141, 31))
        self.table_name.setObjectName("table_name")
        self.finds = QtWidgets.QPushButton(self.centralwidget)
        self.finds.setGeometry(QtCore.QRect(170, 50, 141, 31))
        self.finds.setObjectName("finds")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 20, 201, 51))
        self.pushButton.setObjectName("pushButton")
        self.Delete = QtWidgets.QPushButton(self.centralwidget)
        self.Delete.setGeometry(QtCore.QRect(860, 60, 181, 28))
        self.Delete.setObjectName("Delete")
        self.D_line = QtWidgets.QLineEdit(self.centralwidget)
        self.D_line.setEnabled(True)
        self.D_line.setGeometry(QtCore.QRect(820, 10, 251, 31))
        self.D_line.setInputMask("")
        self.D_line.setText("")
        self.D_line.setFrame(False)
        self.D_line.setAlignment(QtCore.Qt.AlignCenter)
        self.D_line.setDragEnabled(False)
        self.D_line.setPlaceholderText("")
        self.D_line.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.D_line.setObjectName("D_line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.error_line = QtWidgets.QLabel(self.centralwidget)
        self.error_line.setGeometry(QtCore.QRect(420, 70, 261, 20))
        self.error_line.setText("")
        self.error_line.setAlignment(QtCore.Qt.AlignCenter)
        self.error_line.setObjectName("error_line")
        BD.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BD)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 26))
        self.menubar.setObjectName("menubar")
        BD.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BD)
        self.statusbar.setObjectName("statusbar")
        BD.setStatusBar(self.statusbar)

        self.retranslateUi(BD)
        QtCore.QMetaObject.connectSlotsByName(BD)

    def retranslateUi(self, BD):
        _translate = QtCore.QCoreApplication.translate
        BD.setWindowTitle(_translate("BD", "MainWindow"))
        self.finds.setText(_translate("BD", "Найти"))
        self.pushButton.setToolTip(_translate("BD", "<html><head/><body><p align=\"center\">Добавить новый документ в коллекцию.</p></body></html>"))
        self.pushButton.setWhatsThis(_translate("BD", "<html><head/><body><p><span style=\" font-size:10pt;\">Добавить новый документ в коллекцию.</span></p></body></html>"))
        self.pushButton.setText(_translate("BD", "Добавить документ"))
        self.Delete.setToolTip(_translate("BD", "<html><head/><body><p align=\"center\">Удалить документ из коллекции.</p></body></html>"))
        self.Delete.setText(_translate("BD", "Удалить документ по ID"))
        self.label.setText(_translate("BD", "Выберете коллекцию"))
