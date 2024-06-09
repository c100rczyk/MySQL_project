import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from login_screen import LoginScreen
from register_screen import RegisterScreen
from main_screen import MainScreen
from AddTraining_Screen import AddTrainingScreen

class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.stack = QStackedWidget()       # tworzenie stosu widgetów

        self.login_screen = LoginScreen()
        self.login_screen.login_successful.connect(self.show_main_screen)
        #self.login_screen.register_button.clicked.connect(self.show_register_screen)
        self.login_screen.show_register_signal.connect(self.show_register_screen)

        self.register_screen = RegisterScreen()
        self.register_screen.registration_successful.connect(self.show_login_screen)
        self.register_screen.back_to_login.connect(self.show_login_screen)

        self.main_screen = None

        #TESTY
        self.training_screen = AddTrainingScreen()
        self.training_screen.show_trening_signal.connect(self.show_training_screen)
        self.training_screen.back_to_login2.connect(self.show_main_screen)


        self.stack.addWidget(self.login_screen)
        self.stack.addWidget(self.register_screen)
        self.stack.setFixedSize(800, 600)
        self.stack.show()

    def show_main_screen(self, username):
        self.main_screen = MainScreen(username)
        self.main_screen.logout_signal.connect(self.show_login_screen)
        self.main_screen.show_trening_signal.connect(self.show_training_screen)         #########

        self.stack.addWidget(self.main_screen)
        self.stack.setCurrentWidget(self.main_screen)

    def show_training_screen(self):
        #self.traning_screen = AddTrainingScreen()
        self.stack.addWidget(self.training_screen)
        self.stack.setCurrentWidget(self.training_screen)

    def show_login_screen(self):
        self.login_screen.clear_inputs()
        self.stack.setCurrentWidget(self.login_screen)
        if self.main_screen:
            self.stack.removeWidget(self.main_screen)
            self.main_screen = None

    def show_register_screen(self):
        self.register_screen.clear_inputs()
        self.stack.setCurrentWidget(self.register_screen)

    # def add_training_to_plan(self):


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
