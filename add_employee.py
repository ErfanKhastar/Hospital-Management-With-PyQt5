
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_employee(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 394)
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
        self.emp_fn_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_fn_lineEdit.setGeometry(QtCore.QRect(130, 100, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_fn_lineEdit.setFont(font)
        self.emp_fn_lineEdit.setObjectName("emp_fn_lineEdit")
        self.emp_ln_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_ln_lineEdit.setGeometry(QtCore.QRect(130, 150, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_ln_lineEdit.setFont(font)
        self.emp_ln_lineEdit.setObjectName("emp_ln_lineEdit")
        self.add_emp_Button = QtWidgets.QPushButton(self.centralwidget)
        self.add_emp_Button.setGeometry(QtCore.QRect(290, 310, 200, 70))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.add_emp_Button.setFont(font)
        self.add_emp_Button.setObjectName("add_emp_Button")
        self.top_inf_e_label = QtWidgets.QLabel(self.centralwidget)
        self.top_inf_e_label.setGeometry(QtCore.QRect(240, 10, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.top_inf_e_label.setFont(font)
        self.top_inf_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_inf_e_label.setObjectName("top_inf_e_label")
        self.emp_female_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_female_label.setGeometry(QtCore.QRect(660, 255, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_female_label.setFont(font)
        self.emp_female_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_female_label.setObjectName("emp_female_label")
        self.emp_birthyear_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.emp_birthyear_comboBox.setGeometry(QtCore.QRect(526, 150, 85, 25))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_birthyear_comboBox.setFont(font)
        self.emp_birthyear_comboBox.setStyleSheet("/* style for the QComboBox */\n"
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
        self.emp_birthyear_comboBox.setObjectName("emp_birthyear_comboBox")
        self.emp_fn_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_fn_label.setGeometry(QtCore.QRect(30, 100, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_fn_label.setFont(font)
        self.emp_fn_label.setObjectName("emp_fn_label")
        self.emp_id_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_id_lineEdit.setGeometry(QtCore.QRect(130, 250, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_id_lineEdit.setFont(font)
        self.emp_id_lineEdit.setObjectName("emp_id_lineEdit")
        self.emp_gender_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_gender_label.setGeometry(QtCore.QRect(430, 250, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_gender_label.setFont(font)
        self.emp_gender_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_gender_label.setObjectName("emp_gender_label")
        self.emp_id_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_id_label.setGeometry(QtCore.QRect(20, 250, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_id_label.setFont(font)
        self.emp_id_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_id_label.setObjectName("emp_id_label")
        self.emp_male_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_male_label.setGeometry(QtCore.QRect(570, 255, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_male_label.setFont(font)
        self.emp_male_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_male_label.setObjectName("emp_male_label")
        self.emp_phone_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_phone_label.setGeometry(QtCore.QRect(400, 100, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_phone_label.setFont(font)
        self.emp_phone_label.setObjectName("emp_phone_label")
        self.emp_diploma_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_diploma_lineEdit.setGeometry(QtCore.QRect(530, 200, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_diploma_lineEdit.setFont(font)
        self.emp_diploma_lineEdit.setObjectName("emp_diploma_lineEdit")
        self.emp_phone_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_phone_lineEdit.setGeometry(QtCore.QRect(530, 100, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_phone_lineEdit.setFont(font)
        self.emp_phone_lineEdit.setObjectName("emp_phone_lineEdit")
        self.emp_ln_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_ln_label.setGeometry(QtCore.QRect(30, 150, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_ln_label.setFont(font)
        self.emp_ln_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_ln_label.setObjectName("emp_ln_label")
        self.emp_diploma_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_diploma_label.setGeometry(QtCore.QRect(430, 200, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_diploma_label.setFont(font)
        self.emp_diploma_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_diploma_label.setWordWrap(True)
        self.emp_diploma_label.setObjectName("emp_diploma_label")
        self.emp_birthmonth_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.emp_birthmonth_comboBox.setGeometry(QtCore.QRect(613, 150, 85, 25))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_birthmonth_comboBox.setFont(font)
        self.emp_birthmonth_comboBox.setStyleSheet("/* style for the QComboBox */\n"
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
        self.emp_birthmonth_comboBox.setObjectName("emp_birthmonth_comboBox")
        self.emp_nid_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_nid_lineEdit.setGeometry(QtCore.QRect(130, 200, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_nid_lineEdit.setFont(font)
        self.emp_nid_lineEdit.setObjectName("emp_nid_lineEdit")
        self.emp_nid_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_nid_label.setGeometry(QtCore.QRect(30, 200, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_nid_label.setFont(font)
        self.emp_nid_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_nid_label.setObjectName("emp_nid_label")
        self.emp_birthday_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.emp_birthday_comboBox.setGeometry(QtCore.QRect(700, 150, 85, 25))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_birthday_comboBox.setFont(font)
        self.emp_birthday_comboBox.setStyleSheet("/* style for the QComboBox */\n"
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
        self.emp_birthday_comboBox.setObjectName("emp_birthday_comboBox")
        self.emp_birthdate_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_birthdate_label.setGeometry(QtCore.QRect(430, 148, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_birthdate_label.setFont(font)
        self.emp_birthdate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_birthdate_label.setObjectName("emp_birthdate_label")
        self.emp_male_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.emp_male_radioButton.setGeometry(QtCore.QRect(620, 255, 16, 17))
        self.emp_male_radioButton.setText("")
        self.emp_male_radioButton.setObjectName("emp_male_radioButton")
        self.emp_female_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.emp_female_radioButton.setGeometry(QtCore.QRect(720, 255, 16, 17))
        self.emp_female_radioButton.setText("")
        self.emp_female_radioButton.setObjectName("emp_female_radioButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_emp_Button.setText(_translate("MainWindow", "Complete"))
        self.top_inf_e_label.setText(_translate("MainWindow", "Insert Your Informations"))
        self.emp_female_label.setText(_translate("MainWindow", "Female"))
        self.emp_fn_label.setText(_translate("MainWindow", "First Name:"))
        self.emp_gender_label.setText(_translate("MainWindow", "Gender:"))
        self.emp_id_label.setText(_translate("MainWindow", "Employee ID:"))
        self.emp_male_label.setText(_translate("MainWindow", "Male"))
        self.emp_phone_label.setText(_translate("MainWindow", "Phone Number:"))
        self.emp_ln_label.setText(_translate("MainWindow", "Last Name:"))
        self.emp_diploma_label.setText(_translate("MainWindow", "Diploma:"))
        self.emp_nid_label.setText(_translate("MainWindow", "National ID:"))
        self.emp_birthdate_label.setText(_translate("MainWindow", "Birthdate:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_add_employee()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
