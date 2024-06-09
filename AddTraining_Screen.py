from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QSpacerItem, QSizePolicy, \
    QComboBox,QDesktopWidget
from PyQt5.QtCore import Qt, pyqtSignal
from database import register_user_database, add_trening_database
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QGridLayout, QFrame)
from PyQt5.QtGui import QPixmap, QIcon


class AddTrainingScreen(QWidget):
    show_trening_signal = pyqtSignal()
    back_to_login2 = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle('GymApp')
        self.setFixedSize(500, 400)
        self.layout = QVBoxLayout()


        self.body_part_label = QLabel('Partia ciała:')
        self.layout.addWidget(self.body_part_label)
        self.wybor_partii_comboBox = QComboBox()
        self.wybor_partii_comboBox.addItem("Nogi")
        self.wybor_partii_comboBox.addItem("Plecy")
        self.wybor_partii_comboBox.addItem("Brzuch")
        self.wybor_partii_comboBox.addItem("Ręce")
        self.layout.addWidget(self.wybor_partii_comboBox)

        self.cwiczenie_label = QLabel("Nazwa cwiczenia:")
        self.layout.addWidget(self.cwiczenie_label)
        self.wybor_trening_comboBox = QComboBox()
        self.wybor_trening_comboBox.addItem("Shoulders Gotors")
        self.wybor_trening_comboBox.addItem("Push-up & rotation")
        self.wybor_trening_comboBox.addItem("Floor Tricep Dips")
        self.layout.addWidget(self.wybor_trening_comboBox)

        self.number_of_repeats_label = QLabel("Number of repeats:")
        self.layout.addWidget(self.number_of_repeats_label)
        self.number_of_repeats_text = QLineEdit()
        self.number_of_repeats_text.setFixedWidth(150)
        self.layout.addWidget(self.number_of_repeats_text)

        self.number_of_series_label = QLabel("Number of series")
        self.layout.addWidget(self.number_of_series_label)
        self.number_of_series_text = QLineEdit()
        self.number_of_series_text.setFixedWidth(150)
        self.layout.addWidget(self.number_of_series_text)

        self.weight_label = QLabel("Weight:")
        self.layout.addWidget(self.weight_label)
        self.weight_text = QLineEdit()
        self.weight_text.setFixedWidth(150)
        self.layout.addWidget(self.weight_text)

        self.time_label = QLabel("Time:")
        self.layout.addWidget(self.time_label)
        self.time_text = QLineEdit()
        self.time_text.setFixedWidth(150)
        self.layout.addWidget(self.time_text)

        self.button_add_trening = QPushButton("Dodaj Trening")
        self.button_add_trening.setFixedWidth(150)
        self.layout.addWidget(self.button_add_trening)
        self.button_add_trening.clicked.connect(self.add_trening)


        self.setLayout(self.layout)



    def add_trening(self):

        serie_input = self.number_of_series_text.text()
        repeats_input = self.number_of_repeats_text.text()
        weight_input = self.weight_text.text()
        time_input = self.time_text.text()
        partia_input = self.wybor_partii_comboBox.currentText()
        cwiczenie_input = self.wybor_trening_comboBox.currentText()


        add_trening_database(serie_input, weight_input, repeats_input, time_input,cwiczenie_input, partia_input)

        QMessageBox.information(self, "Dodano ćwiczenie", f"Wybor: {serie_input}")
        self.back_to_login2.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    add_training_show = AddTrainingScreen()
    add_training_show.show()
    sys.exit(app.exec_())




