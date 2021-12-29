from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QWidget, QTableWidget, QHBoxLayout
from PyQt5.QtCore import QRect, QSize
import pyglet
from bson import ObjectId
import datetime


# Класс создающий окно для изменения значения в строке
class InClass(QDialog):
    def __init__(self, parent):
        super(InClass, self).__init__(parent)
        self.main = parent
        self.tableWidget = QTableWidget()
        song = pyglet.media.load('tada.mp3')
        song.play()
        self.setupUi()
        self.show()
        self.tableWidget.itemDoubleClicked.connect(self.double_clicked)

    def closeEvent(self, event):
        song = pyglet.media.load('close.mp3')
        song.play()

    def double_clicked(self, itemm):
        print(itemm.row())
        f = self.tableWidget.item(itemm.row(), itemm.column()).text()
        if f[0] == '{':
            self.inf = []
            self.inf.append(eval(f))
            dialog = InClass(self)
            dialog.exec_()
        elif f[0] == '[':
            self.inf = eval(f)
            dialog = InClass(self)
            dialog.exec_()

    def setupUi(self):
        print(1)
        self.setWindowTitle("Смотрим...")
        layout = QHBoxLayout()
        flag = 0
        str = 0
        for post in self.main.inf:
            if flag == 0:
                z = len(post.keys())
                self.tableWidget.setColumnCount(z)
                self.heder = post.keys()
                self.tableWidget.setHorizontalHeaderLabels(self.heder)
                flag = 1
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            val = post.values()
            val = list(val)
            for j in range(len(post.keys())):
                self.tableWidget.setItem(str, j, QTableWidgetItem(f"{val[j]}"))
            str += 1
        self.tableWidget.resizeColumnsToContents()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)
        self.resize(QSize(880, 687))
