from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.db_view = QtWidgets.QTableView(self.centralwidget)
        self.db_view.setGeometry(QtCore.QRect(10, 10, 781, 471))
        self.db_view.setMaximumSize(QtCore.QSize(781, 16777215))
        self.db_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.db_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.db_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.db_view.setObjectName("db_view")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 490, 781, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Капучино"))
        self.addButton.setText(_translate("MainWindow", "Добавить запись"))
        self.editButton.setText(_translate("MainWindow", "Изменить"))
