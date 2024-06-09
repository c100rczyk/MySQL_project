from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QSpacerItem, QSizePolicy, QDesktopWidget
from database import get_user_by_login
from PyQt5.QtCore import Qt, pyqtSignal


class LoginScreen(QWidget):
    login_successful = pyqtSignal(str)
    show_register_signal = pyqtSignal()     # inicjalizacja nowego sygnału

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

        # Add a spacer item before the elements to push them towards the center
        # self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.login_label = QLabel('Login:')
        self.layout.addWidget(self.login_label, alignment=Qt.AlignCenter)

        self.login_input = QLineEdit()
        self.login_input.setFixedWidth(200)
        self.layout.addWidget(self.login_input, alignment=Qt.AlignCenter)

        self.password_label = QLabel('Hasło:')
        self.layout.addWidget(self.password_label, alignment=Qt.AlignCenter)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedWidth(200)
        self.layout.addWidget(self.password_input, alignment=Qt.AlignCenter)

        self.login_button = QPushButton('Zaloguj się')
        self.login_button.setFixedWidth(150)
        self.layout.addWidget(self.login_button, alignment=Qt.AlignCenter)
        self.login_button.clicked.connect(self.check_login)

        # Add a spacer item after the elements to push them towards the center
        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.password_label = QLabel('Nie masz konta?')
        self.layout.addWidget(self.password_label, alignment=Qt.AlignCenter)

        self.register_button = QPushButton('Zarejestruj się')
        self.register_button.setFixedWidth(150)
        self.layout.addWidget(self.register_button, alignment=Qt.AlignCenter)
        self.register_button.clicked.connect(self.show_register)

        self.setLayout(self.layout)
        # self.center()     # w sumie niepotrzbne, bo domyslnie srodkuje

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def check_login(self):
        self.login = self.login_input.text()
        password = self.password_input.text()
        user = get_user_by_login(self.login)
        if user:
            print(f"Fetched user: {user}")
            if 'haslo' in user and user['haslo'] == password:
                # from main_screen import MainScreen  # Import here to avoid circular import
                # self.main_screen = MainScreen(login)
                # self.main_screen.show()
                # self.close()
                self.login_successful.emit(self.login)
            else:
                QMessageBox.warning(self, 'Error', 'Invalid password')
        else:
            QMessageBox.warning(self, 'Error', 'Invalid username')

    # def show_register(self):
    #     from register_screen import RegisterScreen  # Import here to avoid circular import
    #     self.register_screen = RegisterScreen()
    #     self.register_screen.show()
    #     self.close()

    def show_register(self):
        # QMessageBox.information(self, 'Register', 'Registration functionality not implemented yet')
        self.show_register_signal.emit()

    def clear_inputs(self):
        self.login_input.clear()
        self.password_input.clear()