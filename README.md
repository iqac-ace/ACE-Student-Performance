# ACE Student Academic Follow-up & Performance Analysis

Professional Django web application starter for Adhiyamaan College of Engineering (Autonomous), Hosur.

## Included
- IQAC / HOD / Faculty role-based access
- IQAC-created departments and staff usernames/passwords
- Student master profile with 12th-grade marks
- Subject master by department and semester
- Faculty Excel import for subject internal/external marks
- Separate semester result entry (SGPA, CGPA, arrears, credits)
- HOD -> IQAC two-stage authorization workflow
- 1000-point ACE Student Performance Framework with Categories A-F
- Activity/evidence upload for technical, industry, research, co-curricular, cultural, social and holistic achievements
- Search any student and see full academic + activity record
- Department dashboard and comparison report
- Audit log model
- SQLite for easy local development, PostgreSQL-ready for scale

## Quick start (Windows / VS Code)
1. Open this folder in VS Code.
2. Open Terminal.
3. Create virtual environment:
   `python -m venv .venv`
4. Activate it:
   `.venv\\Scripts\\activate`
5. Install packages:
   `pip install -r requirements.txt`
6. Create database tables:
   `python manage.py makemigrations`
   `python manage.py migrate`
7. Load the ACE 1000-point framework:
   `python manage.py seed_framework`
8. Create the first IQAC administrator:
   `python manage.py createsuperuser`
9. Run:
   `python manage.py runserver`
10. Open `http://127.0.0.1:8000/`

## First setup in the website
1. Login with the superuser.
2. Open Departments -> create CSE, ECE, EEE, IT, MECH, CIVIL, etc.
3. Use Create Staff Login to create HOD and Faculty users with department mapping.
4. Add subjects by semester.
5. Add/import students.
6. Faculty uploads marks via Excel.
7. HOD approves first; IQAC approves second.
8. Add semester results and activities/evidence.
9. Search a student to view the complete performance record.

## Excel marks format
Columns: Register Number | Subject Code | Internal | External

Use the built-in `Download Excel Template` button.

## Production scaling
Use PostgreSQL, Gunicorn, Nginx/Reverse Proxy, object storage for evidence, HTTPS, scheduled backups, and separate dev/staging/prod environments. For a college-wide deployment, add SSO/LDAP if available and enable password validators/MFA.
