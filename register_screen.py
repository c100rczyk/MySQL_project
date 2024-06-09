from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, pyqtSignal
from database import register_user_database


class RegisterScreen(QWidget):
    registration_successful = pyqtSignal(str)
    back_to_login = pyqtSignal()

    def __init__(self):

        super().__init__()

        self.setWindowTitle('GymApp')
        self.resize(800, 600)

        self.layout = QVBoxLayout()

        self.image_label = QLabel(self)
        pixmap = QPixmap('gymapp.png')
        scaled_pixmap = pixmap.scaled(300, 100, Qt.KeepAspectRatio)
        self.image_label.setPixmap(scaled_pixmap)
        self.layout.addWidget(self.image_label, alignment=Qt.AlignCenter)

        self.login_label = QLabel('Login:')
        self.layout.addWidget(self.login_label, alignment=Qt.AlignCenter)

        self.login_input = QLineEdit()
        self.login_input.setFixedWidth(200)
        self.layout.addWidget(self.login_input, alignment=Qt.AlignCenter)

        self.password_label = QLabel('Hasło:')
        self.layout.addWidget(self.password_label, alignment=Qt.AlignCenter)

        self.password_input = QLineEdit()
        self.password_input.setFixedWidth(200)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input, alignment=Qt.AlignCenter)

        self.register_button = QPushButton('Zarejestruj się')
        self.register_button.setFixedWidth(150)
        self.register_button.clicked.connect(self.register_user)
        self.layout.addWidget(self.register_button, alignment=Qt.AlignCenter)

        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.back_button = QPushButton('Wróć do logowania')
        self.back_button.setFixedWidth(150)
        self.back_button.clicked.connect(self.show_login)
        self.layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

    def register_user(self):
        login = self.login_input.text()
        password = self.password_input.text()

        register_user_database(login, password)
        QMessageBox.information(self, 'Success', f'Registered {login}')
        # self.show_login()
        self.registration_successful.emit(login)

    def show_login(self):
        self.back_to_login.emit()
        # from login_screen import LoginScreen
        # self.login_screen = LoginScreen()
        # self.login_screen.show()
        # self.close()

    def clear_inputs(self):
        self.login_input.clear()
        self.password_input.clear()