import os

import sys
import requests

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from DesignUI import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Большая задача по Maps API.')
        self.num = 0

        self.pushButton.clicked.connect(self.generation_map)

    def generation_map(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.line_coordinateX.text()},{self.line_coordinateY.text()}&z={self.sbox_coordinateZ.text()}&l=map"
        response = requests.get(map_request)
        self.map_file = "map.png"

        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.display_map()

    def display_map(self):
        self.pixmap = QPixmap(self.map_file)
        self.picture.setPixmap(self.pixmap)
        os.remove(self.map_file)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.num = 1
        if event.key() == Qt.Key_PageDown:
            self.num = -1
        self.sbox_coordinateZ.setValue(int(self.sbox_coordinateZ.text()) + self.num)
        self.generation_map()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.excepthook = except_hook
    sys.exit(application.exec())
