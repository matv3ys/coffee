import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initDB()
        self.initUI()

    def initUI(self):
        uic.loadUi('main.ui', self)

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
        self.show()

    def initDB(self):
        self.con = sqlite3.connect('coffee.db')

        cur = self.con.cursor()
        result = cur.execute(f"""SELECT * FROM Coffee""").fetchall()
        self.number_of_varieties = len(result)
        self.number_of_lines = len(result[0])

        self.info = result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
