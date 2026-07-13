# Student Management System

A Django-based Student Management System that helps manage student records efficiently. The application provides an interface for performing CRUD (Create, Read, Update, Delete) operations on student data.

## Features

- Add new students
- View all student records
- Update student details
- Delete student records
- SQLite database integration
- Django Admin Panel
- Clean and responsive user interface

## Tech Stack

- Python 3
- Django
- SQLite3
- HTML
- CSS
- Bootstrap (if used)

## Project Structure

```
student_management/
│── core/
│── student_management/
│── manage.py
│── requirements.txt
│── README.md
│── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/rnikalje54/Student-management.git
```

### 2. Navigate to the project

```bash
cd Student-management
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Admin Panel

Create a superuser:

```bash
python manage.py createsuperuser
```

Then visit:

```
http://127.0.0.1:8000/admin/
```

## Requirements

Install all required packages using:

```bash
pip install -r requirements.txt
```

## Future Enhancements

- Student authentication
- Faculty login
- Attendance management
- Marks and grades management
- Fee management
- Search and filtering
- Export data to Excel/PDF

## Author

**Ritesh Nikalje**

GitHub: https://github.com/rnikalje54
