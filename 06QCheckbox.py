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
        
        self.VANILLA = QCheckBox('Vainilla', self)
        self.VANILLA.move(20, 80)
        self.CHOCOLATE = QCheckBox('Chocolate', self)
        self.CHOCOLATE.move(20, 100)
        self.FRESA = QCheckBox('Fresa', self)
        self.FRESA.move(20, 120)
        
        self.VANILLA.stateChanged.connect(self.mostrarEstado)
        self.CHOCOLATE.stateChanged.connect(self.mostrarEstado)
        self.FRESA.stateChanged.connect(self.mostrarEstado)
        
    def mostrarEstado(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            print(f'{sender.text()} seleccionado')
        else:
            print(f'{sender.text()} deseleccionado')
            
if __name__ == '__main__':
    app = QApplication(sys.argv) 
    ventana = Aplicacion()
    ventana.show()
    sys.exit(app.exec_())
