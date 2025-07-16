
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_employee_inf_edit(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 397)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #e6ebdc;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit {\n"
"    background-color: #a9af9e;\n"
"    color: #000000;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 6px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #4A7C59;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5A9F73;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.emp_ln_e_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_ln_e_label.setGeometry(QtCore.QRect(30, 140, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_ln_e_label.setFont(font)
        self.emp_ln_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_ln_e_label.setObjectName("emp_ln_e_label")
        self.emp_id_e_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_id_e_label.setGeometry(QtCore.QRect(20, 240, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_id_e_label.setFont(font)
        self.emp_id_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_id_e_label.setObjectName("emp_id_e_label")
        self.emp_brithmonth_e_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.emp_brithmonth_e_comboBox.setGeometry(QtCore.QRect(610, 150, 85, 25))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_brithmonth_e_comboBox.setFont(font)
        self.emp_brithmonth_e_comboBox.setStyleSheet("/* style for the QComboBox */\n"
"QComboBox {\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"/* style for drop down area */\n"
"QComboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"/* style for drop down arrow */\n"
"QComboBox::down-arrow {\n"
"    image: url(D:/Python/Image/down-arrow-8-128);\n"
"    width: 12 px;\n"
"    height: 12px;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"/* style for list menu */\n"
"QComboBox QListView {\n"
"font-size: 12px;\n"
"border: 1px solid #000000;\n"
"padding: 5px;\n"
"background-color: #a9af9e;\n"
"outline: 0px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #a9af9e;\n"
"    font-size: 15px;\n"
"    font-family: \"Arad Medium\";\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #a9af9e;\n"
"    color: black;\n"
"    selection-background-color: #F3E9E2;\n"
"    selection-color: black;\n"
"}")
        self.emp_brithmonth_e_comboBox.setObjectName("emp_brithmonth_e_comboBox")
        self.emp_diploma_e_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_diploma_e_lineEdit.setGeometry(QtCore.QRect(530, 200, 251, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_diploma_e_lineEdit.setFont(font)
        self.emp_diploma_e_lineEdit.setObjectName("emp_diploma_e_lineEdit")
        self.emp_male_e_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_male_e_label.setGeometry(QtCore.QRect(580, 248, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_male_e_label.setFont(font)
        self.emp_male_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_male_e_label.setObjectName("emp_male_e_label")
        self.emp_nid_e_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_nid_e_label.setGeometry(QtCore.QRect(30, 190, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_nid_e_label.setFont(font)
        self.emp_nid_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_nid_e_label.setObjectName("emp_nid_e_label")
        self.add_emp_e_Button = QtWidgets.QPushButton(self.centralwidget)
        self.add_emp_e_Button.setGeometry(QtCore.QRect(290, 300, 200, 70))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.add_emp_e_Button.setFont(font)
        self.add_emp_e_Button.setObjectName("add_emp_e_Button")
        self.emp_phone_e_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_phone_e_label.setGeometry(QtCore.QRect(400, 90, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_phone_e_label.setFont(font)
        self.emp_phone_e_label.setObjectName("emp_phone_e_label")
        self.emp_gender_e_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_gender_e_label.setGeometry(QtCore.QRect(440, 243, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_gender_e_label.setFont(font)
        self.emp_gender_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_gender_e_label.setObjectName("emp_gender_e_label")
        self.emp_id_e_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_id_e_lineEdit.setGeometry(QtCore.QRect(130, 240, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_id_e_lineEdit.setFont(font)
        self.emp_id_e_lineEdit.setObjectName("emp_id_e_lineEdit")
        self.emp_birthdate_e_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_birthdate_e_label.setGeometry(QtCore.QRect(425, 148, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_birthdate_e_label.setFont(font)
        self.emp_birthdate_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_birthdate_e_label.setObjectName("emp_birthdate_e_label")
        self.emp_phone_e_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_phone_e_lineEdit.setGeometry(QtCore.QRect(530, 90, 251, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_phone_e_lineEdit.setFont(font)
        self.emp_phone_e_lineEdit.setObjectName("emp_phone_e_lineEdit")
        self.top_inf_e_e_label = QtWidgets.QLabel(self.centralwidget)
        self.top_inf_e_e_label.setGeometry(QtCore.QRect(240, 10, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.top_inf_e_e_label.setFont(font)
        self.top_inf_e_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_inf_e_e_label.setObjectName("top_inf_e_e_label")
        self.emp_ln_e_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_ln_e_lineEdit.setGeometry(QtCore.QRect(130, 140, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_ln_e_lineEdit.setFont(font)
        self.emp_ln_e_lineEdit.setObjectName("emp_ln_e_lineEdit")
        self.emp_diploma_e_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_diploma_e_label.setGeometry(QtCore.QRect(430, 200, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_diploma_e_label.setFont(font)
        self.emp_diploma_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_diploma_e_label.setWordWrap(True)
        self.emp_diploma_e_label.setObjectName("emp_diploma_e_label")
        self.emp_female_e_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_female_e_label.setGeometry(QtCore.QRect(670, 248, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_female_e_label.setFont(font)
        self.emp_female_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_female_e_label.setObjectName("emp_female_e_label")
        self.emp_birthday_e_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.emp_birthday_e_comboBox.setGeometry(QtCore.QRect(697, 150, 85, 25))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_birthday_e_comboBox.setFont(font)
        self.emp_birthday_e_comboBox.setStyleSheet("/* style for the QComboBox */\n"
"QComboBox {\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"/* style for drop down area */\n"
"QComboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"/* style for drop down arrow */\n"
"QComboBox::down-arrow {\n"
"    image: url(D:/Python/Image/down-arrow-8-128);\n"
"    width: 12 px;\n"
"    height: 12px;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"/* style for list menu */\n"
"QComboBox QListView {\n"
"font-size: 12px;\n"
"border: 1px solid #000000;\n"
"padding: 5px;\n"
"background-color: #a9af9e;\n"
"outline: 0px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #a9af9e;\n"
"    font-size: 15px;\n"
"    font-family: \"Arad Medium\";\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #a9af9e;\n"
"    color: black;\n"
"    selection-background-color: #F3E9E2;\n"
"    selection-color: black;\n"
"}")
        self.emp_birthday_e_comboBox.setObjectName("emp_birthday_e_comboBox")
        self.emp_fn_e_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_fn_e_label.setGeometry(QtCore.QRect(30, 90, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_fn_e_label.setFont(font)
        self.emp_fn_e_label.setObjectName("emp_fn_e_label")
        self.emp_nid_e_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_nid_e_lineEdit.setGeometry(QtCore.QRect(130, 190, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_nid_e_lineEdit.setFont(font)
        self.emp_nid_e_lineEdit.setObjectName("emp_nid_e_lineEdit")
        self.emp_fn_e_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_fn_e_lineEdit.setGeometry(QtCore.QRect(130, 90, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_fn_e_lineEdit.setFont(font)
        self.emp_fn_e_lineEdit.setObjectName("emp_fn_e_lineEdit")
        self.emp_birthyear_e_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.emp_birthyear_e_comboBox.setGeometry(QtCore.QRect(523, 150, 85, 25))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_birthyear_e_comboBox.setFont(font)
        self.emp_birthyear_e_comboBox.setStyleSheet("/* style for the QComboBox */\n"
"QComboBox {\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"/* style for drop down area */\n"
"QComboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"/* style for drop down arrow */\n"
"QComboBox::down-arrow {\n"
"    image: url(D:/Python/Image/down-arrow-8-128);\n"
"    width: 12 px;\n"
"    height: 12px;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"/* style for list menu */\n"
"QComboBox QListView {\n"
"font-size: 12px;\n"
"border: 1px solid #000000;\n"
"padding: 5px;\n"
"background-color: #a9af9e;\n"
"outline: 0px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #a9af9e;\n"
"    font-size: 15px;\n"
"    font-family: \"Arad Medium\";\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #a9af9e;\n"
"    color: black;\n"
"    selection-background-color: #F3E9E2;\n"
"    selection-color: black;\n"
"}")
        self.emp_birthyear_e_comboBox.setObjectName("emp_birthyear_e_comboBox")
        self.emp_e_male_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.emp_e_male_radioButton.setGeometry(QtCore.QRect(630, 250, 16, 17))
        self.emp_e_male_radioButton.setText("")
        self.emp_e_male_radioButton.setObjectName("emp_e_male_radioButton")
        self.emp_e_female_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.emp_e_female_radioButton.setGeometry(QtCore.QRect(730, 250, 16, 17))
        self.emp_e_female_radioButton.setText("")
        self.emp_e_female_radioButton.setObjectName("emp_e_female_radioButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.emp_ln_e_label.setText(_translate("MainWindow", "Last Name:"))
        self.emp_id_e_label.setText(_translate("MainWindow", "Employee ID:"))
        self.emp_male_e_label.setText(_translate("MainWindow", "Male"))
        self.emp_nid_e_label.setText(_translate("MainWindow", "National ID:"))
        self.add_emp_e_Button.setText(_translate("MainWindow", "Finish"))
        self.emp_phone_e_label.setText(_translate("MainWindow", "Phone Number:"))
        self.emp_gender_e_label.setText(_translate("MainWindow", "Gender:"))
        self.emp_birthdate_e_label.setText(_translate("MainWindow", "Birthdate:"))
        self.top_inf_e_e_label.setText(_translate("MainWindow", "Change What You want!"))
        self.emp_diploma_e_label.setText(_translate("MainWindow", "Diploma:"))
        self.emp_female_e_label.setText(_translate("MainWindow", "Female"))
        self.emp_fn_e_label.setText(_translate("MainWindow", "First Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_employee_inf_edit()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
