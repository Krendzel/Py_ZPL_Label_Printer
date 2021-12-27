from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog, QLabel, QGroupBox, QSplitter, QComboBox, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import sys

class UI(QMainWindow):


    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('untitled.ui', self)

        self.button = self.findChild(QPushButton, 'pushButton')
        self.label = self.findChild(QLabel, 'label_2')



        self.button.clicked.connect(self.msg_box)
        self.button.clicked.connect(lambda: self.msg_box('sdsd'))
        self.combobox = self.findChild(QComboBox, 'printer_select')
        # for i in range(1, 11):
        #     self.combobox.addItem(str(i), i)

        self.show()


    def msg_box(self, text):
        self.label.setText(text)
        QMessageBox.information(self, 'Title', self.combobox.currentData())

app = QApplication(sys.argv)
UIWindow = UI()
sys.exit(app.exec_())