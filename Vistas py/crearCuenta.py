# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crearCuenta.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class Ui_crearUsuario(QtWidgets.QMainWindow):


    def setupUi(self, crearUsuario):
        crearUsuario.setObjectName("crearUsuario")
        crearUsuario.resize(1024, 600)
        crearUsuario.setStyleSheet("background-color: rgb(20 ,18 ,35);")
        self.centralwidget = QtWidgets.QWidget(crearUsuario)
        self.centralwidget.setStyleSheet("background-color: rgb(20 ,18 ,35);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(230, 40, 561, 501))
        self.frame.setStyleSheet("background-color: rgb(224, 224, 224);\n"
                                 "border-radius: 20px;\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(220, 30, 131, 151))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 260, 31, 31))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 370, 31, 31))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("image: url(:/CrearCuenta/cerrar-sesion (1).png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 310, 31, 31))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(300, 310, 31, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(300, 260, 31, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 260, 191, 25))
        self.lineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius : 10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 320, 191, 25))
        self.lineEdit_3.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-radius : 10px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 260, 191, 25))
        self.lineEdit_4.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-radius : 10px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 320, 191, 25))
        self.lineEdit_5.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_5.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-radius : 10px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(340, 380, 191, 25))
        self.lineEdit_6.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_6.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-radius : 10px;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(300, 370, 31, 31))
        self.label_2.setStyleSheet("border-image: url(:/CrearCuenta/conversaciones.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(70, 240, 201, 17))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(70, 300, 201, 17))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(60, 360, 221, 17))
        self.label_17.setObjectName("label_17")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(70, 380, 191, 25))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius : 10px;")
        self.comboBox.setObjectName("comboBox")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(330, 240, 201, 17))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(340, 300, 201, 17))
        self.label_19.setObjectName("label_19")
        self.label_44 = QtWidgets.QLabel(self.frame)
        self.label_44.setGeometry(QtCore.QRect(340, 360, 201, 17))
        self.label_44.setObjectName("label_44")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 430, 151, 41))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("background-color: rgb(51, 209, 122);\n"
                                        "border-radius: 10px;\n"
                                        "color: white;\n"
                                        "font-size: 16px;\n"
                                        "font-weight: bold;\n"
                                        "")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(210, 190, 161, 31))
        self.label_8.setObjectName("label_8")
        crearUsuario.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(crearUsuario)
        self.statusbar.setObjectName("statusbar")
        crearUsuario.setStatusBar(self.statusbar)

        self.retranslateUi(crearUsuario)
        QtCore.QMetaObject.connectSlotsByName(crearUsuario)

    def retranslateUi(self, crearUsuario):
        _translate = QtCore.QCoreApplication.translate
        crearUsuario.setWindowTitle(_translate("crearUsuario", "crearUsuario"))
        self.label.setText(_translate("crearUsuario",
                                      "<html><head/><body><p><img src=\":/CrearCuenta/unnamed (1).png\"/></p></body></html>"))
        self.label_3.setText(_translate("crearUsuario",
                                        "<html><head/><body><p><img src=\":/CrearCuenta/correo.png\"/></p></body></html>"))
        self.label_5.setText(_translate("crearUsuario",
                                        "<html><head/><body><p><img src=\":/CrearCuenta/proteger (1).png\"/></p></body></html>"))
        self.label_4.setText(_translate("crearUsuario",
                                        "<html><head/><body><p><img src=\":/CrearCuenta/bloquear (1).png\"/></p></body></html>"))
        self.label_6.setText(_translate("crearUsuario",
                                        "<html><head/><body><p><img src=\":/CrearCuenta/bloquear (1).png\"/></p></body></html>"))
        self.label_7.setText(_translate("crearUsuario",
                                        "<html><head/><body><p><img src=\":/CrearCuenta/usuario (2).png\"/></p></body></html>"))
        self.label_15.setText(_translate("crearUsuario", "Ingrese su correo electronico"))
        self.label_16.setText(_translate("crearUsuario", "Ingrese su contraseña"))
        self.label_17.setText(_translate("crearUsuario", "Eliga su pregunta  de seguiradad"))
        self.label_18.setText(_translate("crearUsuario", "Ingrese su nombre de usuario"))
        self.label_19.setText(_translate("crearUsuario", "Verifique su contraseña"))
        self.label_44.setText(_translate("crearUsuario", "Respuesta"))
        self.pushButton_5.setText(_translate("crearUsuario", "Registrar Usuario"))
        self.label_8.setText(_translate("crearUsuario",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Registrar Usuario</span></p></body></html>"))


import iconosCrearCuenta

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    crearUsuario = QtWidgets.QMainWindow()
    ui = Ui_crearUsuario()
    ui.setupUi(crearUsuario)
    crearUsuario.show()
    sys.exit(app.exec_())
