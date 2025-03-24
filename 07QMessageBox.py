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
        label = QLabel('CATALOGO DE PELICULAS', self)
        label.move(20, 20)
        label.setFont(QFont('Arial', 20))
        label.setAlignment(Qt.AlignCenter)
        
        LABEL_PELICULA = QLabel(' Ingrese el Nombre de la pelicula a buscar :', self)
        LABEL_PELICULA.move(20, 60)
        
        label_nombre = QLabel('Nombre:', self)
        label_nombre.move(20, 90)
        
        self.line_edit = QLineEdit(self)
        self.line_edit.move(180, 90)
        self.line_edit.resize(240, 20)
        self.line_edit.placeholderText = 'Nombre de la pelicula'
        
        self.boton = QPushButton('Buscar', self)
        self.boton.move(95, 130)
        self.boton.resize(150, 40)
        self.boton.clicked.connect(self.mostrarMensaje)
        
    def mostrarMensaje(self):
        try:
            with open('peliculas.txt') as archivo:
                peliculas = [line.strip("\n") for line in archivo]
        except FileNotFoundError:
            print("No se encontro el archivo")
            peliculas = []
        
        pelicula = self.line_edit.text()
        
        if pelicula in peliculas:
            QMessageBox.information(self, 'Busqueda', f'La pelicula {pelicula} se encuentra en el catalogo', QMessageBox.Ok, QMessageBox.Ok)
        else:
            pelicula_no_encontrada = QMessageBox.question(self, 'Busqueda', f'La pelicula {pelicula} no se encuentra en el catalogo. ¿Desea agregarla?', QMessageBox.Yes | QMessageBox.No)
            if pelicula_no_encontrada == QMessageBox.Yes:
                with open('peliculas.txt', 'a') as archivo:
                    archivo.write(f'{pelicula}\n')
                QMessageBox.information(self, 'Agregar', f'La pelicula {pelicula} ha sido agregada al catalogo', QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.close()
            
            
if __name__ == '__main__':  
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()
    sys.exit(app.exec_())
        