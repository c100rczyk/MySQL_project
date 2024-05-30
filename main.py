
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
from login_process import LoginProcess
import sys
from connect_mysql import ConnectMySQL
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QApplication, QVBoxLayout, QFrame, QHBoxLayout,
                              QLineEdit, QGridLayout)
import mysql.connector


class AplikacjaTreningowa(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def handle_login_process(self):
        self.wprowadzone_haslo = self.put_haslo_textBox.text()
        self.wprowadzony_login = self.put_login_textBox.text()
        print("wprowadzony_login", self.wprowadzony_login)
        print("wprowadzone_haslo", self.wprowadzone_haslo)
        handle_login()


    def get_putted_password(self):
        return self.wprowadzone_haslo
    def get_putted_login(self):
        return self.wprowadzony_login

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
        self.put_login_textBox = QLineEdit(self.middleBar)
        self.put_login_textBox.setFixedWidth(290)
        self.put_login_textBox.setFixedHeight(30)
        main_panel.addWidget(self.put_login_textBox)

        self.haslo_label = QLabel("Haslo: " ,self.middleBar)
        main_panel.addWidget(self.haslo_label)
        self.put_haslo_textBox = QLineEdit(self.middleBar)
        self.put_haslo_textBox.setFixedWidth(290)
        self.put_haslo_textBox.setFixedHeight(30)
        main_panel.addWidget(self.put_haslo_textBox)

        self.zaloguj_sie_button = QPushButton("Zaloguj sie", self.middleBar)
        main_panel.addWidget(self.zaloguj_sie_button)
        self.zaloguj_sie_button.setStyleSheet("background-color : blue")

        #JEŚLI NACISNĘ PRZYCISK "ZALOGU SIE"
        self.zaloguj_sie_button.clicked.connect(self.handle_login_process)


        main_panel.addLayout(central_layout)
        self.setLayout(main_panel)
        self.show()


# Uruchomienie aplikacji
app = QApplication(sys.argv)
app1 = AplikacjaTreningowa()

# Łączenie z bazą danych
mydb_connect = ConnectMySQL(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
mydb = mydb_connect.connect()

#Porusznie się po Bazie danych
mycoursor = mydb.cursor()
print(f"mycoursor {mycoursor}")



#TODO
#czekać na naciśnięcie przycisku zaloguj sie
#pobrać dane z pola tekstowego haslo
#sprawdzic haslo z tym z bazy danych
#podjąc decyzję o logowaniu


def handle_login():
    input_login = app1.get_putted_login()
    input_password = app1.get_putted_password()

    login_to = LoginProcess(mycoursor)
    login_to.login_to_app(input_login, input_password)




sys.exit(app.exec_())











# SHOW ALL DATABASES
# mycoursor.execute("SHOW DATABASES")
#
# for i in mycoursor:
#     print(i)

# DODANIE UZYTKOWNIKA DO BAZY DANYCH
# sql = "INSERT INTO uzytkownik (login, haslo, rodzaj_konta) VALUES (%s, %s, %s)"
# val = ("InnyFilip", "bim222", 0)
# mycoursor.execute(sql,val)
# mydb.commit()
# print(mycoursor.rowcount, "record inserted.")



# WYBRANIE DANYCH Z TABELI
