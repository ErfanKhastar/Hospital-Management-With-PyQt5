

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_patient_inf_edit(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 410)
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
        self.pt_nid_e_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pt_nid_e_lineEdit.setGeometry(QtCore.QRect(130, 190, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_nid_e_lineEdit.setFont(font)
        self.pt_nid_e_lineEdit.setObjectName("pt_nid_e_lineEdit")
        self.pt_male_e_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_male_e_label.setGeometry(QtCore.QRect(150, 245, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pt_male_e_label.setFont(font)
        self.pt_male_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_male_e_label.setObjectName("pt_male_e_label")
        self.add_pt_e_Button = QtWidgets.QPushButton(self.centralwidget)
        self.add_pt_e_Button.setGeometry(QtCore.QRect(90, 299, 200, 70))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.add_pt_e_Button.setFont(font)
        self.add_pt_e_Button.setObjectName("add_pt_e_Button")
        self.pt_birthday_e_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.pt_birthday_e_comboBox.setGeometry(QtCore.QRect(700, 140, 85, 25))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_birthday_e_comboBox.setFont(font)
        self.pt_birthday_e_comboBox.setStyleSheet("/* style for the QComboBox */\n"
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
        self.pt_birthday_e_comboBox.setObjectName("pt_birthday_e_comboBox")
        self.pt_ln_e_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pt_ln_e_lineEdit.setGeometry(QtCore.QRect(130, 140, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_ln_e_lineEdit.setFont(font)
        self.pt_ln_e_lineEdit.setObjectName("pt_ln_e_lineEdit")
        self.pt_gender_e_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_gender_e_label.setGeometry(QtCore.QRect(30, 240, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_gender_e_label.setFont(font)
        self.pt_gender_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_gender_e_label.setObjectName("pt_gender_e_label")
        self.pt_phone_e_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pt_phone_e_lineEdit.setGeometry(QtCore.QRect(530, 90, 251, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_phone_e_lineEdit.setFont(font)
        self.pt_phone_e_lineEdit.setObjectName("pt_phone_e_lineEdit")
        self.pt_birthdate_e_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_birthdate_e_label.setGeometry(QtCore.QRect(430, 138, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_birthdate_e_label.setFont(font)
        self.pt_birthdate_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_birthdate_e_label.setObjectName("pt_birthdate_e_label")
        self.pt_brithmonth_e_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.pt_brithmonth_e_comboBox.setGeometry(QtCore.QRect(613, 140, 85, 25))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_brithmonth_e_comboBox.setFont(font)
        self.pt_brithmonth_e_comboBox.setStyleSheet("/* style for the QComboBox */\n"
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
        self.pt_brithmonth_e_comboBox.setObjectName("pt_brithmonth_e_comboBox")
        self.pt_detail_e_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_detail_e_label.setGeometry(QtCore.QRect(440, 190, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pt_detail_e_label.setFont(font)
        self.pt_detail_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_detail_e_label.setWordWrap(True)
        self.pt_detail_e_label.setObjectName("pt_detail_e_label")
        self.pt_phone_e_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_phone_e_label.setGeometry(QtCore.QRect(400, 90, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_phone_e_label.setFont(font)
        self.pt_phone_e_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pt_phone_e_label.setObjectName("pt_phone_e_label")
        self.pt_birthyear_e_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.pt_birthyear_e_comboBox.setGeometry(QtCore.QRect(526, 140, 85, 25))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_birthyear_e_comboBox.setFont(font)
        self.pt_birthyear_e_comboBox.setStyleSheet("/* style for the QComboBox */\n"
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
        self.pt_birthyear_e_comboBox.setObjectName("pt_birthyear_e_comboBox")
        self.pt_detail_e_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.pt_detail_e_textEdit.setGeometry(QtCore.QRect(440, 240, 341, 151))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_detail_e_textEdit.setFont(font)
        self.pt_detail_e_textEdit.setObjectName("pt_detail_e_textEdit")
        self.top_inf_p_label = QtWidgets.QLabel(self.centralwidget)
        self.top_inf_p_label.setGeometry(QtCore.QRect(240, 10, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.top_inf_p_label.setFont(font)
        self.top_inf_p_label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_inf_p_label.setObjectName("top_inf_p_label")
        self.pt_fn_e_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_fn_e_label.setGeometry(QtCore.QRect(30, 90, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_fn_e_label.setFont(font)
        self.pt_fn_e_label.setObjectName("pt_fn_e_label")
        self.pt_fn_e_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pt_fn_e_lineEdit.setGeometry(QtCore.QRect(130, 90, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_fn_e_lineEdit.setFont(font)
        self.pt_fn_e_lineEdit.setObjectName("pt_fn_e_lineEdit")
        self.pt_female_e_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_female_e_label.setGeometry(QtCore.QRect(250, 245, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pt_female_e_label.setFont(font)
        self.pt_female_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_female_e_label.setObjectName("pt_female_e_label")
        self.pt_nid_e_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_nid_e_label.setGeometry(QtCore.QRect(30, 190, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_nid_e_label.setFont(font)
        self.pt_nid_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_nid_e_label.setObjectName("pt_nid_e_label")
        self.pt_ln_e_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_ln_e_label.setGeometry(QtCore.QRect(30, 140, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_ln_e_label.setFont(font)
        self.pt_ln_e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_ln_e_label.setObjectName("pt_ln_e_label")
        self.pt_e_female_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.pt_e_female_radioButton.setGeometry(QtCore.QRect(310, 247, 16, 17))
        self.pt_e_female_radioButton.setText("")
        self.pt_e_female_radioButton.setObjectName("pt_e_female_radioButton")
        self.pt_e_male_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.pt_e_male_radioButton.setGeometry(QtCore.QRect(200, 247, 16, 17))
        self.pt_e_male_radioButton.setText("")
        self.pt_e_male_radioButton.setObjectName("pt_e_male_radioButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pt_male_e_label.setText(_translate("MainWindow", "Male"))
        self.add_pt_e_Button.setText(_translate("MainWindow", "Finish"))
        self.pt_gender_e_label.setText(_translate("MainWindow", "Gender:"))
        self.pt_birthdate_e_label.setText(_translate("MainWindow", "Birthdate:"))
        self.pt_detail_e_label.setText(_translate("MainWindow", "If You Have Or Had Any Sickness                              Write That Down Here"))
        self.pt_phone_e_label.setText(_translate("MainWindow", "Phone Number:"))
        self.top_inf_p_label.setText(_translate("MainWindow", "Change What You want!"))
        self.pt_fn_e_label.setText(_translate("MainWindow", "First Name:"))
        self.pt_female_e_label.setText(_translate("MainWindow", "Female"))
        self.pt_nid_e_label.setText(_translate("MainWindow", "National ID:"))
        self.pt_ln_e_label.setText(_translate("MainWindow", "Last Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_patient_inf_edit()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
