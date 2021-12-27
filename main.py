import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        # Set the layout
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)
        # Add label
        my_label = qtw.QLabel("Hello World!")
        my_label2 = qtw.QLabel("Hello World!2")
        layout.addWidget(my_label)

        # Add input field
        input_field = qtw.QLineEdit()
        input_field.setPlaceholderText("Enter text here")
        input_field.setObjectName("input_field")
        layout.addWidget(input_field)

        # Add combobox
        combo_box = qtw.QComboBox()
        combo_box.addItem("Item 1", "10.213.34.5")
        combo_box.addItem("Item 2", "10.213.34.2")

        layout.addWidget(combo_box)

        # Add button
        button = qtw.QPushButton("Click me!", clicked= lambda:on_button_clicked())
        layout.addWidget(button)

        self.show()

        def msg_box(text):
            msg = qtw.QMessageBox()
            # msg.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel | qtw.QMessageBox.Retry)
            # msg.setDetailedText("details")
            msg.setText(text)
            msg.exec_()

        def on_button_clicked():
            msg_box(f'combo: " {combo_box.currentText()} = {combo_box.currentData()} "')
            my_label.setText(combo_box.currentData())
            print("button clicked")


app = qtw.QApplication([])
mw = MainWindow()

app.exec()
