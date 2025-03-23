# Importaciones
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont, QPixmap
import sys


class PerfilUsuario(QWidget):
    def __init__(self):
        super(PerfilUsuario, self).__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setGeometry(100,100,300,440)
        self.setWindowTitle("Perfil de usuario")
        self.mostrar_imagenes()
        self.mostrar_labels()

    def mostrar_imagenes(self):
        foto_perfil = "IMG/SECCION2/profile_image.png"
        foto_fondo = "IMG/SECCION2/skyblue.jpg"

        try:
            with open(foto_fondo):
                label_fondo = QLabel(self)
                pixmap = QPixmap(foto_fondo)
                label_fondo.setPixmap(pixmap)
        except FileNotFoundError:
            print("No se encontro la imagen")

        try:
            with open(foto_perfil):
                label_perfil = QLabel(self)
                pixmap = QPixmap(foto_perfil)
                label_perfil.setPixmap(pixmap)
                label_perfil.move(100,25)
        except FileNotFoundError:
            print("No se encontro la imagen")

    def mostrar_labels(self):
        usuario = QLabel(self)
        usuario.setText("John Doe")
        usuario.move(100, 155)
        usuario.setFont(QFont("Arial", 17))

        biografia_title = QLabel(self)
        biografia_title.setText("Biography")
        biografia_title.move(15, 185)
        biografia_title.setFont(QFont("Arial", 17))

        biografia = QLabel(self)
        biografia.setText("I´m a software Enginner with 8 years experience creating awesome code")
        biografia.move(15, 220)
        biografia.setWordWrap(True)
        # biografia.setFont(QFont("Arial", 17))

        skills_title = QLabel(self)
        skills_title.setText("Skills")
        skills_title.move(15, 260)
        skills_title.setFont(QFont("Arial", 17))

        skills = QLabel(self)
        skills.setText("Python | PHP | SQL | JavaScript")
        skills.move(15, 290)

        experiencias_title = QLabel(self)
        experiencias_title.setText("Experience")
        experiencias_title.move(15,320)
        skills_title.setFont(QFont("Arial", 17))

        experiencias = QLabel(self)
        experiencias.setText("Python Developer")
        experiencias.move(15, 350)
        experiencias.setFont(QFont("Arial", 8))

        fechas = QLabel(self)
        fechas.setText("PMar 2011 - Present")
        fechas.move(15, 370)
        fechas.setFont(QFont("Arial", 8))

        experiencias = QLabel(self)
        experiencias.setText("Pizza Delivery Driver")
        experiencias.move(15, 390)
        experiencias.setFont(QFont("Arial", 8))

        fechas = QLabel(self)
        fechas.setText("Aug 2015 - Dec 2017")
        fechas.move(15, 410)
        fechas.setFont(QFont("Arial", 8))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PerfilUsuario()
    window.show()
    sys.exit(app.exec_())