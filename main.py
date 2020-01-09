import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initDB()

    def initUI(self):
        uic.loadUi('main.ui', self)
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
        self.con = sqlite3.connect('coffee.db')

        cur = self.con.cursor()
        result = cur.execute(f"""SELECT * FROM Coffee""").fetchall()
        self.number_of_varieties = len(result)
        self.number_of_lines = len(result[0])

        self.info = result

        self.show_table()

    def update(self):
        self.update_window = UpdateWindow()
        self.update_window.setWindowModality(Qt.ApplicationModal)


class UpdateWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initDB()

    def initUI(self):
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.ok_btn.clicked.connect(self.update)
        self.show()

    def initDB(self):
        self.con = sqlite3.connect('coffee.db')

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