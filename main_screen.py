import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QGridLayout, QFrame, QListWidget, QListWidgetItem)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal


class MainScreen(QMainWindow):
    logout_signal = pyqtSignal()
    show_trening_signal = pyqtSignal()

    def __init__(self, login):
        super().__init__()
        self.login = login
        self.setWindowTitle('GymApp')
        self.setFixedSize(800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QHBoxLayout(self.central_widget)

        # Left Navigation Panel
        nav_panel = QVBoxLayout()

        # Plan treningu Button
        self.plan_button = QPushButton("Plan treningu")
        # plan_button.setIcon(QIcon('plan_icon.png'))
        # plan_button.setStyleSheet("font-size: 18px; text-align: left; padding: 10px;")
        # plan_button.setIconSize(plan_button.sizeHint())
        self.plan_button.clicked.connect(self.create_trening_screen)
        nav_panel.addWidget(self.plan_button)

        # Dodaj trening Button
        add_button = QPushButton("Dodaj trening")
        # add_button.setIcon(QIcon('add_icon.png'))  # Ensure you have the icon file
        # add_button.setStyleSheet("font-size: 18px; text-align: left; padding: 10px;")
        # add_button.setIconSize(add_button.sizeHint())
        nav_panel.addWidget(add_button)

        # Statystyki Button
        stats_button = QPushButton("Statystyki")
        # stats_button.setIcon(QIcon('stats_icon.png'))  # Ensure you have the icon file
        # stats_button.setStyleSheet("font-size: 18px; text-align: left; padding: 10px;")
        # stats_button.setIconSize(stats_button.sizeHint())
        nav_panel.addWidget(stats_button)

        nav_panel.addStretch()

        # Wyloguj się Button
        logout_button = QPushButton("Wyloguj się")
        # logout_button.setIcon(QIcon('logout_icon.png'))  # Ensure you have the icon file
        # logout_button.setStyleSheet("font-size: 18px; text-align: left; padding: 10px;")
        # logout_button.setIconSize(logout_button.sizeHint())
        logout_button.clicked.connect(self.logout)
        nav_panel.addWidget(logout_button)

        # Left Panel Frame
        nav_frame = QFrame()
        nav_frame.setLayout(nav_panel)
        nav_frame.setFixedWidth(160)
        nav_frame.setStyleSheet("background-color: darkGray; color: white;")

        main_layout.addWidget(nav_frame)

        # Main Content
        content_layout = QVBoxLayout()

        # Title Layout
        title_layout = QHBoxLayout()

        logo = QLabel()
        pixmap = QPixmap('gymapp.png').scaled(300, 60, Qt.KeepAspectRatio)
        logo.setPixmap(pixmap)
        title_layout.addWidget(logo)

        # title = QLabel('GymApp')
        # title.setStyleSheet("font-size: 36px; font-weight: bold;")
        # title_layout.addWidget(title)

        # title_layout.addStretch()

        user_label = QLabel(f'użytkownik: \n{login}')
        user_label.setFixedHeight(80)
        user_label.setFixedWidth(120)
        user_label.setStyleSheet("font-size: 15px; color: black; padding: 5px;")
        title_layout.addWidget(user_label)

        content_layout.addLayout(title_layout)



        # # Calendar Placeholder
        # calendar_layout = QGridLayout()
        #
        # # Month Label
        # month_label = QLabel('Styczeń 1 - 7')
        # month_label.setStyleSheet("font-size: 18px; padding: 10px;")
        # calendar_layout.addWidget(month_label, 0, 1, 1, 5, Qt.AlignCenter)
        #
        # # Navigation Arrows
        # left_arrow = QPushButton('<')
        # left_arrow.setFixedSize(50, 30)
        # calendar_layout.addWidget(left_arrow, 0, 0)
        #
        # right_arrow = QPushButton('>')
        # right_arrow.setFixedSize(50, 30)
        # calendar_layout.addWidget(right_arrow, 0, 7)
        #
        # # Week Days Labels
        # days = ['Pn 1', 'Wt 2', 'Sr 3', 'Cz 4', 'Pt 5', 'Sb 6', 'Nd 7']
        # for i, day in enumerate(days):
        #     day_label = QLabel(day)
        #     day_label.setStyleSheet("font-size: 14px; padding: 5px;")
        #     calendar_layout.addWidget(day_label, 1, i+1)
        #
        # # Time Slots and Events (Placeholder for actual implementation)
        # times = ['8:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00']
        # for i, time in enumerate(times):
        #     time_label = QLabel(time)
        #     time_label.setStyleSheet("font-size: 12px; padding: 5px;")
        #     calendar_layout.addWidget(time_label, i + 2, 0)
        #
        # # Dostępne do wprowadzenia w okienkach [2-pn do 8-nd   w godzinach 1-8:00 do 7-20:00]
        # events = [
        #     (2, 1, "8:00-10:00\nKlatka\nBarki\nTriceps"),
        #     (2, 2, "\n\n"),
        #     (2, 3, "\n\n"),
        #     (2, 4, "11:00-12:30\nNogi\nBrzuch"),
        #     (2, 5, "\n\n"),
        #     (2, 6, "\n\n"),
        #     (2, 7, "\n\n"),
        #     (3, 1, "\n\n"),
        #     (3, 2, "\n\n"),
        #     (3, 3, "\n\n"),
        #     (3, 4, "\n\n"),
        #     (3, 5, "\n\n"),
        #     (3, 6, "\n\n"),
        #     (3, 7, "\n\n"),
        #     (4, 1, "\n\n"),
        #     (4, 2, "\n\n"),
        #     (4, 3, "\n\n"),
        #     (4, 4, "\n\n"),
        #     (4, 5, "\n\n"),
        #     (4, 6, "\n\n"),
        #     (4, 7, "\n\n"),
        #     (5, 1, "16:00-18:00\nPlecy\nBiceps"),
        #     (5, 2, "\n\n"),
        #     (5, 3, "\n\n"),
        #     (5, 4, "\n\n"),
        #     (5, 5, "\n\n"),
        #     (5, 6, "\n\n"),
        #     (5, 7, "\n\n"),
        #     (6, 1, "\n\n"),
        #     (6, 2, "\n\n"),
        #     (6, 3, "\n\n"),
        #     (6, 4, "\n\n"),
        #     (6, 5, "\n\n"),
        #     (6, 6, "\n\n"),
        #     (6, 7, "\n\n"),
        #     (7, 1, "\n\n"),
        #     (7, 2, "\n\n"),
        #     (7, 3, "\n\n"),
        #     (7, 4, "\n\n"),
        #     (7, 5, "\n\n"),
        #     (7, 6, "\n\n"),
        #     (7, 7, "\n\n"),
        # ]
        #
        # for row, col, event in events:
        #     event_label = QPushButton(event)
        #     event_label.setStyleSheet("background-color: lightgrey; padding: 5px;")
        #     calendar_layout.addWidget(event_label, row, col)
        #
        # content_layout.addLayout(calendar_layout)
        #

        list_of_trainings = QListWidget()
        content_layout.addWidget(list_of_trainings)

        main_layout.addLayout(content_layout)

    def logout(self):
        self.logout_signal.emit()

    def create_trening_screen(self):
        self.show_trening_signal.emit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    username = 'login_użyt'  # Przykładowa nazwa użytkownika
    main_screen = MainScreen(username)
    main_screen.show()
    sys.exit(app.exec_())
