import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import QSettings, QCoreApplication
from UI_ui import Ui_BD
from AddClass import AddClass
from UpdateClass import UpdateClass
import pymongo as pm
import pyglet
from InClass import InClass
from bson import ObjectId
import datetime

APPLICATION_NAME = 'QSettings program'
ORGANIZATION_DOMAIN = 'example.com'
SET_TABLE = "TABLE"


class MyWidget(QMainWindow, Ui_BD):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.error_line.setText("")
        song = pyglet.media.load('welcom.mp3')
        song.play()
        self.heder = 0
        self.connect()
        # Добавление значений в выпадающий список
        self.table_name.addItem("")
        self.table_name.addItem("Product")
        self.table_name.addItem("Purchases")
        self.table_name.addItem("Applications")
        settings = QSettings("./BD.ini", 1)
        table_name_id = settings.value(SET_TABLE, 0, type=int)  # Считываем значение переменной сохраненной в файле
        self.table_name.setCurrentIndex(table_name_id)
        self.find_col()
        self.name = self.table_name.currentText()
        # создаем обработчики
        self.finds.clicked.connect(self.find_col)
        self.pushButton.clicked.connect(self.open_Add_Dialog)
        self.Delete.clicked.connect(self.Delet)
        self.tableWidget.itemDoubleClicked.connect(self.double_clicked)

    # Функция отрабатывающее двойное нажатие на значение в таблице
    def double_clicked(self, itemm):
        self.inf = list
        f = self.tableWidget.item(itemm.row(), itemm.column()).text()
        if f[0] == '{':  # Если мы встретили словарь в ячейке
            self.inf = []
            self.inf.append(eval(f))
            dialog = InClass(self)
            dialog.exec_()
        elif f[0] == '[':  # Если мы встретили массив в ячейке
            self.inf = eval(f)
            dialog = InClass(self)
            dialog.exec_()
        else:  # Если просто значение
            self.rowss = itemm.row()
            dialog = UpdateClass(self)
            dialog.exec_()

    # Функция выполняющая соединение с БД
    def connect(self):
        conn_str = "mongodb+srv://Roman:[пароль]@cluster0.jjtq1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = pm.MongoClient(conn_str)
        try:
            print()
        except Exception:
            print("Unable to connect to the server.")
        self.db = client['Semestr']

    # Функция отрабатывающая удаление документа
    def Delet(self):
        line = self.D_line.text()
        self.D_line.clear()
        if line == '' and self.name == '':
            self.D_line.setStyleSheet('background : #FF0000;;;;')
            self.error_line.setText("Не указан ID удаления")
            print("Не указан id удаления")
        elif line[0] != '6' and len(line) != 24:
            self.D_line.setStyleSheet('background : #FF0000;;;;')
            self.error_line.setText("Не верно указан ID")
            print("Ошибка в ID")
        else:
            self.error_line.setText("")
            self.D_line.setStyleSheet('background : #008000;;;;')
            series_collection = self.db[self.name]
            series_collection.delete_one({'_id': ObjectId(line)})
            self.find_col()
            self.D_line.clear()

    # Функция вызыввающая экземпляр класса, для добавления новых данных в БД
    def open_Add_Dialog(self):
        if self.name == '':
            self.error_line.setText("Не выбрана таблица")
            print("Не выбрана таблица")
        else:
            self.error_line.setText("")
            dialog = AddClass(self)
            dialog.exec_()

    # Функция производящее поиск и вывод документов в табличном виде
    def find_col(self):
        self.name = self.table_name.currentText()
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        if self.name == '':
            self.error_line.setText("Не выбрана таблица")
            print("Не выбрана таблица")
        else:
            self.error_line.setText("")
            series_collection = self.db[self.name]
            flag = 0
            ser = series_collection.find()
            str = 0
            for post in ser:
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
            song = pyglet.media.load('file.mp3')
            song.play()

    # Функция отрабатывающая для созранения выбранной таблицы, для последующего изменения
    def closeEvent(self, event):
        settings = QSettings("./BD.ini", 1)
        settings.setValue(SET_TABLE, self.table_name.currentIndex())
        settings.sync()


if __name__ == '__main__':
    QCoreApplication.setApplicationName(APPLICATION_NAME)
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
