'''
Измененный код, на основе кода из Qt Designer, но в качестве родительского класса QMainWindow, в котором получается
реализовать нажатие клавиатуры
Но появилась ошибка:
    (DeprecationWarning: sipPyTypeDict() is deprecated, the extension module should use sipPyTypeDictRef() instead
    super(Window, self).__init__()),
которую я просто игнорирую, т.к она связана с версией python (line 18)
'''

import sys
import warnings

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QKeyEvent

from style import style_for_button_nm, style_for_button_equal, style_for_button_oper

warnings.filterwarnings("ignore", category=DeprecationWarning)




class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Калькулятор')
        self.setFixedSize(298, 399)
        self.setStyleSheet("background-color: rgb(32, 32, 32);")

        self.result_label = QtWidgets.QLabel(self)
        self.result_label.setGeometry(QtCore.QRect(0, 0, 300, 81))
        self.result_label.setIndent(10)
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
        self.btn_plus = QtWidgets.QPushButton(self)
        self.btn_plus.setGeometry(QtCore.QRect(224, 320, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet(style_for_button_oper)
        self.btn_plus.setObjectName("btn_plus")
        self.btn_equal = QtWidgets.QPushButton(self)
        self.btn_equal.setGeometry(QtCore.QRect(150, 320, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet(style_for_button_equal)
        self.btn_equal.setObjectName("btn_equal")
        self.btn_zero = QtWidgets.QPushButton(self)
        self.btn_zero.setGeometry(QtCore.QRect(76, 320, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_zero.setFont(font)
        self.btn_zero.setStyleSheet(style_for_button_nm)
        self.btn_zero.setObjectName("btn_zero")
        self.btn_dot = QtWidgets.QPushButton(self)
        self.btn_dot.setGeometry(QtCore.QRect(2, 320, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet(style_for_button_nm)
        self.btn_dot.setObjectName("btn_dot")
        self.btn_1 = QtWidgets.QPushButton(self)
        self.btn_1.setGeometry(QtCore.QRect(2, 240, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet(style_for_button_nm)
        self.btn_1.setObjectName("btn_1")
        self.btn_4 = QtWidgets.QPushButton(self)
        self.btn_4.setGeometry(QtCore.QRect(2, 160, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet(style_for_button_nm)
        self.btn_4.setObjectName("btn_4")
        self.btn_7 = QtWidgets.QPushButton(self)
        self.btn_7.setGeometry(QtCore.QRect(2, 80, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet(style_for_button_nm)
        self.btn_7.setObjectName("btn_7")
        self.btn_2 = QtWidgets.QPushButton(self)
        self.btn_2.setGeometry(QtCore.QRect(76, 240, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet(style_for_button_nm)
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self)
        self.btn_3.setGeometry(QtCore.QRect(150, 240, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet(style_for_button_nm)
        self.btn_3.setObjectName("btn_3")
        self.btn_minus = QtWidgets.QPushButton(self)
        self.btn_minus.setGeometry(QtCore.QRect(224, 240, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet(style_for_button_oper)
        self.btn_minus.setObjectName("btn_minus")
        self.btn_5 = QtWidgets.QPushButton(self)
        self.btn_5.setGeometry(QtCore.QRect(76, 160, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet(style_for_button_nm)
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self)
        self.btn_6.setGeometry(QtCore.QRect(150, 160, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet(style_for_button_nm)
        self.btn_6.setObjectName("btn_6")
        self.btn_mult = QtWidgets.QPushButton(self)
        self.btn_mult.setGeometry(QtCore.QRect(224, 160, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mult.setFont(font)
        self.btn_mult.setStyleSheet(style_for_button_oper)
        self.btn_mult.setObjectName("btn_mult")
        self.btn_8 = QtWidgets.QPushButton(self)
        self.btn_8.setGeometry(QtCore.QRect(76, 80, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet(style_for_button_nm)
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self)
        self.btn_9.setGeometry(QtCore.QRect(150, 80, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet(style_for_button_nm)
        self.btn_9.setObjectName("btn_9")
        self.btn_divis = QtWidgets.QPushButton(self)
        self.btn_divis.setGeometry(QtCore.QRect(224, 80, 72, 77))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_divis.setFont(font)
        self.btn_divis.setStyleSheet(style_for_button_oper)
        self.btn_divis.setObjectName("btn_divis")

        self.retranslateUi(self)
        self.add_functions()

    def keyPressEvent(self, event):
        if event.key() == 16777219:
            if len(self.result_label.text()) == 1:
                self.result_label.setText('0')
            else:
                self.result_label.setText(self.result_label.text()[:-1])
        elif event.key() in ([i for i in range(47, 58)] + [42, 43, 45, 46]):
            self.write_number(chr(event.key()))
        elif event.key() == 16777220:
            self.res()

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
        if self.result_label.text() == '0' and number not in '+-*/.':
            self.result_label.setText(number)
        else:
            self.result_label.setText(self.result_label.text() + number)

    def res(self):
        if '/' in self.result_label.text():
            try:
                self.result_label.setText(str(round(eval(self.result_label.text()), 9)))
            except Exception:
                pass
        else:
            try:
                self.result_label.setText(str(eval(self.result_label.text())))
            except Exception:
                pass


def application():
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(r'calc_icon.png'))
    window = Window()

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    application()
