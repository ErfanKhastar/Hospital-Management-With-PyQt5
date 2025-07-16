import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def connect():
    return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )


def mydb():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    cursor = conn.cursor()

    # Create Database
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS hospital"
    )

    cursor.execute("USE hospital")

    # Patients Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Patient(
        ID INT AUTO_INCREMENT PRIMARY KEY,
        First_Name VARCHAR(20),
        Last_Name VARCHAR(30),
        Gender VARCHAR(10),
        National_ID VARCHAR(15),
        Phone_Number VARCHAR(15),
        Birthdate VARCHAR(20),
        Detail VARCHAR(100)
        )
        ''')

    # Employees Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employee(
        ID INT AUTO_INCREMENT PRIMARY KEY,
        First_Name VARCHAR(20),
        Last_Name VARCHAR(30),
        Gender VARCHAR(10),
        National_ID VARCHAR(15),
        Employee_ID VARCHAR(15),
        Phone_Number VARCHAR(15),
        Diploma VARCHAR(25),
        Birthdate VARCHAR(20)
        )
        ''')

    cursor.close()
    conn.close()


def insert_patient(data: dict):

    conn = connect()
    cursor = conn.cursor()

    query = '''
        INSERT INTO Patient
        (First_Name, Last_Name, Gender, National_ID, Phone_Number, Birthdate, Detail)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''

    values = (
        data["First_Name"], data["Last_Name"], data["Gender"], data["National_ID"],
        data["Phone_Number"], data["Birthdate"], data["Detail"]
    )

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def insert_employee(data: dict):
    conn = connect()
    cursor = conn.cursor()

    query = '''
        INSERT INTO Employee
        (First_Name, Last_Name, Gender, National_ID, Employee_ID, Phone_Number, Diploma, Birthdate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''

    values = (
        data["First_Name"], data["Last_Name"], data["Gender"], data["National_ID"],
        data["Employee_ID"], data["Phone_Number"], data["Diploma"], data["Birthdate"]
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def patient_list():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT ID, First_Name, Last_Name FROM Patient")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_patient_by_id(patient_id):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Patient WHERE ID=%s", (patient_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row


def update_patient(data: dict):
    conn = connect()
    cursor = conn.cursor()
    query = '''
        UPDATE Patient SET
            First_Name = %s,
            Last_Name = %s,
            Gender = %s,
            National_ID = %s,
            Phone_Number = %s,
            Birthdate = %s,
            Detail = %s
        WHERE ID = %s
    '''
    values = (
        data["First_Name"],
        data["Last_Name"],
        data["Gender"],
        data["National_ID"],
        data["Phone_Number"],
        data["Birthdate"],
        data["Detail"],
        data["ID"]
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def employee_list():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT ID, First_Name, Last_Name FROM Employee")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_employee_by_id(employee_id):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Employee WHERE ID=%s", (employee_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row


def update_employee(data: dict):
    conn = connect()
    cursor = conn.cursor()
    query = '''
        UPDATE Employee SET
            First_Name = %s,
            Last_Name = %s,
            Gender = %s,
            National_ID = %s,
            Employee_ID = %s,
            Phone_Number = %s,
            Diploma = %s,
            Birthdate = %s
        WHERE ID = %s
    '''
    values = (
        data["First_Name"],
        data["Last_Name"],
        data["Gender"],
        data["National_ID"],
        data["Employee_ID"],
        data["Phone_Number"],
        data["Diploma"],
        data["Birthdate"],
        data["ID"]
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


mydb()
