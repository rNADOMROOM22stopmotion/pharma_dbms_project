# MEDIFY – A Digital Medical Management System

## 1. Introduction
MEDIFY is a database-driven medical management system designed to streamline healthcare operations such as patient record management, appointment scheduling, doctor information tracking, and medical history maintenance.
The system ensures fast data access, secure storage, and efficient retrieval using a robust backend and an intuitive user interface.
It is built using:
* PostgreSQL as the primary database
* Python (Flask) for backend processing
* Supabase as the cloud database hosting service
* HTML, CSS, JavaScript, Bootstrap for frontend development

## 2. Objectives
* Design an efficient database system for managing medical data
* Provide a user-friendly interface for patients, doctors, and administrators
* Ensure secure storage and retrieval of sensitive healthcare information
* Reduce manual errors through automation
* Implement a scalable system capable of real-time data processing

## 3. Tools & Technologies Used

### 3.1 Programming Language
Python 3.14
Used for backend logic, API creation, database handling, and server-side operations.

### 3.2 Database
PostgreSQL
Chosen for its reliability, ACID compliance, and strong support for relational data structures.

### 3.3 Database Hosting Service
Supabase
Provides PostgreSQL hosting, authentication, and storage services.

### 3.4 Backend Web Framework
Flask
A lightweight Python framework used to develop RESTful routes and connect the frontend with the database.

### 3.5 Frontend Technologies
* HTML – Structure
* CSS – Styling
* JavaScript – Client-side interactivity
* Bootstrap – Responsive UI design

## 4. System Architecture

### Backend Layer
* Flask handles all backend routes
* Python interacts with PostgreSQL using psycopg2 or SQLAlchemy
* Supabase hosts the PostgreSQL database and manages authentication (optional)

### Database Layer
Key tables:
* Patients
* Doctors
* Appointments
* Medical Records
* Prescriptions
The schema is normalized to remove redundancy and ensure efficient queries.

### Frontend Layer
* HTML templates rendered using Flask’s Jinja engine
* Bootstrap for modern, responsive styling
* JavaScript for validation, AJAX requests, and dynamic components

## 5. Key Features
* User Authentication (Supabase Auth optional)
* Patient Management: Add, update, delete patient records
* Doctor Management: Manage profiles, specialization, and availability
* Appointment Scheduling: Manage dates and times
* Medical Records Tracking: Maintain diagnoses, reports, and patient history
* Prescription Management
* Responsive UI
* Database Integrity: Keys, constraints, triggers, stored procedures

## 6. ER Diagram (Conceptual Overview)
### Entities
* Patient
* Doctor
* Appointment
* Medical_Record
* Prescription

### Relationships
* A Patient books an Appointment
* A Doctor handles an Appointment
* A Patient has multiple Medical Records
* A Doctor writes Prescriptions
(If you want, I can generate the ER diagram as an image.)

## 7. Advantages
* Fast access to medical information
* Improved accuracy and data integrity
* Reduced operational workload
* Real-time data flow
* Scalable and easy to deploy
* Secure handling of sensitive data

## 8. Conclusion
The MEDIFY project demonstrates the successful integration of database management and web application development to build a secure, reliable, and user-friendly medical management platform.
By utilizing Python, PostgreSQL, Supabase, Flask, and modern frontend technologies, MEDIFY offers a scalable, secure, and maintainable solution for healthcare data management.

## 9. Project Structure

This project is structured as follows:

```
.
├───.gitignore
├───.python-version
├───main.py             # Main Flask application entry point
├───pyproject.toml      # Project dependencies and metadata
├───README.md           # This README file
├───requirements.txt    # Python dependencies
├───uv.lock             # Dependency lock file
├───wsgi.py             # WSGI entry point for deployment
├───__pycache__/        # Python cache files
├───.git/               # Git version control
├───.idea/              # PyCharm project files
├───.venv/              # Python virtual environment
├───models/             # Database models and related logic
│   ├───__init__.py
│   ├───db.py           # Database connection and utility functions
│   ├───models.py       # SQLAlchemy models for database tables
│   ├───rating.py       # Rating-related model or logic
│   └───__pycache__/
├───static/             # Static assets (CSS, JS, images)
│   ├───assets/
│   │   ├───favicon.ico
│   │   └───pill.jpg    # Image asset
│   ├───css/
│   │   ├───login.css   # Styles for login page
│   │   ├───signup.css  # Styles for signup page
│   │   └───styles.css  # General styles
│   └───js/
│       └───scripts.js  # Frontend JavaScript
└───templates/          # HTML templates
    ├───about.html
    ├───cart.html
    ├───contact.html
    ├───header.html
    ├───index.html
    ├───login.html
    ├───navbar.html
    ├───products.html
    └───signup.html
```