from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QHBoxLayout, QFormLayout, QPushButton
import pyglet
from bson import ObjectId
import datetime

# Класс для создания окна для добавления документа
class AddClass(QDialog):
    def __init__(self, parent):
        super(AddClass, self).__init__(parent)
        self.zapros = {}
        self.button = QPushButton()
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

    # Метод для создания ока и заполнения его
    def setLay(self):
        for title in self.hed:
            self.fild[title] = QLabel(self)
            self.fild[title].setText(f"{title}")
            self.lay[title] = QLineEdit("", self)
            self.form.addRow(self.fild[title], self.lay[title])
        self.button.setText("Добавить запись")
        self.button.clicked.connect(self.add)
        self.form.addRow(self.button)
        self.setLayout(self.form)
        self.adjustSize()

    # Метод добавлени документа в коллекцию
    def add(self):
        for title in self.hed:
            text = self.lay[title].text()
            if text != '':  # Если было найдено пустое поле, вернуть на до заполнение
                if text.isdigit():  # Если передано число, то записать как число
                    text = int(text)
                self.zapros[self.fild[title].text()] = text
            else:
                return
        series_collection = self.main.db[self.main.name]
        series_collection.insert_one(self.zapros)
        self.main.find_col()
