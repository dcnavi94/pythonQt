from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QLabel
from PyQt5.QtCore import Qt
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('Ventana QCheckBox')
        self.setGeometry(100, 100, 250, 200)
        self.mostrarWidgets()

    def mostrarWidgets(self):
        label = QLabel('¿Qué tipo de helado quieres', self)
        label.resize(250,60)
        label.setAlignment(Qt.AlignCenter)
        
        VANILLA = QCheckBox('Vainilla', self)
        VANILLA.move(20, 80)
        CHOCOLATE = QCheckBox('Chocolate', self)
        CHOCOLATE.move(20, 100)
        FRESA = QCheckBox('Fresa', self)
        FRESA.move(20, 120)
        
        VANILLA.StateChanged.connect(self.mostrarEstado)
        CHOCOLATE.StateChanged.connect(self.mostrarEstado)
        FRESA.StateChanged.connect(self.mostrarEstado)
        
    def mostrarEstado(self):
        sender = self.sender()
        if estado := sender.isChecked():
            print(f'{sender.text()} seleccionado')
        else:
            print(f'{sender.text()} deseleccionado')
            
if __name__ == '__main__':
    app = QApplication(sys.argv) 
    ventana = Aplicacion()
    ventana.show()
    sys.exit(app.exec_())