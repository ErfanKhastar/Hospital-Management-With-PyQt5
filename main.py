import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QLabel,
    QPushButton, QLineEdit, QTextEdit,
    QComboBox, QCheckBox, QMessageBox )
from add_patient import Ui_add_patient
from add_employee import Ui_add_employee
from patient_information import Ui_patient_information
from employee_information import Ui_employee_information
from patient_inf_edit import Ui_patient_inf_edit
from employee_inf_edit import Ui_employee_inf_edit
import Database


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load The UI File
        uic.loadUi("D:/Python/Projects/GitHub_PR/Hospital Management/main.ui", self)
        # Set the app"s title
        self.setWindowTitle("Hospital Management")

        # Define Our Widgets
        self.order_label = self.findChild(QLabel, "order_label")
        self.add_pt_order_button = self.findChild(QPushButton, "add_pt_order_Button")
        self.add_emp_order_button = self.findChild(QPushButton, "add_emp_order_Button")
        self.pt_inf_order_button = self.findChild(QPushButton, "pt_inf_order_Button")
        self.emp_inf_order_button = self.findChild(QPushButton, "emp_inf_order_Button")

        # Click The Button
        self.add_pt_order_button.clicked.connect(self.add_pt_order)
        self.add_emp_order_button.clicked.connect(self.add_emp_order)
        self.pt_inf_order_button.clicked.connect(self.pt_inf_order)
        self.emp_inf_order_button.clicked.connect(self.emp_inf_order)

        # Show The App
        self.show()


    def add_pt_order(self):
        self.OpenAddPatientWindow()


    def add_emp_order(self):
        self.OpenAddEmployeeWindow()


    def pt_inf_order(self):
        self.OpenPatientInformationWindow()


    def emp_inf_order(self):
        self.OpenEmployeeInformationWindow()


    # Open "add patient" window
    def OpenAddPatientWindow(self):
        self.add_pt_window = QMainWindow()
        self.add_pt_Ui = Ui_add_patient()
        self.add_pt_Ui.setupUi(self.add_pt_window)
        # Show the window
        self.add_pt_window.show()
        # Connect function to button
        self.add_pt_Ui.add_pt_Button.clicked.connect(self.add_patient)

        self.add_pt_Ui.pt_birthyear_comboBox.addItems([str(year) for year in range(1900, 2026)])
        self.add_pt_Ui.pt_birthmonth_comboBox.addItems([
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])
        self.add_pt_Ui.pt_birthday_comboBox.addItems([str(day) for day in range(1, 32)])


    # Open "add employee" window
    def OpenAddEmployeeWindow(self):
        self.add_emp_window = QMainWindow()
        self.add_emp_Ui = Ui_add_employee()
        self.add_emp_Ui.setupUi(self.add_emp_window)
        # Show the window
        self.add_emp_window.show()
        # Connect function to button
        self.add_emp_Ui.add_emp_Button.clicked.connect(self.add_employee)

        self.add_emp_Ui.emp_birthyear_comboBox.addItems([str(year) for year in range(1900, 2026)])
        self.add_emp_Ui.emp_birthmonth_comboBox.addItems([
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])
        self.add_emp_Ui.emp_birthday_comboBox.addItems([str(day) for day in range(1, 32)])


    # Open "patient information" window
    def OpenPatientInformationWindow(self):
        self.pt_inf_window = QMainWindow()
        self.pt_inf_Ui = Ui_patient_information()
        self.pt_inf_Ui.setupUi(self.pt_inf_window)
        # Show the window
        self.pt_inf_window.show()

        self.patient_inf()
        # Connect function to button
        self.pt_inf_Ui.edit_pt_inf_Button.clicked.connect(self.OpenPatientInformationEditWindow)


    # Open "employee information" window
    def OpenEmployeeInformationWindow(self):
        self.emp_inf_window = QMainWindow()
        self.emp_inf_Ui = Ui_employee_information()
        self.emp_inf_Ui.setupUi(self.emp_inf_window)
        # Show the window
        self.emp_inf_window.show()

        self.employee_inf()
        # Connect function to button
        self.emp_inf_Ui.edit_emp_inf_Button.clicked.connect(self.OpenEmployeeInformationEditWindow)



    # Open "Patient information edit" window
    def OpenPatientInformationEditWindow(self):
        self.pt_inf_window.close()
        self.pt_inf_edit_window = QMainWindow()
        self.pt_inf_edit_Ui = Ui_patient_inf_edit()
        self.pt_inf_edit_Ui.setupUi(self.pt_inf_edit_window)
        # Show the window
        self.pt_inf_edit_window.show()

        self.pt_inf_edit_Ui.pt_birthyear_e_comboBox.addItems([str(year) for year in range(1900, 2026)])
        self.pt_inf_edit_Ui.pt_brithmonth_e_comboBox.addItems([
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])
        self.pt_inf_edit_Ui.pt_birthday_e_comboBox.addItems([str(day) for day in range(1, 32)])

        self.pt_inf_edit_Ui.pt_fn_e_lineEdit.setText(self.pt_inf_Ui.pt_fn_sh_d_label.text())
        self.pt_inf_edit_Ui.pt_ln_e_lineEdit.setText(self.pt_inf_Ui.pt_ln_sh_d_label.text())
        self.pt_inf_edit_Ui.pt_nid_e_lineEdit.setText(self.pt_inf_Ui.pt_nid_sh_d_label.text())
        self.pt_inf_edit_Ui.pt_phone_e_lineEdit.setText(self.pt_inf_Ui.pt_phone_sh_d_label.text())
        self.pt_inf_edit_Ui.pt_detail_e_textEdit.setText(self.pt_inf_Ui.pt_detail_sh_d_label.text())

        # Connect function to button
        self.pt_inf_edit_Ui.add_pt_e_Button.clicked.connect(self.edit_patient)


    # Open "employee information edit" window
    def OpenEmployeeInformationEditWindow(self):
        self.emp_inf_window.close()
        self.emp_inf_edit_window = QMainWindow()
        self.emp_inf_edit_Ui = Ui_employee_inf_edit()
        self.emp_inf_edit_Ui.setupUi(self.emp_inf_edit_window)
        # Show the window
        self.emp_inf_edit_window.show()

        self.emp_inf_edit_Ui.emp_birthyear_e_comboBox.addItems([str(year) for year in range(1900, 2026)])
        self.emp_inf_edit_Ui.emp_brithmonth_e_comboBox.addItems([
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])
        self.emp_inf_edit_Ui.emp_birthday_e_comboBox.addItems([str(day) for day in range(1, 32)])

        self.emp_inf_edit_Ui.emp_fn_e_lineEdit.setText(self.emp_inf_Ui.emp_fn_sh_d_label.text())
        self.emp_inf_edit_Ui.emp_ln_e_lineEdit.setText(self.emp_inf_Ui.emp_ln_sh_d_label.text())
        self.emp_inf_edit_Ui.emp_nid_e_lineEdit.setText(self.emp_inf_Ui.emp_nid_sh_d_label.text())
        self.emp_inf_edit_Ui.emp_id_e_lineEdit.setText(self.emp_inf_Ui.emp_id_sh_d_label.text())
        self.emp_inf_edit_Ui.emp_phone_e_lineEdit.setText(self.emp_inf_Ui.emp_phone_sh_d_label.text())
        self.emp_inf_edit_Ui.emp_diploma_e_lineEdit.setText(self.emp_inf_Ui.emp_diploma_sh_d_label.text())

        # Connect function to button
        self.emp_inf_edit_Ui.add_emp_e_Button.clicked.connect(self.edit_employee)


    def add_patient(self):

        try:
            Ui = self.add_pt_Ui

            first_name = Ui.pt_fn_lineEdit.text()
            last_name = Ui.pt_ln_lineEdit.text()
            national_id = Ui.pt_nid_lineEdit.text()
            phone_number = Ui.pt_phone_lineEdit.text()
            detail = Ui.pt_detail_textEdit.toPlainText()

            if not all([first_name, last_name, national_id, phone_number]):
                raise Exception("Please fill all required fields.")

            if not (Ui.pt_male_radioButton.isChecked() or Ui.pt_female_radioButton.isChecked()):
                raise Exception("Please choose a gender.")

            gender = "Male" if Ui.pt_male_radioButton.isChecked() else "Female"

            year = Ui.pt_birthyear_comboBox.currentText()
            month_name = Ui.pt_birthmonth_comboBox.currentText()
            day = Ui.pt_birthday_comboBox.currentText()

            months_dict = {
                "January": "01", "February": "02", "March": "03", "April": "04",
                "May": "05", "June": "06", "July": "07", "August": "08",
                "September": "09", "October": "10", "November": "11", "December": "12"
            }

            day = day.zfill(2)
            month = months_dict.get(month_name, "01")
            birthdate = f"{year}-{month}-{day}"

            data = {
                "First_Name": first_name,
                "Last_Name": last_name,
                "Gender": gender,
                "National_ID": national_id,
                "Phone_Number": phone_number,
                "Birthdate": birthdate,
                "Detail": detail
            }

            Database.insert_patient(data)

            self.add_pt_window.close()

        except Exception as e:
            self.show_error_message(str(e), "Input Error")


    def add_employee(self):

        try:
            Ui = self.add_emp_Ui

            first_name = Ui.emp_fn_lineEdit.text()
            last_name = Ui.emp_ln_lineEdit.text()
            national_id = Ui.emp_nid_lineEdit.text()
            phone_number = Ui.emp_phone_lineEdit.text()
            diploma = Ui.emp_diploma_lineEdit.text()
            Employee_id = Ui.emp_id_lineEdit.text()

            if not all([first_name, last_name, national_id, phone_number, diploma, Employee_id]):
                raise Exception("Please fill all required fields.")

            if not (Ui.emp_male_radioButton.isChecked() or Ui.emp_female_radioButton.isChecked()):
                raise Exception("Please choose a gender.")

            gender = "Male" if Ui.emp_male_radioButton.isChecked() else "Female"

            year = Ui.emp_birthyear_comboBox.currentText()
            month_name = Ui.emp_birthmonth_comboBox.currentText()
            day = Ui.emp_birthday_comboBox.currentText()

            months_dict = {
                "January": "01", "February": "02", "March": "03", "April": "04",
                "May": "05", "June": "06", "July": "07", "August": "08",
                "September": "09", "October": "10", "November": "11", "December": "12"
            }

            day = day.zfill(2)
            month = months_dict.get(month_name, "01")
            birthdate = f"{year}-{month}-{day}"

            data = {
                "First_Name": first_name,
                "Last_Name": last_name,
                "Gender": gender,
                "National_ID": national_id,
                "Employee_ID": Employee_id,
                "Phone_Number": phone_number,
                "Diploma": diploma,
                "Birthdate": birthdate
            }


            Database.insert_employee(data)

            self.add_emp_window.close()

        except Exception as e:
            self.show_error_message(str(e), "Input Error")


    def patient_inf(self):
        self.pt_inf_Ui.pt_search_comboBox.addItem(f"Choose Patient Here!", None)
        for row in Database.patient_list():
            ID , first_name, last_name = row
            self.pt_inf_Ui.pt_search_comboBox.addItem(f"{first_name} {last_name}", ID)

        self.pt_inf_Ui.pt_search_comboBox.currentIndexChanged.connect(self.display_patient_info)


    def display_patient_info(self):
        selected_id = self.pt_inf_Ui.pt_search_comboBox.currentData()

        if selected_id is None:
            self.pt_inf_Ui.pt_fn_sh_d_label.clear()
            self.pt_inf_Ui.pt_ln_sh_d_label.clear()
            self.pt_inf_Ui.pt_gender_sh_d_label.clear()
            self.pt_inf_Ui.pt_nid_sh_d_label.clear()
            self.pt_inf_Ui.pt_phone_sh_d_label.clear()
            self.pt_inf_Ui.pt_birthdate_sh_d_label.clear()
            self.pt_inf_Ui.pt_detail_sh_d_label.clear()
            return

        patient = Database.get_patient_by_id(selected_id)

        if patient:
            self.pt_inf_Ui.pt_fn_sh_d_label.setText(str(patient["First_Name"] or ""))
            self.pt_inf_Ui.pt_ln_sh_d_label.setText(str(patient["Last_Name"] or ""))
            self.pt_inf_Ui.pt_gender_sh_d_label.setText(str(patient["Gender"] or ""))
            self.pt_inf_Ui.pt_nid_sh_d_label.setText(str(patient["National_ID"] or ""))
            self.pt_inf_Ui.pt_phone_sh_d_label.setText(str(patient["Phone_Number"] or ""))
            self.pt_inf_Ui.pt_birthdate_sh_d_label.setText(str(patient["Birthdate"] or ""))
            self.pt_inf_Ui.pt_detail_sh_d_label.setText(str(patient["Detail"] or ""))


    def employee_inf(self):
        self.emp_inf_Ui.emp_sh_comboBox.addItem(f"Choose Employee Here!", None)
        for row in Database.employee_list():
            ID, first_name, last_name = row
            self.emp_inf_Ui.emp_sh_comboBox.addItem(f"{first_name} {last_name}", ID)

        self.emp_inf_Ui.emp_sh_comboBox.currentIndexChanged.connect(self.display_employee_info)


    def display_employee_info(self):
        selected_id = self.emp_inf_Ui.emp_sh_comboBox.currentData()

        if selected_id is None:
            self.emp_inf_Ui.emp_fn_sh_d_label.clear()
            self.emp_inf_Ui.emp_ln_sh_d_label.clear()
            self.emp_inf_Ui.emp_gender_sh_d_label.clear()
            self.emp_inf_Ui.emp_nid_sh_d_label.clear()
            self.emp_inf_Ui.emp_id_sh_d_label.clear()
            self.emp_inf_Ui.emp_phone_sh_d_label.clear()
            self.emp_inf_Ui.emp_diploma_sh_d_label.clear()
            self.emp_inf_Ui.emp_birthdate_sh_d_label.clear()
            return

        employee = Database.get_employee_by_id(selected_id)

        if employee:
            self.emp_inf_Ui.emp_fn_sh_d_label.setText(str(employee["First_Name"] or ""))
            self.emp_inf_Ui.emp_ln_sh_d_label.setText(str(employee["Last_Name"] or ""))
            self.emp_inf_Ui.emp_gender_sh_d_label.setText(str(employee["Gender"] or ""))
            self.emp_inf_Ui.emp_nid_sh_d_label.setText(str(employee["National_ID"] or ""))
            self.emp_inf_Ui.emp_id_sh_d_label.setText(str(employee["Employee_ID"] or ""))
            self.emp_inf_Ui.emp_phone_sh_d_label.setText(str(employee["Phone_Number"] or ""))
            self.emp_inf_Ui.emp_diploma_sh_d_label.setText(str(employee["Diploma"] or ""))
            self.emp_inf_Ui.emp_birthdate_sh_d_label.setText(str(employee["Birthdate"] or ""))


    def edit_patient(self):

        try:
            Ui = self.pt_inf_edit_Ui

            first_name = Ui.pt_fn_e_lineEdit.text()
            last_name = Ui.pt_ln_e_lineEdit.text()
            national_id = Ui.pt_nid_e_lineEdit.text()
            phone_number = Ui.pt_phone_e_lineEdit.text()
            detail = Ui.pt_detail_e_textEdit.toPlainText()
            ID = self.pt_inf_Ui.pt_search_comboBox.currentData()

            if not all([first_name, last_name, national_id, phone_number]):
                raise Exception("Please fill all required fields.")

            if not (Ui.pt_e_male_radioButton.isChecked() or Ui.pt_e_female_radioButton.isChecked()):
                raise Exception("Please choose a gender.")

            gender = "Male" if Ui.pt_e_male_radioButton.isChecked() else "Female"

            year = Ui.pt_birthyear_e_comboBox.currentText()
            month_name = Ui.pt_brithmonth_e_comboBox.currentText()
            day = Ui.pt_birthday_e_comboBox.currentText()

            months_dict = {
                "January": "01", "February": "02", "March": "03", "April": "04",
                "May": "05", "June": "06", "July": "07", "August": "08",
                "September": "09", "October": "10", "November": "11", "December": "12"
            }

            day = day.zfill(2)
            month = months_dict.get(month_name, "01")
            birthdate = f"{year}-{month}-{day}"

            data = {
                "First_Name": first_name,
                "Last_Name": last_name,
                "Gender": gender,
                "National_ID": national_id,
                "Phone_Number": phone_number,
                "Birthdate": birthdate,
                "Detail": detail,
                "ID": ID
            }

            Database.update_patient(data)

            self.pt_inf_edit_window.close()

        except Exception as e:
            self.show_error_message(str(e), "Input Error")


    def edit_employee(self):

        try:
            Ui = self.emp_inf_edit_Ui

            first_name = Ui.emp_fn_e_lineEdit.text()
            last_name = Ui.emp_ln_e_lineEdit.text()
            national_id = Ui.emp_nid_e_lineEdit.text()
            Employee_id = Ui.emp_id_e_lineEdit.text()
            phone_number = Ui.emp_phone_e_lineEdit.text()
            diploma = Ui.emp_diploma_e_lineEdit.text()
            ID = self.emp_inf_Ui.emp_sh_comboBox.currentData()

            if not all([first_name, last_name, national_id, phone_number, diploma, Employee_id]):
                raise Exception("Please fill all required fields.")

            if not (Ui.emp_e_male_radioButton.isChecked() or Ui.emp_e_female_radioButton.isChecked()):
                raise Exception("Please choose a gender.")

            gender = "Male" if Ui.emp_e_male_radioButton.isChecked() else "Female"

            year = Ui.emp_birthyear_e_comboBox.currentText()
            month_name = Ui.emp_brithmonth_e_comboBox.currentText()
            day = Ui.emp_birthday_e_comboBox.currentText()

            months_dict = {
                "January": "01", "February": "02", "March": "03", "April": "04",
                "May": "05", "June": "06", "July": "07", "August": "08",
                "September": "09", "October": "10", "November": "11", "December": "12"
            }

            day = day.zfill(2)
            month = months_dict.get(month_name, "01")
            birthdate = f"{year}-{month}-{day}"

            data = {
                "First_Name": first_name,
                "Last_Name": last_name,
                "Gender": gender,
                "National_ID": national_id,
                "Employee_ID": Employee_id,
                "Phone_Number": phone_number,
                "Diploma": diploma,
                "Birthdate": birthdate,
                "ID": ID
            }

            Database.update_employee(data)

            self.emp_inf_edit_window.close()

        except Exception as e:
            self.show_error_message(str(e), "Input Error")


    def show_error_message(self, message, title="Error"):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setText(message)
        msg.exec_()

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
