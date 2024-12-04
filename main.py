import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("мяу мяу мяу")
        self.setGeometry(100, 100, 400, 300)
        self.pushButton = QPushButton("рисовать", self)
        self.pushButton.setGeometry(150, 130, 100, 30)
        self.pushButton.clicked.connect(self.draw_circle)
        self.circles = []

    def draw_circle(self):
        x = random.randint(50, 350)
        y = random.randint(50, 250)
        diameter = random.randint(10, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
