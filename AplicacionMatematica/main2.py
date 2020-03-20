import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('main.ui', self)
        self.go_to_raiz.clicked.connect(self.abrirVentanaRaiz)
        self.salir.clicked.connect(self.Exit)
        self.operaciones.clicked.connect(self.abrirVentanaBasicas)
    def Exit(self):
        self.close()
    def abrirVentanaRaiz(self):
        self.hide()
        Raiz=VentanaRaiz(self)
        Raiz.show()
    def abrirVentanaBasicas(self):
        self.hide()
        Basicas=VentanaBasicas(self)
        Basicas.show()
        
    

class VentanaBasicas(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaBasicas, self).__init__(parent)
        loadUi('basicas.ui', self)
        self.evaluar.clicked.connect(self.calculos)
        self.volver.clicked.connect(self.abrirVentanaPrincipal)
        
    def calculos(self):
        self.estatus.setText("<<")
        self.estatus.setText("<<")
        X=self.a_evaluar.toPlainText()
        
        try:  
            Y=eval(X)
            _Y=str(Y)
            self.estatus.setText("<<"+"Done")
        except SyntaxError:
            self.resultado1.setText("Error")
            self.estatus.setText("<<"+"Valor introducido no admitido\n<< Done")
        except NameError:
            self.resultado1.setText("Error")
            self.estatus.setText("<<"+"Valor introducido no admitido\n<< Done")
           
        if len(_Y)<20:
            self.resultado1.setText(_Y)
        elif len(_Y)>20:
            self.resultado1.setText("Error"+_Y[0:14])
            self.estatus.setText("<<"+"Longitud del resultado mayor a la permitida\n<< Done")
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
        
            
            
        
            
                
class VentanaRaiz(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaRaiz, self).__init__(parent)
        loadUi('raiz.ui', self)
        
        self.volver.clicked.connect(self.abrirVentanaPrincipal)
        self.boton1.clicked.connect(self.calculos)
    def calculos(self):
        self.resultado1.setText("")
        self.observaciones_1.setText("")
        
        try:
            Base=float(self.numero1.toPlainText())
            Raiz=float(self.raiz.value())
            if Base<=0:
                self.observaciones_1.setText("<< Es imposible obtener raiz de numeros negativos o 0\n<< Done")
            elif Base>0:
                raizCubica =  Base**(1/Raiz)
                self.resultado1.setText(str(raizCubica))
                self.observaciones_1.setText("<< Done")
            
        except ValueError:
            
            self.observaciones_1.setText("<< Es imposible obtener raiz de caracteres\n<< Done")
        except ZeroDivisionError:
            self.observaciones_1.setText("<< Es imposible obtener raiz a la 0\n<< Done")

    
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
        
app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())

