# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IniciarSesion.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setBaseSize(QtCore.QSize(1024, 600))
        MainWindow.setStyleSheet("background-color: rgb(20, 18, 20);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(20 ,18 ,35);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 90, 431, 411))
        self.frame.setStyleSheet("background-color: rgb( 224, 224, 224 );\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 176, 151, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 256, 181, 21))
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(130, 30, 161, 121))
        self.graphicsView.setObjectName("graphicsView")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(150, 10, 131, 151))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(100, 210, 31, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(100, 280, 21, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(130, 210, 201, 31))
        self.lineEdit.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 280, 201, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 340, 141, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(46, 194, 126);\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(480, 160, 501, 281))
        self.frame_2.setStyleSheet("border-width: 2px 2px 2px 0px;\n"
"border-style: dotted;\n"
"border-color: rgb( 224, 224, 224 );\n"
"background-color: transparent;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(140, 40, 251, 71))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("color: rgb(224,224,224);\n"
"font-size: 48px;\n"
"border-style: none")
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(40, 90, 421, 17))
        self.label_4.setStyleSheet("color: rgb(224,224,224);\n"
"border-style: none")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(40, 190, 501, 17))
        self.label_5.setStyleSheet("color: rgb(224,224,224);\n"
"border-style: none")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.frame_2)
        self.commandLinkButton.setGeometry(QtCore.QRect(120, 110, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet("color: rgb(224,224,224);\n"
"border-style: None\n"
"")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.frame_2)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(100, 160, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_2.setStyleSheet("color: rgb(224,224,224);\n"
"border-style: None\n"
"")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.frame_2)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(210, 220, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setStyleSheet("color: red;\n"
"border-style: None\n"
"")
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inicio"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Ingresar Usuario</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Ingresar Contraseña</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Inicio/unnamed (1).png\"/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Inicio/usuario (2).png\"/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Inicio/bloquear (1).png\"/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Iniciar Sesion"))
        self.label_3.setText(_translate("MainWindow", "Bienvenido"))
        self.label_4.setText(_translate("MainWindow", "_________________________________________________________"))
        self.label_5.setText(_translate("MainWindow", "_________________________________________________________"))
        self.commandLinkButton.setText(_translate("MainWindow", "¿Olvidaste tu contraseña?"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "¿No tienes cuenta? Registrate"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "Salir"))
import iconos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
