import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTabWidget,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Статистика по заданию")
        self.resize(900, 600)

        layout = QVBoxLayout()

        self.tabs = QTabWidget()

        # Сюда можно добавлять другие вкладки

        layout.addWidget(self.tabs)
        self.setLayout(layout)

