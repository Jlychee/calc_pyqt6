'''
Весь код создания окна и кнопок, не считая функция взаимодейсвтия из QtDesigner
(наверное) Из-за того, что наследуется object, не получается реализовать проверку нажатия клавиатуры
'''

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.result_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(0, 0, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.result_label.setFont(font)
        self.result_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.result_label.setStyleSheet("background-color: rgb(32, 32, 32);\n"
                                        "color: rgb(210, 210, 210);")
        self.result_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.result_label.setObjectName("result_label")
        self.btn_plus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(225, 320, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                    "color: rgb(199, 199, 199);\n"
                                    "border-radius: 10px")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_equal = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(150, 320, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(138, 157, 182);\n"
                                     "border-radius: 10px")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_zero = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_zero.setGeometry(QtCore.QRect(75, 320, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_zero.setFont(font)
        self.btn_zero.setStyleSheet("background-color: rgb(59, 59, 59);\n"
                                    "color: rgb(199, 199, 199);\n"
                                    "border-radius: 10px")
        self.btn_zero.setObjectName("btn_zero")
        self.btn_dot = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(1, 320, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet("background-color: rgb(59, 59, 59);\n"
                                   "color: rgb(199, 199, 199);\n"
                                   "border-radius: 10px")
        self.btn_dot.setObjectName("btn_dot")
        self.btn_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(1, 240, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(59, 59, 59);\n"
                                 "color: rgb(199, 199, 199);\n"
                                 "border-radius: 10px")
        self.btn_1.setObjectName("btn_1")
        self.btn_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(1, 160, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(59, 59, 59);\n"
                                 "color: rgb(199, 199, 199);\n"
                                 "border-radius: 10px")
        self.btn_4.setObjectName("btn_4")
        self.btn_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(1, 80, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(59, 59, 59);\n"
                                 "color: rgb(199, 199, 199);\n"
                                 "border-radius: 10px")
        self.btn_7.setObjectName("btn_7")
        self.btn_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(75, 240, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(59, 59, 59);\n"
                                 "color: rgb(199, 199, 199);\n"
                                 "border-radius: 10px")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(150, 240, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(59, 59, 59);\n"
                                 "color: rgb(199, 199, 199);\n"
                                 "border-radius: 10px")
        self.btn_3.setObjectName("btn_3")
        self.btn_minus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(225, 240, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                     "color: rgb(199, 199, 199);\n"
                                     "border-radius: 10px")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(75, 160, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(59, 59, 59);\n"
                                 "color: rgb(199, 199, 199);\n"
                                 "border-radius: 10px")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(150, 160, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(59, 59, 59);\n"
                                 "color: rgb(199, 199, 199);\n"
                                 "border-radius: 10px\n"
                                 "")
        self.btn_6.setObjectName("btn_6")
        self.btn_mult = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_mult.setGeometry(QtCore.QRect(225, 160, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mult.setFont(font)
        self.btn_mult.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                    "color: rgb(199, 199, 199);\n"
                                    "border-radius: 10px")
        self.btn_mult.setObjectName("btn_mult")
        self.btn_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(75, 80, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(59, 59, 59);\n"
                                 "color: rgb(199, 199, 199);\n"
                                 "border-radius: 10px")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(150, 80, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(59, 59, 59);\n"
                                 "color: rgb(199, 199, 199);\n"
                                 "border-radius: 10px")
        self.btn_9.setObjectName("btn_9")
        self.btn_divis = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_divis.setGeometry(QtCore.QRect(225, 80, 71, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_divis.setFont(font)
        self.btn_divis.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                     "color: rgb(199, 199, 199);\n"
                                     "border-radius: 10px")
        self.btn_divis.setObjectName("btn_divis")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Калькулятор")
        self.result_label.setText(_translate("MainWindow", "0"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_zero.setText(_translate("MainWindow", "0"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_divis.setText(_translate("MainWindow", "/"))

    def add_functions(self):
        self.btn_zero.clicked.connect(lambda: self.write_number(self.btn_zero.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_mult.clicked.connect(lambda: self.write_number(self.btn_mult.text()))
        self.btn_divis.clicked.connect(lambda: self.write_number(self.btn_divis.text()))
        self.btn_dot.clicked.connect(lambda: self.write_number(self.btn_dot.text()))
        self.btn_equal.clicked.connect(self.res)

    def write_number(self, number):
        if number in '+-*/':
            if (
                    '+' in self.result_label.text() or '-' in self.result_label.text() or '*' in self.result_label.text() or '/' in self.result_label.text()) and \
                    self.result_label.text()[-1] not in '+-*/':
                self.res()
            elif (
                    '+' in self.result_label.text() or '-' in self.result_label.text() or '*' in self.result_label.text() or '/' in self.result_label.text()) and \
                    self.result_label.text()[-1] in '+-*/':
                self.result_label.setText(self.result_label.text()[:-1])
        if self.result_label.text() == '0' and number not in '+-*/':
            self.result_label.setText(number)
        else:
            self.result_label.setText(self.result_label.text() + number)

    def res(self):
        self.result_label.setText(str(eval(self.result_label.text())))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(r'calc_icon.png'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
