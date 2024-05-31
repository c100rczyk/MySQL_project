
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
from login_process import LoginProcess
import sys
from connect_mysql import ConnectMySQL
from logowanie_PyQt import AplikacjaTreningowa

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QApplication, QVBoxLayout, QFrame, QHBoxLayout,
                              QLineEdit, QGridLayout)



def handle_login():
    input_login = app1.get_putted_login()
    input_password = app1.get_putted_password()

    login_to = LoginProcess(mycoursor)
    login_to.login_to_app(input_login, input_password)

#def handle_register():


if __name__ == "__main__":

    # Łączenie z bazą danych
    mydb_connect = ConnectMySQL(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    mydb = mydb_connect.connect()

    # Uruchomienie aplikacji
    app = QApplication(sys.argv)
    app1 = AplikacjaTreningowa(handle_login)

    #Porusznie się po Bazie danych
    mycoursor = mydb.cursor()
    print(f"mycoursor {mycoursor}")


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


#TODO
#czekać na naciśnięcie przycisku zaloguj sie
#pobrać dane z pola tekstowego haslo
#sprawdzic haslo z tym z bazy danych
#podjąc decyzję o logowaniu