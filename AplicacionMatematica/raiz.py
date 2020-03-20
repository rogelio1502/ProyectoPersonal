# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raiz.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_v_raiz(object):
    def setupUi(self, v_raiz):
        v_raiz.setObjectName("v_raiz")
        v_raiz.setEnabled(True)
        v_raiz.resize(470, 399)
        v_raiz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        v_raiz.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));")
        self.centralwidget = QtWidgets.QWidget(v_raiz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, -20, 271, 81))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 121, 41))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.numero1 = QtWidgets.QTextEdit(self.centralwidget)
        self.numero1.setGeometry(QtCore.QRect(30, 120, 104, 31))
        self.numero1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numero1.setObjectName("numero1")
        self.boton1 = QtWidgets.QPushButton(self.centralwidget)
        self.boton1.setGeometry(QtCore.QRect(350, 100, 99, 31))
        self.boton1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.boton1.setObjectName("boton1")
        self.resultado1 = QtWidgets.QTextEdit(self.centralwidget)
        self.resultado1.setGeometry(QtCore.QRect(120, 170, 241, 31))
        self.resultado1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resultado1.setObjectName("resultado1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 220, 181, 31))
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.observaciones_1 = QtWidgets.QLabel(self.centralwidget)
        self.observaciones_1.setGeometry(QtCore.QRect(50, 260, 401, 51))
        self.observaciones_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 italic 10pt \"Ubuntu\";\n"
"color: rgb(0, 0, 255);")
        self.observaciones_1.setText("")
        self.observaciones_1.setObjectName("observaciones_1")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 70, 121, 41))
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.raiz = QtWidgets.QSpinBox(self.centralwidget)
        self.raiz.setGeometry(QtCore.QRect(190, 120, 101, 31))
        self.raiz.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.raiz.setProperty("value", 2)
        self.raiz.setObjectName("raiz")
        self.volver = QtWidgets.QPushButton(self.centralwidget)
        self.volver.setGeometry(QtCore.QRect(190, 330, 99, 27))
        self.volver.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        
        self.volver.setObjectName("volver")
        self.volver.clicked.connect(self.menuPrincipal)
        v_raiz.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(v_raiz)
        self.statusbar.setObjectName("statusbar")
        v_raiz.setStatusBar(self.statusbar)

        self.retranslateUi(v_raiz)
        QtCore.QMetaObject.connectSlotsByName(v_raiz)

    def retranslateUi(self, v_raiz):
        _translate = QtCore.QCoreApplication.translate
        v_raiz.setWindowTitle(_translate("v_raiz", "MainWindow"))
        self.label.setText(_translate("v_raiz", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Raices Cuadradas</span></p></body></html>"))
        self.label_2.setText(_translate("v_raiz", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Numero</span></p></body></html>"))
        self.boton1.setWhatsThis(_translate("v_raiz", "<html><head/><body><p>Calcular</p><p><br/></p></body></html>"))
        self.boton1.setText(_translate("v_raiz", "Calcular"))
        self.label_3.setText(_translate("v_raiz", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Observaciones</span></p></body></html>"))
        self.label_4.setText(_translate("v_raiz", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Raiz</span></p><p><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.volver.setText(_translate("v_raiz", "Volver"))
    def menuPrincipal(self):
        self.ui=Ui_MainApp()
        

