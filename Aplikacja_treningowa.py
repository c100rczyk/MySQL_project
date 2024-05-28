

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QApplication, QVBoxLayout, QFrame, QHBoxLayout,
                              QLineEdit, QGridLayout)


import mysql.connector


class AplikacjaTreningowa(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplikacja do zarządzania treningami')
        self.setGeometry(500,500, 1000,700)

        # ramka panelu głównego
        self.middleBar = QFrame(self)
        self.middleBar.setFrameShape(QFrame.StyledPanel)
        self.middleBar.setFixedWidth(340)
        self.middleBar.setFixedHeight(500)
        self.middleBar.setAutoFillBackground(True)
        palette = self.middleBar.palette()
        palette.setColor(QPalette.Background, QColor(210,210,210))
        self.middleBar.setPalette(palette)

        central_layout = QHBoxLayout()
        central_layout.addStretch(1)
        central_layout.addWidget(self.middleBar)
        central_layout.addStretch(1)


        # ramka pionowa
        main_panel = QVBoxLayout()


        # Wyświetlanie obrazu
        self.image_logo = QLabel(self)
        pixmap = QPixmap('Logo_app.png')
        self.image_logo.setPixmap(pixmap)
        self.image_logo.setAlignment(Qt.AlignHCenter)
        main_panel.addWidget(self.image_logo)


        self.login_label = QLabel("Login: ", self.middleBar)
        main_panel.addWidget(self.login_label)
        self.put_login = QLineEdit(self.middleBar)
        self.put_login.setFixedWidth(290)
        self.put_login.setFixedHeight(30)
        main_panel.addWidget(self.put_login)

        self.haslo_label = QLabel("Haslo: " ,self.middleBar)
        main_panel.addWidget(self.haslo_label)
        self.put_haslo = QLineEdit(self.middleBar)
        self.put_haslo.setFixedWidth(290)
        self.put_haslo.setFixedHeight(30)
        main_panel.addWidget(self.put_haslo)

        main_panel.addLayout(central_layout)
        self.setLayout(main_panel)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app1 = AplikacjaTreningowa()
    sys.exit(app.exec_())
