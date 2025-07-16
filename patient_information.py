
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_patient_information(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 405)
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
        self.pt_fn_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_fn_sh_t_label.setGeometry(QtCore.QRect(30, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_fn_sh_t_label.setFont(font)
        self.pt_fn_sh_t_label.setObjectName("pt_fn_sh_t_label")
        self.pt_nid_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_nid_sh_t_label.setGeometry(QtCore.QRect(405, 160, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_nid_sh_t_label.setFont(font)
        self.pt_nid_sh_t_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_nid_sh_t_label.setObjectName("pt_nid_sh_t_label")
        self.edit_pt_inf_Button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_pt_inf_Button.setGeometry(QtCore.QRect(100, 300, 200, 70))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.edit_pt_inf_Button.setFont(font)
        self.edit_pt_inf_Button.setObjectName("edit_pt_inf_Button")
        self.pt_birthdate_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_birthdate_sh_t_label.setGeometry(QtCore.QRect(405, 250, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_birthdate_sh_t_label.setFont(font)
        self.pt_birthdate_sh_t_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_birthdate_sh_t_label.setObjectName("pt_birthdate_sh_t_label")
        self.pt_gender_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_gender_sh_d_label.setGeometry(QtCore.QRect(130, 240, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pt_gender_sh_d_label.setFont(font)
        self.pt_gender_sh_d_label.setText("")
        self.pt_gender_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_gender_sh_d_label.setObjectName("pt_gender_sh_d_label")
        self.pt_phone_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_phone_sh_d_label.setGeometry(QtCore.QRect(520, 205, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pt_phone_sh_d_label.setFont(font)
        self.pt_phone_sh_d_label.setText("")
        self.pt_phone_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_phone_sh_d_label.setObjectName("pt_phone_sh_d_label")
        self.pt_fn_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_fn_sh_d_label.setGeometry(QtCore.QRect(130, 160, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pt_fn_sh_d_label.setFont(font)
        self.pt_fn_sh_d_label.setText("")
        self.pt_fn_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_fn_sh_d_label.setObjectName("pt_fn_sh_d_label")
        self.top_inf_shp_label = QtWidgets.QLabel(self.centralwidget)
        self.top_inf_shp_label.setGeometry(QtCore.QRect(205, 10, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.top_inf_shp_label.setFont(font)
        self.top_inf_shp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_inf_shp_label.setObjectName("top_inf_shp_label")
        self.pt_sh_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_sh_label.setGeometry(QtCore.QRect(20, 90, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_sh_label.setFont(font)
        self.pt_sh_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_sh_label.setObjectName("pt_sh_label")
        self.pt_search_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.pt_search_comboBox.setGeometry(QtCore.QRect(110, 88, 231, 35))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pt_search_comboBox.setFont(font)
        self.pt_search_comboBox.setStyleSheet("/* style for the QComboBox */\n"
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
        self.pt_search_comboBox.setObjectName("pt_search_comboBox")
        self.pt_birthdate_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_birthdate_sh_d_label.setGeometry(QtCore.QRect(520, 250, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pt_birthdate_sh_d_label.setFont(font)
        self.pt_birthdate_sh_d_label.setText("")
        self.pt_birthdate_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_birthdate_sh_d_label.setObjectName("pt_birthdate_sh_d_label")
        self.pt_phone_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_phone_sh_t_label.setGeometry(QtCore.QRect(390, 205, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_phone_sh_t_label.setFont(font)
        self.pt_phone_sh_t_label.setObjectName("pt_phone_sh_t_label")
        self.pt_gender_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_gender_sh_t_label.setGeometry(QtCore.QRect(30, 240, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_gender_sh_t_label.setFont(font)
        self.pt_gender_sh_t_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_gender_sh_t_label.setObjectName("pt_gender_sh_t_label")
        self.pt_ln_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_ln_sh_t_label.setGeometry(QtCore.QRect(30, 200, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_ln_sh_t_label.setFont(font)
        self.pt_ln_sh_t_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_ln_sh_t_label.setObjectName("pt_ln_sh_t_label")
        self.pt_ln_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_ln_sh_d_label.setGeometry(QtCore.QRect(130, 200, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pt_ln_sh_d_label.setFont(font)
        self.pt_ln_sh_d_label.setText("")
        self.pt_ln_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_ln_sh_d_label.setObjectName("pt_ln_sh_d_label")
        self.pt_nid_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_nid_sh_d_label.setGeometry(QtCore.QRect(520, 160, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pt_nid_sh_d_label.setFont(font)
        self.pt_nid_sh_d_label.setText("")
        self.pt_nid_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_nid_sh_d_label.setObjectName("pt_nid_sh_d_label")
        self.pt_detail_sh_t_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_detail_sh_t_label.setGeometry(QtCore.QRect(405, 335, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pt_detail_sh_t_label.setFont(font)
        self.pt_detail_sh_t_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_detail_sh_t_label.setObjectName("pt_detail_sh_t_label")
        self.pt_detail_sh_d_label = QtWidgets.QLabel(self.centralwidget)
        self.pt_detail_sh_d_label.setGeometry(QtCore.QRect(520, 300, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Arad Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pt_detail_sh_d_label.setFont(font)
        self.pt_detail_sh_d_label.setText("")
        self.pt_detail_sh_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_detail_sh_d_label.setWordWrap(True)
        self.pt_detail_sh_d_label.setObjectName("pt_detail_sh_d_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pt_fn_sh_t_label.setText(_translate("MainWindow", "First Name:"))
        self.pt_nid_sh_t_label.setText(_translate("MainWindow", "National ID:"))
        self.edit_pt_inf_Button.setText(_translate("MainWindow", "Edit Information"))
        self.pt_birthdate_sh_t_label.setText(_translate("MainWindow", "Birthdate:"))
        self.top_inf_shp_label.setText(_translate("MainWindow", "Search For Informations"))
        self.pt_sh_label.setText(_translate("MainWindow", "Patient:"))
        self.pt_phone_sh_t_label.setText(_translate("MainWindow", "Phone Number:"))
        self.pt_gender_sh_t_label.setText(_translate("MainWindow", "Gender:"))
        self.pt_ln_sh_t_label.setText(_translate("MainWindow", "Last Name:"))
        self.pt_detail_sh_t_label.setText(_translate("MainWindow", "Detail:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_patient_information()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
