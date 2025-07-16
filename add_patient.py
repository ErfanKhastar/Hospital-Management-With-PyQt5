
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_patient(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 417)
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
        self.pt_birthmonth_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.pt_birthmonth_comboBox.setGeometry(QtCore.QRect(607, 150, 85, 25))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_birthmonth_comboBox.setFont(font)
        self.pt_birthmonth_comboBox.setStyleSheet("/* style for the QComboBox */\n"
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
        self.pt_birthmonth_comboBox.setObjectName("pt_birthmonth_comboBox")
        self.pt_birthdate_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_birthdate_label.setGeometry(QtCore.QRect(420, 148, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_birthdate_label.setFont(font)
        self.pt_birthdate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_birthdate_label.setObjectName("pt_birthdate_label")
        self.pt_ln_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pt_ln_lineEdit.setGeometry(QtCore.QRect(130, 150, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_ln_lineEdit.setFont(font)
        self.pt_ln_lineEdit.setObjectName("pt_ln_lineEdit")
        self.pt_ln_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_ln_label.setGeometry(QtCore.QRect(30, 150, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_ln_label.setFont(font)
        self.pt_ln_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_ln_label.setObjectName("pt_ln_label")
        self.pt_phone_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pt_phone_lineEdit.setGeometry(QtCore.QRect(530, 100, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_phone_lineEdit.setFont(font)
        self.pt_phone_lineEdit.setObjectName("pt_phone_lineEdit")
        self.pt_female_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_female_label.setGeometry(QtCore.QRect(250, 260, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pt_female_label.setFont(font)
        self.pt_female_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_female_label.setObjectName("pt_female_label")
        self.pt_fn_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_fn_label.setGeometry(QtCore.QRect(30, 100, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_fn_label.setFont(font)
        self.pt_fn_label.setObjectName("pt_fn_label")
        self.pt_gender_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_gender_label.setGeometry(QtCore.QRect(30, 253, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_gender_label.setFont(font)
        self.pt_gender_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_gender_label.setObjectName("pt_gender_label")
        self.pt_nid_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_nid_label.setGeometry(QtCore.QRect(30, 200, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_nid_label.setFont(font)
        self.pt_nid_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_nid_label.setObjectName("pt_nid_label")
        self.pt_nid_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pt_nid_lineEdit.setGeometry(QtCore.QRect(130, 200, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_nid_lineEdit.setFont(font)
        self.pt_nid_lineEdit.setObjectName("pt_nid_lineEdit")
        self.pt_birthyear_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.pt_birthyear_comboBox.setGeometry(QtCore.QRect(520, 150, 85, 25))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_birthyear_comboBox.setFont(font)
        self.pt_birthyear_comboBox.setStyleSheet("/* style for the QComboBox */\n"
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
        self.pt_birthyear_comboBox.setObjectName("pt_birthyear_comboBox")
        self.pt_fn_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pt_fn_lineEdit.setGeometry(QtCore.QRect(130, 100, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_fn_lineEdit.setFont(font)
        self.pt_fn_lineEdit.setObjectName("pt_fn_lineEdit")
        self.pt_detail_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.pt_detail_textEdit.setGeometry(QtCore.QRect(440, 250, 341, 151))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_detail_textEdit.setFont(font)
        self.pt_detail_textEdit.setObjectName("pt_detail_textEdit")
        self.pt_birthday_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.pt_birthday_comboBox.setGeometry(QtCore.QRect(694, 150, 85, 25))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_birthday_comboBox.setFont(font)
        self.pt_birthday_comboBox.setStyleSheet("/* style for the QComboBox */\n"
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
        self.pt_birthday_comboBox.setObjectName("pt_birthday_comboBox")
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
        self.pt_male_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_male_label.setGeometry(QtCore.QRect(150, 260, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pt_male_label.setFont(font)
        self.pt_male_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_male_label.setObjectName("pt_male_label")
        self.pt_phone_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_phone_label.setGeometry(QtCore.QRect(400, 100, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_phone_label.setFont(font)
        self.pt_phone_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pt_phone_label.setObjectName("pt_phone_label")
        self.add_pt_Button = QtWidgets.QPushButton(self.centralwidget)
        self.add_pt_Button.setGeometry(QtCore.QRect(100, 309, 200, 70))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.add_pt_Button.setFont(font)
        self.add_pt_Button.setObjectName("add_pt_Button")
        self.pt_detail_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_detail_label.setGeometry(QtCore.QRect(440, 200, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pt_detail_label.setFont(font)
        self.pt_detail_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_detail_label.setWordWrap(True)
        self.pt_detail_label.setObjectName("pt_detail_label")
        self.pt_female_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.pt_female_radioButton.setGeometry(QtCore.QRect(310, 260, 16, 17))
        self.pt_female_radioButton.setText("")
        self.pt_female_radioButton.setObjectName("pt_female_radioButton")
        self.pt_male_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.pt_male_radioButton.setGeometry(QtCore.QRect(200, 260, 16, 17))
        self.pt_male_radioButton.setText("")
        self.pt_male_radioButton.setObjectName("pt_male_radioButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pt_birthdate_label.setText(_translate("MainWindow", "Birthdate:"))
        self.pt_ln_label.setText(_translate("MainWindow", "Last Name:"))
        self.pt_female_label.setText(_translate("MainWindow", "Female"))
        self.pt_fn_label.setText(_translate("MainWindow", "First Name:"))
        self.pt_gender_label.setText(_translate("MainWindow", "Gender:"))
        self.pt_nid_label.setText(_translate("MainWindow", "National ID:"))
        self.top_inf_p_label.setText(_translate("MainWindow", "Insert Your Informations"))
        self.pt_male_label.setText(_translate("MainWindow", "Male"))
        self.pt_phone_label.setText(_translate("MainWindow", "Phone Number:"))
        self.add_pt_Button.setText(_translate("MainWindow", "Complete"))
        self.pt_detail_label.setText(_translate("MainWindow", "If You Have Or Had Any Sickness                              Write That Down Here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_add_patient()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
