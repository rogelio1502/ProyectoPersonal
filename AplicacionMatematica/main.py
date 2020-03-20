import sys
import time
from PyQt5 import uic, QtWidgets
from raiz import Ui_v_raiz
qtCreatorFile = "main.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.go_to_raiz.clicked.connect(self.abrir)
    def abrir(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_v_raiz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        
        
        
    

   
        
            
            
        
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())