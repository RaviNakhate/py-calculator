from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        uic.loadUi('calculator.ui', self)

        self.pushButton_0 = self.findChild(QPushButton, 'pushButton_0')
        self.pushButton_1 = self.findChild(QPushButton, 'pushButton_1')
        self.pushButton_2 = self.findChild(QPushButton, 'pushButton_2')
        self.pushButton_3 = self.findChild(QPushButton, 'pushButton_3')
        self.pushButton_4 = self.findChild(QPushButton, 'pushButton_4')
        self.pushButton_5 = self.findChild(QPushButton, 'pushButton_5')
        self.pushButton_6 = self.findChild(QPushButton, 'pushButton_6')
        self.pushButton_7 = self.findChild(QPushButton, 'pushButton_7')
        self.pushButton_8 = self.findChild(QPushButton, 'pushButton_8')
        self.pushButton_9 = self.findChild(QPushButton, 'pushButton_9')
        self.pushButton_add = self.findChild(QPushButton, 'pushButton_sum')
        self.pushButton_subtract = self.findChild(QPushButton, 'pushButton_subtract')
        self.pushButton_multiply = self.findChild(QPushButton, 'pushButton_multiply')
        self.pushButton_divide = self.findChild(QPushButton, 'pushButton_divide')
        self.pushButton_equals = self.findChild(QPushButton, 'pushButton_result')
        self.pushButton_clear = self.findChild(QPushButton, 'pushButton_clear')

        self.pushButton_0.clicked.connect(self.number_click)
        self.pushButton_1.clicked.connect(self.number_click)
        self.pushButton_2.clicked.connect(self.number_click)
        self.pushButton_3.clicked.connect(self.number_click)
        self.pushButton_4.clicked.connect(self.number_click)
        self.pushButton_5.clicked.connect(self.number_click)
        self.pushButton_6.clicked.connect(self.number_click)
        self.pushButton_7.clicked.connect(self.number_click)
        self.pushButton_8.clicked.connect(self.number_click)
        self.pushButton_9.clicked.connect(self.number_click)

        self.pushButton_add.clicked.connect(self.number_click)
        self.pushButton_subtract.clicked.connect(self.number_click)
        self.pushButton_multiply.clicked.connect(self.number_click)
        self.pushButton_divide.clicked.connect(self.number_click)

        self.pushButton_equals.clicked.connect(self.equals_click)
        self.pushButton_clear.clicked.connect(self.clear_click)

        self.lineEdit = self.findChild(QLineEdit, "output")
        self.reset_calculator()
        self.previous_char = None

    def reset_calculator(self):
        self.lineEdit.setText(None)

    def number_click(self):
        button = self.sender()
        char = button.text()

        if char.isdigit():
            self.lineEdit.setText(self.lineEdit.text() + char)
            self.previous_char = char
        elif self.previous_char.isdigit():
            self.lineEdit.setText(self.lineEdit.text() + char)
            self.previous_char = char

    def equals_click(self):
        expression = self.lineEdit.text()
        try:
            result = str(eval(expression))
            self.lineEdit.setText(result)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Error")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.lineEdit.setText(None)
        self.previous_char = None

    def clear_click(self):
        self.reset_calculator()


# app = QApplication(sys.argv)
# widget = MyWindow()
# widget.show()
# app.exec_()
if __name__ == "__main__":
    app = QApplication([])
    calculator = MyWindow()
    calculator.show()
    app.exec_()
