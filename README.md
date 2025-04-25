# Interview_Scheduler-RollingArrays

Overview

The Interview Scheduling System is a web application built using Django, designed to manage and track interview assignments for applicants and interviewers. It helps HR managers and recruiters schedule, monitor, and update interview sessions effectively, ensuring a streamlined process for both applicants and interviewers.

Features

Applicant Management: Add and manage applicant details, including name and interview slots.

Interview Slot Management: Create, assign, and track interview slots for various applicants and interviewers.

Status Tracking: Track the progress of interviews (e.g., upcoming, completed).

Dynamic Filtering: Filter interview assignments based on date or other criteria to improve efficiency.

Technologies

Backend: Django

Frontend: HTML, Tailwind CSS

Database: SQLite (default; can be configured for others like PostgreSQL)

Deployment: Render for hosting

Installation Prerequisites Python 3.6+

pip (for managing dependencies)

Steps to Run Locally -> Clone the repository: git clone https://github.com/aniketgoyal51/Interview_Scheduler-RollingArrays

->Navigate into the project directory: cd employee-training-tracker

->Create a virtual environment: python -m venv venv

->Activate the virtual environment: On Windows: venv\Scripts\activate On Mac/Linux: source venv/bin/activate

->Install the required dependencies: pip install -r requirements.txt

->Apply the migrations to set up the database: python manage.py migrate

->Create a superuser to access the admin panel: python manage.py createsuperuser

->Run the development server: python manage.py runserver Access the app: Open your browser and go to http://127.0.0.1:8000/.

Deployment Employee Training Tracker - https://interview-scheduler-rollingarrays.onrender.com/

