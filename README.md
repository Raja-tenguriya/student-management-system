#  Student Management System using Django

A simple **CRUD (Create, Read, Update, Delete)** web application built with **Python Django** and **Tailwind CSS** for managing student records like Roll No., Name, Class, and City.

## Features

- Add new student record  
- Display list of all students  
- Edit student details  
- Delete student record  
- Roll number is uniquely validated  
- Built using Django class-based views  
- Tailwind CSS for styling  

###### Installation & Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/student-management-django.git
cd student-management-django
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Then open in browser: `http://127.0.0.1:8000/`

---

## Tech Stack

- **Backend:** Django (Class-based Views)
- **Frontend:** HTML, Tailwind CSS
- **Database:** SQLite (default)
- **Forms:** Django ModelForm

---

## Unique Roll Number Feature

- The roll field is marked as `unique=True` in `models.py`
- Duplicate roll entries will raise validation errors
- Duplicates must be cleaned manually before applying the `unique` constraint

## Sample Admin Setup

To create superuser (for admin panel):

```bash
python manage.py createsuperuser
```

Login at: `http://127.0.0.1:8000/admin/`


This project is open-source and free to use.

## Credits

Created by **Raja Tenguriya** as part of a learning project.  
Feel free to suggest improvements or raise issues.
