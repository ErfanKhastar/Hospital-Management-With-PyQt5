
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_employee_information(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 415)
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
        self.emp_nid_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_nid_sh_t_label.setGeometry(QtCore.QRect(420, 130, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_nid_sh_t_label.setFont(font)
        self.emp_nid_sh_t_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_nid_sh_t_label.setObjectName("emp_nid_sh_t_label")
        self.emp_nid_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_nid_sh_d_label.setGeometry(QtCore.QRect(520, 130, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_nid_sh_d_label.setFont(font)
        self.emp_nid_sh_d_label.setText("")
        self.emp_nid_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_nid_sh_d_label.setObjectName("emp_nid_sh_d_label")
        self.emp_id_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_id_sh_d_label.setGeometry(QtCore.QRect(520, 180, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_id_sh_d_label.setFont(font)
        self.emp_id_sh_d_label.setText("")
        self.emp_id_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_id_sh_d_label.setObjectName("emp_id_sh_d_label")
        self.emp_sh_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_sh_label.setGeometry(QtCore.QRect(20, 80, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_sh_label.setFont(font)
        self.emp_sh_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_sh_label.setObjectName("emp_sh_label")
        self.emp_birthdate_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_birthdate_sh_d_label.setGeometry(QtCore.QRect(120, 280, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_birthdate_sh_d_label.setFont(font)
        self.emp_birthdate_sh_d_label.setText("")
        self.emp_birthdate_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_birthdate_sh_d_label.setObjectName("emp_birthdate_sh_d_label")
        self.emp_phone_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_phone_sh_t_label.setGeometry(QtCore.QRect(410, 280, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_phone_sh_t_label.setFont(font)
        self.emp_phone_sh_t_label.setObjectName("emp_phone_sh_t_label")
        self.emp_phone_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_phone_sh_d_label.setGeometry(QtCore.QRect(530, 280, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_phone_sh_d_label.setFont(font)
        self.emp_phone_sh_d_label.setText("")
        self.emp_phone_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_phone_sh_d_label.setObjectName("emp_phone_sh_d_label")
        self.edit_emp_inf_Button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_emp_inf_Button.setGeometry(QtCore.QRect(290, 330, 200, 70))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.edit_emp_inf_Button.setFont(font)
        self.edit_emp_inf_Button.setObjectName("edit_emp_inf_Button")
        self.emp_sh_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.emp_sh_comboBox.setGeometry(QtCore.QRect(110, 78, 231, 35))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.emp_sh_comboBox.setFont(font)
        self.emp_sh_comboBox.setStyleSheet("/* style for the QComboBox */\n"
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
"    background-color: #a9af9e; /* آبی تیره‌تر */\n"
"    color: black; /* رنگ متن آیتم‌ها */\n"
"    selection-background-color: #F3E9E2; /* رنگ پس‌زمینه آیتم انتخاب‌شده */\n"
"    selection-color: black; /* رنگ متن آیتم انتخاب‌شده */\n"
"}")
        self.emp_sh_comboBox.setObjectName("emp_sh_comboBox")
        self.emp_fn_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_fn_sh_d_label.setGeometry(QtCore.QRect(120, 130, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_fn_sh_d_label.setFont(font)
        self.emp_fn_sh_d_label.setText("")
        self.emp_fn_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_fn_sh_d_label.setObjectName("emp_fn_sh_d_label")
        self.emp_gender_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_gender_sh_d_label.setGeometry(QtCore.QRect(120, 230, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_gender_sh_d_label.setFont(font)
        self.emp_gender_sh_d_label.setText("")
        self.emp_gender_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_gender_sh_d_label.setObjectName("emp_gender_sh_d_label")
        self.emp_ln_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_ln_sh_t_label.setGeometry(QtCore.QRect(20, 180, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_ln_sh_t_label.setFont(font)
        self.emp_ln_sh_t_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_ln_sh_t_label.setObjectName("emp_ln_sh_t_label")
        self.emp_fn_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_fn_sh_t_label.setGeometry(QtCore.QRect(20, 130, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_fn_sh_t_label.setFont(font)
        self.emp_fn_sh_t_label.setObjectName("emp_fn_sh_t_label")
        self.emp_gender_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_gender_sh_t_label.setGeometry(QtCore.QRect(20, 230, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_gender_sh_t_label.setFont(font)
        self.emp_gender_sh_t_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_gender_sh_t_label.setObjectName("emp_gender_sh_t_label")
        self.emp_birthdate_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_birthdate_sh_t_label.setGeometry(QtCore.QRect(20, 280, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_birthdate_sh_t_label.setFont(font)
        self.emp_birthdate_sh_t_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_birthdate_sh_t_label.setObjectName("emp_birthdate_sh_t_label")
        self.emp_ln_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_ln_sh_d_label.setGeometry(QtCore.QRect(120, 180, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_ln_sh_d_label.setFont(font)
        self.emp_ln_sh_d_label.setText("")
        self.emp_ln_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_ln_sh_d_label.setObjectName("emp_ln_sh_d_label")
        self.emp_id_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_id_sh_t_label.setGeometry(QtCore.QRect(415, 180, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_id_sh_t_label.setFont(font)
        self.emp_id_sh_t_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_id_sh_t_label.setObjectName("emp_id_sh_t_label")
        self.top_inf_she_label = QtWidgets.QLabel(self.centralwidget)
        self.top_inf_she_label.setGeometry(QtCore.QRect(205, 10, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.top_inf_she_label.setFont(font)
        self.top_inf_she_label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_inf_she_label.setObjectName("top_inf_she_label")
        self.emp_diploma_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_diploma_sh_d_label.setGeometry(QtCore.QRect(520, 230, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_diploma_sh_d_label.setFont(font)
        self.emp_diploma_sh_d_label.setText("")
        self.emp_diploma_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_diploma_sh_d_label.setObjectName("emp_diploma_sh_d_label")
        self.emp_diploma_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.emp_diploma_sh_t_label.setGeometry(QtCore.QRect(420, 230, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.emp_diploma_sh_t_label.setFont(font)
        self.emp_diploma_sh_t_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emp_diploma_sh_t_label.setWordWrap(True)
        self.emp_diploma_sh_t_label.setObjectName("emp_diploma_sh_t_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.emp_nid_sh_t_label.setText(_translate("MainWindow", "National ID:"))
        self.emp_sh_label.setText(_translate("MainWindow", "Employee:"))
        self.emp_phone_sh_t_label.setText(_translate("MainWindow", "Phone Number:"))
        self.edit_emp_inf_Button.setText(_translate("MainWindow", "Edit Information"))
        self.emp_ln_sh_t_label.setText(_translate("MainWindow", "Last Name:"))
        self.emp_fn_sh_t_label.setText(_translate("MainWindow", "First Name:"))
        self.emp_gender_sh_t_label.setText(_translate("MainWindow", "Gender:"))
        self.emp_birthdate_sh_t_label.setText(_translate("MainWindow", "Birthdate:"))
        self.emp_id_sh_t_label.setText(_translate("MainWindow", "Employee ID:"))
        self.top_inf_she_label.setText(_translate("MainWindow", "Search For Informations"))
        self.emp_diploma_sh_t_label.setText(_translate("MainWindow", "Diploma:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_employee_information()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
