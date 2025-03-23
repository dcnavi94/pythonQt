from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.inicializar_gui()

    def inicializar_gui(self):
        self.setWindowTitle('Campo de texto')
        self.setGeometry(100, 100, 400, 300)
        self.mostrar_widgets()

    

    def mostrar_widgets(self):
        QLabel('escribe Nombre:', self).move(100, 10)
        nombre = QLabel(self)
        nombre.setText('Nombre:')
        nombre.move(80, 50)

        self.nombre_entrada = QLineEdit(self)
        self.nombre_entrada.move(130, 50)
        self.nombre_entrada.resize(200, 20)
        self.nombre_entrada.setAlignment(Qt.AlignLeft)

        self.boton = QPushButton(self)
        self.boton.move(160, 110) 
        self.boton.setText('Limpiar')
        self.boton.clicked.connect(self.Limpiar_Line_edit)
           
    def Limpiar_Line_edit(self):
        sender = self.sender()
        if sender.text() == 'Limpiar':
            self.nombre_entrada.clear()

       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()
    sys.exit(app.exec_())