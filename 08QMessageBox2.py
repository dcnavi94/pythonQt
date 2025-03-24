from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setWindowTitle('Ventana QMessageBox')
        self.setGeometry(100, 100, 340, 200)
        self.mostrarWidgets()
        
    def mostrarWidgets(self):
        