from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QHBoxLayout, QFormLayout, QPushButton
from bson import ObjectId
import pyglet
import json
import datetime


# Класс создающий окно для изменения значения в строке
class UpdateClass(QDialog):
    def __init__(self, parent):
        super(UpdateClass, self).__init__(parent)
        self.zapros = {} # Словарь в котором хранится запрос
        self.button = QPushButton() # Кнопка
        self.main = parent
        self.hed = list(self.main.heder)[1:]
        self.admin = QHBoxLayout()
        self.form = QFormLayout()
        self.fild = {}
        self.lay = {}
        self.setLay()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Добавление")

    def closeEvent(self, event):
        song = pyglet.media.load('close.mp3')
        song.play()

    # Метод для считывания значений и создания окна
    def setLay(self):
        column = 1
        for title in self.hed:
            self.fild[title] = QLabel(self)
            self.fild[title].setText(f"{title}")
            item = self.main.tableWidget.item(self.main.rowss, column).text()
            column += 1
            self.lay[title] = QLineEdit(f"{item}", self)
            self.form.addRow(self.fild[title], self.lay[title])
        self.button.setText("Изменить")
        self.button.clicked.connect(self.add)
        self.form.addRow(self.button)
        self.setLayout(self.form)
        self.adjustSize()

    # Метод занесения информации в БД
    def add(self):
        print("Сработал метод add")
        for title in self.hed:
            text = self.lay[title].text()
            if text != '':  # Если было найдено пустое поле, вернуть на до заполнение
                if text.isdigit(): # Если передано число, то записать как число
                    text = int(text)
                self.zapros[self.fild[title].text()] = text
            else:
                return
        series_collection = self.main.db[self.main.name]
        series_collection.update_one({'_id': ObjectId(self.main.tableWidget.item(self.main.rowss, 0).text())},
                                     {"$set": self.zapros})
        self.main.find_col()
