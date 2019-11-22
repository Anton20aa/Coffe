from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLineEdit
import sqlite3
import sys
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.swowCoffe)
        self.connect = sqlite3.connect("coffee.sqlite")
        self.cursor = self.connect.cursor()

    def swowCoffe(self):
        coffee = self.cursor.execute(
            """SELECT * FROM coffee WHERE sort = '{0}'""".format(self.lineEdit.text())).fetchall()
        self.fillTable(coffee)
        self.tableWidget.resizeColumnsToContents()

    def fillTable(self, data):
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        self.tableWidget.setItem(0, 0, QTableWidgetItem(data[0][0]))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(str(data[0][1])))
        self.tableWidget.setItem(0, 2, QTableWidgetItem(str(data[0][2])))
        self.tableWidget.setItem(0, 3, QTableWidgetItem(str(data[0][3])))
        self.tableWidget.setItem(0, 4, QTableWidgetItem(data[0][4]))
        self.tableWidget.setItem(0, 5, QTableWidgetItem(str(data[0][5])))
        self.tableWidget.setItem(0, 6, QTableWidgetItem(str(data[0][6])))


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())