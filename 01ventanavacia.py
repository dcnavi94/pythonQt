from PyQt5.QtWidgets  import QApplication, QWidget
import sys

class VentanaVacia(QWidget):
    def __init__(self):
        super(VentanaVacia,self).__init__()
        self.initializeUI()
        
    def initializeUI(self):
        self.setWindowTitle('Ventana Vacía')
        self.setGeometry(100, 100, 300, 200)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaVacia()
    ventana.show()
    sys.exit(app.exec_())
