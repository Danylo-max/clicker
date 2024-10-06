import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer

class ClickerGame(QWidget):
    def __init__(self):
        super().__init__()

        self.click_count = 0
        self.time_left = 10  # Время игры (секунды)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        
        self.cps_timer = QTimer(self)
        self.cps_timer.timeout.connect(self.update_cps)

        self.cps_count = 0  # Количество кликов за текущую секунду
        self.cps = 0  # CPS (clicks per second)

        self.init_ui()

    def init_ui(self):
        # Настройка интерфейса
        self.setWindowTitle('Clicker Game')
        self.setGeometry(100, 100, 300, 250)

        layout = QVBoxLayout()

        self.label = QLabel('Нажмите "Начать игру", чтобы начать!', self)
        layout.addWidget(self.label)

        self.start_button = QPushButton('Начать игру', self)
        self.start_button.setFixedWidth(200)
        self.start_button.clicked.connect(self.start_game)
        layout.addWidget(self.start_button)

        self.click_button = QPushButton('Кликни меня!', self)
        self.click_button.setFixedWidth(200)
        self.click_button.setEnabled(False)
        self.click_button.clicked.connect(self.on_click)
        layout.addWidget(self.click_button)

        self.score_label = QLabel('Клики: 0', self)
        layout.addWidget(self.score_label)

        self.cps_label = QLabel('CPS: 0', self)  # Метка для отображения CPS
        layout.addWidget(self.cps_label)

        self.time_label = QLabel(f'Осталось времени: {self.time_left} секунд', self)
        layout.addWidget(self.time_label)

        self.setLayout(layout)

    def on_click(self):
        if self.time_left > 0:
            self.click_count += 1
            self.score_label.setText(f'Клики: {self.click_count}')
            self.cps_count += 1  # Увеличиваем количество кликов за текущую секунду

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.setText(f'Осталось времени: {self.time_left} секунд')
        else:
            self.timer.stop()
            self.cps_timer.stop()  # Останавливаем таймер CPS
            self.click_button.setEnabled(False)
            self.time_label.setText('Время вышло!')
            self.label.setText(f'Игра окончена! Ваш счёт: {self.click_count}.\nВаш средний CPS: {self.cps:.2f}')

    def update_cps(self):
        self.cps = self.cps_count  # Обновляем CPS
        self.cps_label.setText(f'CPS: {self.cps}')  # Обновляем метку CPS
        self.cps_count = 0  # Сбрасываем количество кликов за текущую секунду

    def start_game(self):
        self.click_count = 0
        self.time_left = 10
        self.click_button.setEnabled(True)
        self.score_label.setText(f'Клики: {self.click_count}')
        self.cps_label.setText('CPS: 0')  # Сбрасываем метку CPS
        self.time_label.setText(f'Осталось времени: {self.time_left} секунд')
        self.label.setText('Нажимайте "Кликни меня", как можно быстрее!')
        self.timer.start(1000)  # Таймер обновляется каждую секунду
        self.cps_timer.start(1000)  # Таймер CPS обновляется каждую секунду

def main():
    app = QApplication(sys.argv)
    game = ClickerGame()
    game.show()
    sys.exit(app.exec_())

    app.exec()



