import pandas as pd
import numpy as np
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget,
    QTableWidgetItem, QHBoxLayout, QSpinBox
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PopulationStatsTab(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.label = QLabel("Нажмите 'Собрать статистику', чтобы отобразить данные")
        self.layout.addWidget(self.label)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.plot_widget = FigureCanvas(Figure(figsize=(5, 3)))
        self.ax = self.plot_widget.figure.add_subplot(111)
        self.layout.addWidget(self.plot_widget)

        control_layout = QHBoxLayout()
        self.n_label = QLabel("Прогноз на N лет:")
        control_layout.addWidget(self.n_label)
        self.n_spinbox = QSpinBox()
        self.n_spinbox.setRange(1, 20)
        self.n_spinbox.setValue(5)
        control_layout.addWidget(self.n_spinbox)
        self.layout.addLayout(control_layout)

        self.button = QPushButton("Собрать статистику")
        
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)


