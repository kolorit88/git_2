import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from random import randrange


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        screen_size = [1500, 900]
        self.setGeometry(100, 50, *screen_size)
        self.setFixedSize(*screen_size)
        self.btn = QPushButton('click', self)
        self.btn.move(700, 800)
        self.go_pain = False
        self.btn.clicked.connect(self.elips)

    def paintEvent(self, event):
        if self.go_pain:
            self.paint = QPainter()
            self.paint.begin(self)
            self.paint.setPen(QColor(238, 238, 0))
            self.paint.setBrush(QColor(205, 205, 0))
            self.paint.drawEllipse(randrange(1500), randrange(1000), randrange(100, 500), randrange(100, 500))
            self.paint.end()

    def elips(self):
        self.go_pain = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
