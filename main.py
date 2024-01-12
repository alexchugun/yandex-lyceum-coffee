import sys

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication, QMainWindow

from addEditCoffee import AddEditCoffee


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        uic.loadUi('main.ui', self)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('coffee.sqlite')
        self.db.open()

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('coffee')
        self.model.select()

        self.db_view.setModel(self.model)

        self.addButton.clicked.connect(self.add_data)
        self.editButton.clicked.connect(self.update_data)

    def add_data(self):
        self.add_edit_coffee = AddEditCoffee(self)
        self.add_edit_coffee.show()

    def update_data(self):
        # print(data)
        # print(self.db_view.selectionModel().currentIndex().row()) # тут индекс для обновления
        # selected_index = self.db_view.model().index(self.db_view.selectionModel().currentIndex().row(), 0).data() # тут индекс в самой бд

        current_index = self.db_view.selectionModel().currentIndex().row()
        name = self.db_view.model().index(current_index, 1).data()
        degree_roast = self.db_view.model().index(current_index, 2).data()
        is_ground = self.db_view.model().index(current_index, 3).data()
        description = self.db_view.model().index(current_index, 4).data()
        price = self.db_view.model().index(current_index, 5).data()
        volume = self.db_view.model().index(current_index, 6).data()

        data = {'current_index': current_index,
                'name': name,
                'degree_roast': degree_roast,
                'is_ground': is_ground,
                'description': description,
                'price': price,
                'volume': volume
                }

        self.add_edit_coffee = AddEditCoffee(self, data=data)
        self.add_edit_coffee.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
