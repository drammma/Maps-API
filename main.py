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
        self.coordX.setText('10.7461'), self.coordY.setText('59.9127'), self.coordZ.setValue(16)
        self.Button.clicked.connect(self.generation_map)
        self.keyboard.stateChanged.connect(self.keyboard_ON)

    def keyboard_ON(self):
        if self.keyboard.isChecked():
            self.coordX.setEnabled(False)
            self.coordY.setEnabled(False)
            self.coordZ.setEnabled(False)
        else:
            self.coordX.setEnabled(True)
            self.coordY.setEnabled(True)
            self.coordZ.setEnabled(True)

    def generation_map(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.coordX.text()},{self.coordY.text()}&z={self.coordZ.text()}&l=sat"
        response = requests.get(map_request)
        self.map_file = "map.png"

        with open(self.map_file, "wb") as image:
            image.write(response.content)
            self.pixmap = QPixmap(self.map_file)
            self.picture.setPixmap(self.pixmap)
        os.remove(self.map_file)

    def keyPressEvent(self, event):
        self.pos_x, self.pos_y = 0, 0
        if self.keyboard.isChecked():
            if event.key() == Qt.Key_W:
                self.pos_y = -0.01
            if event.key() == Qt.Key_S:
                self.pos_y = 0.01
            if event.key() == Qt.Key_A:
                self.pos_x = 0.01
            if event.key() == Qt.Key_D:
                self.pos_x = -0.01
            new_pos_x = float(self.coordX.text().replace(',', '.')) + self.pos_x
            new_pos_y = float(self.coordY.text().replace(',', '.')) + self.pos_y
            self.coordX.setText(str(new_pos_x))
            self.coordY.setText(str(new_pos_y))

            if event.key() == Qt.Key_PageUp:
                self.coordZ.setValue(int(self.coordZ.text()) + 1)
            if event.key() == Qt.Key_PageDown:
                self.coordZ.setValue(int(self.coordZ.text()) - 1)
            self.generation_map()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.excepthook = except_hook
    sys.exit(application.exec())
