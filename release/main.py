import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.price_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price_line_edit.sizePolicy().hasHeightForWidth())
        self.price_line_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.price_line_edit.setFont(font)
        self.price_line_edit.setObjectName("price_line_edit")
        self.gridLayout.addWidget(self.price_line_edit, 6, 2, 1, 1)
        self.isGround_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isGround_line_edit.sizePolicy().hasHeightForWidth())
        self.isGround_line_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.isGround_line_edit.setFont(font)
        self.isGround_line_edit.setObjectName("isGround_line_edit")
        self.gridLayout.addWidget(self.isGround_line_edit, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.packing_volume_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packing_volume_line_edit.sizePolicy().hasHeightForWidth())
        self.packing_volume_line_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.packing_volume_line_edit.setFont(font)
        self.packing_volume_line_edit.setObjectName("packing_volume_line_edit")
        self.gridLayout.addWidget(self.packing_volume_line_edit, 7, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.taste_description_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taste_description_line_edit.sizePolicy().hasHeightForWidth())
        self.taste_description_line_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.taste_description_line_edit.setFont(font)
        self.taste_description_line_edit.setObjectName("taste_description_line_edit")
        self.gridLayout.addWidget(self.taste_description_line_edit, 5, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 1, 1, 1)
        self.sort_title_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sort_title_line_edit.sizePolicy().hasHeightForWidth())
        self.sort_title_line_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sort_title_line_edit.setFont(font)
        self.sort_title_line_edit.setObjectName("sort_title_line_edit")
        self.gridLayout.addWidget(self.sort_title_line_edit, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 2)
        self.frying_degree_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frying_degree_line_edit.sizePolicy().hasHeightForWidth())
        self.frying_degree_line_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.frying_degree_line_edit.setFont(font)
        self.frying_degree_line_edit.setObjectName("frying_degree_line_edit")
        self.gridLayout.addWidget(self.frying_degree_line_edit, 3, 2, 1, 1)
        self.id_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id_line_edit.sizePolicy().hasHeightForWidth())
        self.id_line_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.id_line_edit.setFont(font)
        self.id_line_edit.setObjectName("id_line_edit")
        self.gridLayout.addWidget(self.id_line_edit, 1, 2, 1, 1)
        self.ok_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ok_btn.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ok_btn.setFont(font)
        self.ok_btn.setStyleSheet("")
        self.ok_btn.setObjectName("ok_btn")
        self.gridLayout.addWidget(self.ok_btn, 8, 1, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.price_line_edit.setText(_translate("MainWindow", "Не изменять"))
        self.isGround_line_edit.setText(_translate("MainWindow", "Не изменять"))
        self.label_2.setText(_translate("MainWindow", "   sort title:"))
        self.label_3.setText(_translate("MainWindow", "   frying degree:"))
        self.packing_volume_line_edit.setText(_translate("MainWindow", "Не изменять"))
        self.label_4.setText(_translate("MainWindow", "   isGround:"))
        self.taste_description_line_edit.setText(_translate("MainWindow", "Не изменять"))
        self.label_7.setText(_translate("MainWindow", "   packing volume:"))
        self.sort_title_line_edit.setText(_translate("MainWindow", "Не изменять"))
        self.label.setText(_translate("MainWindow", "   id:"))
        self.label_6.setText(_translate("MainWindow", "   price:"))
        self.label_5.setText(_translate("MainWindow", "   taste description:"))
        self.label_8.setText(_translate("MainWindow", "Оствляя id в значении по умолчанию в БД будет создан новый пункт"))
        self.frying_degree_line_edit.setText(_translate("MainWindow", "Не изменять"))
        self.id_line_edit.setText(_translate("MainWindow", "Не изменять"))
        self.ok_btn.setText(_translate("MainWindow", "Ok"))


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridLayout.addWidget(self.table, 1, 0, 1, 2)
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.add_btn.setFont(font)
        self.add_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(self.add_btn, 0, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_btn.setText(_translate("MainWindow", "Добавить / Редактировать запись"))


class MainWindow(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initDB()

    def initUI(self):
        self.setupUi(self)
        self.add_btn.clicked.connect(self.update)
        self.show()

    def show_table(self):
        self.table.setColumnCount(self.number_of_lines)
        self.table.setRowCount(self.number_of_varieties)

        self.table.setHorizontalHeaderLabels(["id", "sort title", "frying degree", "isGround",
                                              "taste description", "price", "packing volume"])

        for i in range(self.number_of_lines):
            self.table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)

        for i in range(self.number_of_varieties):
            for j in range(self.number_of_lines):
                self.table.setItem(i, j, QTableWidgetItem(str(self.info[i][j])))

        self.table.resizeColumnsToContents()

    def initDB(self):
        self.con = sqlite3.connect('data/coffee.db')

        cur = self.con.cursor()
        result = cur.execute(f"""SELECT * FROM Coffee""").fetchall()
        self.number_of_varieties = len(result)
        self.number_of_lines = len(result[0])

        self.info = result

        self.show_table()

    def update(self):
        self.update_window = UpdateWindow()
        self.update_window.setWindowModality(Qt.ApplicationModal)


class UpdateWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initDB()

    def initUI(self):
        self.setupUi(self)
        self.ok_btn.clicked.connect(self.update)
        self.show()

    def initDB(self):
        self.con = sqlite3.connect('data/coffee.db')

    def update(self):
        id = self.id_line_edit.text()
        sort_title = self.sort_title_line_edit.text()
        frying_degree = self.frying_degree_line_edit.text()
        isGround = self.isGround_line_edit.text()
        taste_description = self.taste_description_line_edit.text()
        price = self.price_line_edit.text()
        packing_volume = self.packing_volume_line_edit.text()

        cur = self.con.cursor()
        try:
            if id == 'Не изменять':
                if any([_ == 'Не изменять' for _ in (sort_title, frying_degree, isGround,
                                                     taste_description, price, packing_volume)]):
                    self.send_error()
                else:
                    cur.execute(f"""INSERT INTO Coffee 
                                    ("sort title", "frying degree", "isGround", 
                                    "taste description", "price", "packing volume") 
                                    VALUES {sort_title,
                                            frying_degree,
                                            isGround,
                                            taste_description,
                                            price,
                                            packing_volume}""").fetchall()
            else:
                if sort_title == 'Не изменять':
                    sort_title = cur.execute(
                        f'SELECT "sort title" FROM Coffee WHERE id = {id}').fetchall()[0][0]
                if frying_degree == 'Не изменять':
                    frying_degree = cur.execute(
                        f'SELECT "frying degree" FROM Coffee WHERE id = {id}').fetchall()[0][0]
                if isGround == 'Не изменять':
                    isGround = cur.execute(
                        f'SELECT "isGround" FROM Coffee WHERE id = {id}').fetchall()[0][0]
                if taste_description == 'Не изменять':
                    taste_description = cur.execute(
                        f'SELECT "taste description" FROM Coffee WHERE id = {id}').fetchall()[0][0]
                if price == 'Не изменять':
                    price = cur.execute(
                        f'SELECT "price" FROM Coffee WHERE id = {id}').fetchall()[0][0]
                if packing_volume == 'Не изменять':
                    packing_volume = cur.execute(
                        f'SELECT "packing volume" FROM Coffee WHERE id = {id}').fetchall()[0][0]
                cur.execute(f"""UPDATE Coffee SET "sort title" =        {sort_title}       ,
                                                  "frying degree" =     {frying_degree}    ,
                                                  "isGround" =          {isGround}         ,
                                                  "taste description" = {taste_description},
                                                  "price" =             {price}            ,
                                                  "packing volume" =    {packing_volume}   
                                WHERE id = {id}""")
            self.close()
        except:
            self.send_error()

        self.con.commit()
        ex.initDB()

    def send_error(self):
        self.ok_btn.setText('Error.')
        self.ok_btn.setStyleSheet('color: red')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
