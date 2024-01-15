import sys

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication, QMainWindow

from ui.add_edit_coffee_ui import Ui_AddEditCoffeeWindow


class AddEditCoffee(QMainWindow, Ui_AddEditCoffeeWindow):
    def __init__(self, parent, data=None):
        super().__init__()

        self.index = 0
        self.data = data
        self.is_add = True if data is None else False

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.setupUi(self)

        if self.data is not None:
            self.set_data()

        self.saveButton.clicked.connect(self.save)

    def set_data(self):
        self.nameEdit.setText(str(self.data['name']))
        self.degreeRoastEdit.setText(str(self.data['degree_roast']))
        self.isGround.setChecked(int(self.data['is_ground']) == 1)
        self.descriptionEdit.setText(str(self.data['description']))
        self.priceEdit.setText(str(self.data['price']))
        self.volumeEdit.setText(str(self.data['volume']))

        self.index = int(self.data['current_index'])

    def save(self):
        name = self.nameEdit.text()
        degree_roast = self.degreeRoastEdit.text()
        is_ground = self.isGround.isChecked()
        description = self.descriptionEdit.text()
        price = self.priceEdit.text()
        volume = self.volumeEdit.text()

        if '' in [name, degree_roast, description, price, volume]:
            return
            # тут бы надо вывести окно что есть пустые поля и сделать проверку введенных данных

        r = self.parent.model.record() if self.is_add else self.parent.model.record(self.index)
        r.setValue('name', name)
        r.setValue('degree_roast', degree_roast)
        r.setValue('isGround', 1 if is_ground else 0)
        r.setValue('description', description)
        r.setValue('price', price)
        r.setValue('volume', volume)

        if self.is_add:
            self.parent.model.insertRecord(-1, r)
        else:
            self.parent.model.setRecord(self.index, r)
            self.parent.model.submitAll()

        self.parent.model.select()

        self.close()
