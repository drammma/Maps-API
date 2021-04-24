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
        self.Button.clicked.connect(self.generation_map)
        self.keyboard.stateChanged.connect(self.keyboard_ON)
        self.types_cart = {'Спутник': 'sat', 'Гибрид': 'skl', 'Схема': 'map'}

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
        if self.Address_line:
            # Москва, ул. Ак. Королева, 12
            toponym_to_find = '+'.join(self.Address_line.text().split())
            geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
            geocoder_params = {
                "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                "geocode": toponym_to_find,
                "format": "json"}
            response = requests.get(geocoder_api_server, params=geocoder_params)

            json_response = response.json()
            toponym = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]
            toponym_coodrinates = toponym["Point"]["pos"]
            toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
            map_params = {
                "ll": ",".join([toponym_longitude, toponym_lattitude]),
                "z": self.coordZ.text(),
                "l": self.types_cart[self.type_cart.currentText()]
            }
            self.coordX.setText(str(toponym_longitude))
            self.coordY.setText(str(toponym_lattitude))
            api_server = "http://static-maps.yandex.ru/1.x/"
            map_request = requests.get(api_server, params=map_params)
            self.map_file = "map.png"

        else:
            api_server = 'http://static-maps.yandex.ru/1.x/'
            params = {
                "ll": ",".join([self.coordX.text(), self.coordY.text()]),
                "z": self.coordZ.text(),
                "l": self.types_cart[self.type_cart.currentText()]
            }
            map_request = requests.get(api_server, params=params)
            self.map_file = "map.png"


        with open(self.map_file, "wb") as image:
            image.write(map_request.content)
            self.pixmap = QPixmap(self.map_file)
            self.picture.setPixmap(self.pixmap)
        os.remove(self.map_file)

    def keyPressEvent(self, event):
        self.pos_x, self.pos_y = 0, 0
        if self.keyboard.isChecked():
            if event.key() == Qt.Key_Up:
                self.pos_y = -1
            if event.key() == Qt.Key_Down:
                self.pos_y = 1
            if event.key() == Qt.Key_Right:
                self.pos_x = 1
            if event.key() == Qt.Key_Left:
                self.pos_x = -1
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
