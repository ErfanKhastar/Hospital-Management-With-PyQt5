# 🏥 Hospital Management System
A comprehensive desktop application designed to manage patient and employee records within a hospital or clinic. This system provides a full CRUD (Create, Read, Update) graphical user interface built with Python, PyQt5, and a MySQL database backend.

<br>

## ✨ Key Features
- **Dual Management Modules:** Separate, dedicated sections for managing **Patients** and **Employees**.
- **Full CRUD Functionality:**
    - **Create:** Add new patient and employee records through intuitive data entry forms.
    - **Read:** Search for specific individuals from a dropdown list and view their complete information.
    - **Update:** Easily edit and save changes to any existing patient or employee record.
- **Robust Backend:** Powered by a **MySQL** database to ensure data is stored persistently and reliably.
- **Secure Configuration:** Sensitive database credentials (host, user, password) are managed securely using a `.env` file, keeping them separate from the source code.
- **Intuitive GUI:** A multi-window graphical interface built with **PyQt5** provides a smooth and user-friendly experience, with clear navigation from a central main menu.
- **Data Integrity:** The application includes input validation to ensure that required fields are filled and prompts the user with error messages if data is missing.

<br>

## 🛠️ Technologies & Libraries
- **Programming Language:** `Python`
- **GUI Framework:** `PyQt5`
- **Database:** `MySQL`
- **Database Connector:** `mysql-connector-python`
- **Configuration:** `python-dotenv`

<br>

## 🚀 Setup and Installation
Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites
- **Python 3.9+** installed on your system.
- **MySQL Server** installed and running.

### 2. Project Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ErfanKhastar/Hospital-Management-With-PyQt5.git
    cd Hospital-Management-With-PyQt5
    ```

2.  **Create a `.env` file** in the root directory of the project. This file will store your database credentials. Add the following variables, replacing the placeholder values with your actual MySQL details:
    ```env
    DB_HOST=localhost
    DB_USER=your_mysql_user
    DB_PASSWORD=your_mysql_password
    DB_NAME=hospital
    ```

3.  **Install the required libraries.** It is recommended to use a virtual environment.
    ```bash
    # Create and activate a virtual environment (optional but recommended)
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install dependencies
    pip install PyQt5 mysql-connector-python python-dotenv
    ```

### 3. Database Initialization

The application is designed to automatically create the database and tables for you. The first time you run it, the `mydb()` function in `Database.py` will execute the following:
- `CREATE DATABASE IF NOT EXISTS hospital`
- `CREATE TABLE IF NOT EXISTS Patient`
- `CREATE TABLE IF NOT EXISTS Employee`

### 4. Running the Application

Once the setup is complete, you can run the application with the following command:
```bash
python main.py
```
This will launch the main menu, from where you can navigate to all other features of the system.
