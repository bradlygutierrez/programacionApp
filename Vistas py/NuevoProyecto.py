# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NuevoProyecto.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from entidades.proyecto import Proyecto
from Datos.dtProyecto import DT_proyect
from Proyectos import Ui_proyectos

class Ui_nuevoProyecto(QtWidgets.QMainWindow):
        def setupUi(self, NuevoProyecto):
                NuevoProyecto.setObjectName("NuevoProyecto")
                NuevoProyecto.resize(1024, 600)
                font = QtGui.QFont()
                font.setPointSize(20)
                NuevoProyecto.setFont(font)
                NuevoProyecto.setStyleSheet("background-color: rgb(20, 18, 35);\n"
                                            "border-color: rgb(255, 255, 255);")
                NuevoProyecto.setTabShape(QtWidgets.QTabWidget.Rounded)
                self.centralwidget = QtWidgets.QWidget(NuevoProyecto)
                self.centralwidget.setObjectName("centralwidget")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(10, 10, 128, 25))
                self.pushButton.setStyleSheet("background-color: rgb(51, 209, 122);\n"
                                              "\n"
                                              "border-color: rgb(0, 0, 0);")
                self.pushButton.setObjectName("pushButton")
                self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
                self.groupBox.setGeometry(QtCore.QRect(10, 70, 1001, 491))
                font = QtGui.QFont()
                font.setFamily("Ubuntu")
                font.setPointSize(20)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.groupBox.setFont(font)
                self.groupBox.setStyleSheet("font: 20pt \"Ubuntu\";\n"
                                            "color: rgb(255, 255, 255);")
                self.groupBox.setObjectName("groupBox")
                self.label = QtWidgets.QLabel(self.groupBox)
                self.label.setGeometry(QtCore.QRect(10, 50, 241, 81))
                font = QtGui.QFont()
                font.setFamily("Ubuntu")
                font.setPointSize(20)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
                self.lineEdit.setGeometry(QtCore.QRect(270, 80, 291, 25))
                font = QtGui.QFont()
                font.setFamily("Tlwg Typist")
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.lineEdit.setFont(font)
                self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 14pt \"Tlwg Typist\";\n"
                                            "border-color: rgb(0, 0, 0);\n"
                                            "color: black")
                self.lineEdit.setText("")
                self.lineEdit.setObjectName("lineEdit")
                self.label_2 = QtWidgets.QLabel(self.groupBox)
                self.label_2.setGeometry(QtCore.QRect(10, 130, 261, 41))
                font = QtGui.QFont()
                font.setFamily("Ubuntu")
                font.setPointSize(20)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.groupBox)
                self.label_3.setGeometry(QtCore.QRect(10, 190, 221, 41))
                font = QtGui.QFont()
                font.setFamily("Ubuntu")
                font.setPointSize(20)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.groupBox)
                self.label_4.setGeometry(QtCore.QRect(10, 250, 231, 41))
                font = QtGui.QFont()
                font.setFamily("Ubuntu")
                font.setPointSize(20)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_4.setFont(font)
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.groupBox)
                self.label_5.setGeometry(QtCore.QRect(10, 320, 161, 31))
                font = QtGui.QFont()
                font.setFamily("Ubuntu")
                font.setPointSize(20)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_5.setFont(font)
                self.label_5.setObjectName("label_5")
                self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
                self.lineEdit_5.setGeometry(QtCore.QRect(190, 320, 391, 141))
                font = QtGui.QFont()
                font.setFamily("Tlwg Typist")
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.lineEdit_5.setFont(font)
                self.lineEdit_5.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border-color: rgb(0, 0, 0);\n"
                                              "font: 14pt \"Tlwg Typist\";\n"
                                              "color: black")
                self.lineEdit_5.setText("")
                self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                self.lineEdit_5.setObjectName("lineEdit_5")
                self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
                self.lineEdit_2.setGeometry(QtCore.QRect(270, 140, 291, 25))
                font = QtGui.QFont()
                font.setFamily("Tlwg Typist")
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.lineEdit_2.setFont(font)
                self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "font: 14pt \"Tlwg Typist\";\n"
                                              "border-color: rgb(0, 0, 0);\n"
                                              "color: black")
                self.lineEdit_2.setText("")
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
                self.lineEdit_3.setGeometry(QtCore.QRect(270, 200, 291, 25))
                font = QtGui.QFont()
                font.setFamily("Tlwg Typist")
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.lineEdit_3.setFont(font)
                self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border-color: rgb(0, 0, 0);\n"
                                              "font: 14pt \"Tlwg Typist\";\n"
                                              "color: black")
                self.lineEdit_3.setText("")
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
                self.lineEdit_4.setGeometry(QtCore.QRect(270, 260, 291, 25))
                font = QtGui.QFont()
                font.setFamily("Tlwg Typist")
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.lineEdit_4.setFont(font)
                self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border-color: rgb(0, 0, 0);\n"
                                              "font: 14pt \"Tlwg Typist\";\n"
                                              "color: black")
                self.lineEdit_4.setText("")
                self.lineEdit_4.setObjectName("lineEdit_4")
                self.label_8 = QtWidgets.QLabel(self.groupBox)
                self.label_8.setGeometry(QtCore.QRect(10, 50, 241, 81))
                font = QtGui.QFont()
                font.setFamily("Ubuntu")
                font.setPointSize(20)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label_8.setFont(font)
                self.label_8.setObjectName("label_8")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(690, 130, 128, 128))
                self.label_6.setStyleSheet("border-image: url(:/logo/casco.png);")
                self.label_6.setText("")
                self.label_6.setObjectName("label_6")
                self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_6.setGeometry(QtCore.QRect(600, 260, 401, 251))
                self.lineEdit_6.setMinimumSize(QtCore.QSize(251, 0))
                self.lineEdit_6.setMaximumSize(QtCore.QSize(600, 800))
                font = QtGui.QFont()
                font.setFamily("DejaVu Sans Mono")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.lineEdit_6.setFont(font)
                self.lineEdit_6.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
                self.lineEdit_6.setTabletTracking(False)
                self.lineEdit_6.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.lineEdit_6.setAutoFillBackground(False)
                self.lineEdit_6.setStyleSheet("border-image: url(:/logo/t1exto.png);")
                self.lineEdit_6.setText("")
                self.lineEdit_6.setMaxLength(32755)
                self.lineEdit_6.setFrame(False)
                self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.lineEdit_6.setCursorPosition(0)
                self.lineEdit_6.setReadOnly(False)
                self.lineEdit_6.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
                self.lineEdit_6.setObjectName("lineEdit_6")
                self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_2.setGeometry(QtCore.QRect(720, 490, 211, 51))
                self.pushButton_2.setStyleSheet("background-color: rgb(51, 209, 122);\n"
                                                "\n"
                                                "border-color: rgb(0, 0, 0);")
                self.pushButton_2.setObjectName("pushButton_2")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(830, 130, 128, 128))
                self.label_7.setStyleSheet("border-image: url(:/logo/construccion.png);")
                self.label_7.setText("")
                self.label_7.setObjectName("label_7")
                self.pushButton.raise_()
                self.groupBox.raise_()
                self.label_6.raise_()
                self.label_7.raise_()
                self.lineEdit_6.raise_()
                self.pushButton_2.raise_()
                NuevoProyecto.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(NuevoProyecto)
                self.statusbar.setObjectName("statusbar")
                NuevoProyecto.setStatusBar(self.statusbar)
                self.menubar = QtWidgets.QMenuBar(NuevoProyecto)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
                self.menubar.setObjectName("menubar")
                NuevoProyecto.setMenuBar(self.menubar)

                self.retranslateUi(NuevoProyecto)
                QtCore.QMetaObject.connectSlotsByName(NuevoProyecto)

        def retranslateUi(self, NuevoProyecto):
                _translate = QtCore.QCoreApplication.translate
                NuevoProyecto.setWindowTitle(_translate("NuevoProyecto", "MainWindow"))
                self.pushButton.setText(_translate("NuevoProyecto", "Regresar"))
                self.groupBox.setTitle(_translate("NuevoProyecto", "Nuevo Proyecto"))
                self.label.setText(_translate("NuevoProyecto",
                                              "<html><head/><body><p><span style=\" font-weight:600;\">Nombre:</span></p></body></html>"))
                self.label_2.setText(_translate("NuevoProyecto",
                                                "<html><head/><body><p><span style=\" font-weight:600;\">Presupuesto Inicial:</span></p></body></html>"))
                self.label_3.setText(_translate("NuevoProyecto",
                                                "<html><head/><body><p><span style=\" font-weight:600;\">Beneficiario:</span></p></body></html>"))
                self.label_4.setText(_translate("NuevoProyecto",
                                                "<html><head/><body><p><span style=\" font-weight:600;\">Fecha inicio:</span></p></body></html>"))
                self.label_5.setText(_translate("NuevoProyecto",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Descripción:</span></p></body></html>"))
                self.label_8.setText(_translate("NuevoProyecto",
                                                "<html><head/><body><p><span style=\" font-weight:600;\">Nombre:</span></p></body></html>"))
                self.pushButton_2.setText(_translate("NuevoProyecto", "Crear Proyecto"))






        def volver(self):
                self.pushButton.clicked.connect(Ui_proyectos.show())
import logo1
import logos2


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NuevoProyecto = QtWidgets.QMainWindow()
    ui = Ui_nuevoProyecto()
    ui.setupUi(NuevoProyecto)
    NuevoProyecto.show()
    sys.exit(app.exec_())
