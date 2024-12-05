import sqlite3
import traceback
import random
import sys

from PyQt6 import uic
from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QPushButton
from forma import Ui_MainWindow

class Yellow_circle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.push_button)
        self.button_is_pushed = False

    def paintEvent(self, event):
        if self.button_is_pushed:
            qp = QPainter()
            qp.begin(self)
            self.circle(qp)
            qp.end()
        self.button_is_pushed = False


    def push_button(self):
        self.button_is_pushed = True
        self.update()

    def circle(self, qp: QPainter):
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        radius = random.randint(1, 800)
        qp.drawEllipse(QPoint(random.randint(1, 800), random.randint(1, 800)), radius, radius)

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Oбнаружена ошибка !:", tb)

if __name__ == '__main__':
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = Yellow_circle()
    ex.show()
    sys.exit(app.exec())