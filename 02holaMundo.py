from PyQt5.QtWidgets  import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
import sys

class AplicacionHolaMundo(QWidget):
    def __init__(self):
        super(AplicacionHolaMundo,self).__init__()
        self.emptywindow()
        
    def emptywindow(self):
        self.setWindowTitle('Aplicación Hola Mundo')
        self.setGeometry(100, 100, 300, 200)
        self.displaylabels()
    def displaylabels(self):
        texto = QLabel(self)
        texto.setText('Hola Mundo')
        texto.move(100, 100)
        
        image = r"world.jpeg"
        try:
            with open(image):
                labelimage = QLabel(self)
                pixmap = QPixmap(image)
                labelimage.setPixmap(pixmap)
                labelimage.move(100, 50)
                    
        except FileNotFoundError:
            print(f"Imagen no encontrada: {image}")
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = AplicacionHolaMundo()
    ventana.show()
    sys.exit(app.exec_())
