import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from random import randrange
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp):
        size = randrange(20, 400)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(265 - size // 2, 250 - size // 2, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())