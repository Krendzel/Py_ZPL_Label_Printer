from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog, QLabel, QGroupBox, QSplitter, QComboBox, QPushButton, QLineEdit, QSpinBox, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import sys
import os
from os.path import isfile
import glob
import socket

class UI(QMainWindow):


    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('untitled.ui', self)

        self.button = self.findChild(QPushButton, 'pushButton')
        self.print_template_btn = self.findChild(QPushButton, 'print_template_btn')
        self.label = self.findChild(QLabel, 'label')
        self.templates_combo = self.findChild(QComboBox, 'template_select')
        self.ean_input = self.findChild(QLineEdit, 'ean_input')
        self.qty_input = self.findChild(QSpinBox, 'qty_input')

        self.tableWidget = self.findChild(QTableWidget, 'tableWidget')
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 150)

        self.print_template_btn.clicked.connect(lambda: self.print_template(self.templates_combo.currentData()))
        self.button.clicked.connect(lambda: self.msg_box(self.templates_combo.currentData()))


        for file in glob.glob('templates/*.txt'):
            if isfile(file):
                filename = os.path.basename(file)
                full_path = file
                self.templates_combo.addItem(filename, full_path)

        self.load_data_from_file()

        self.show()

    def load_data_from_file(self):
        slots = [{'col_1': 'name', 'col_2': 'John'}, {'col_1': 'surname', 'col_2': 'Doe'}]
        row = 0
        self.tableWidget.setRowCount(len(slots))

        for slot in slots:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(slot['col_1'], ))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(slot['col_2'], ))
            row=row+1

    # List templates
    def list_templates(self, path):
        pass

    def print_template(self, path):
        variables = []
        with open(path, 'r') as f:
            data = f.read()

            data = data.replace('@EAN', self.ean_input.text())
            data = data.replace('@QTY', self.qty_input.text())
            print(data)
            self.print_zpl_label(data)



    def msg_box(self, text):
        print(text)
        self.label.setText(str(text))
        # QMessageBox('Title', str(self.templates_combo.currentData()))

    def print_zpl_label(self, label):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket object
        host = "127.0.0.1"
        port = 9100
        try:
            mysocket.connect((host, port))  # connecting to host
            mysocket.send(bytes(label, encoding='utf-8'))  # using bytes
            mysocket.close()  # closing connection
        except:
            print("Error with the connection")

app = QApplication(sys.argv)
UIWindow = UI()
sys.exit(app.exec_())