from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
import sys

class VentanaBoton(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize()
        
    def initialize(self):
        self.setWindowTitle('Ventana con Botón')
        self.setGeometry(100, 100, 300, 200)
        self.displayButton()
    def displayButton(self):
        button = QPushButton( self)
        button.setText('Presiona')
        button.move(100, 100)
        button.clicked.connect(self.on_button_click)
    def on_button_click(self):
        print('Botón presionado')
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaBoton()
    ventana.show()
    sys.exit(app.exec_())