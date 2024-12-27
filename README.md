# 📇 Django Contacts List App

A contact management web application built with Django that allows users to create, read, update, and delete (CRUD) contact entries.

## 🚀 Features

- Add, edit, and delete contact information.
- Search and filter contacts.
- User authentication and authorization.
- Responsive design for mobile and desktop views.

## 🛠️ Technologies Used

- **Backend:** Django 5.1.4, Python
- **Frontend:** HTML, CSS
- **Database:** SQLite (default Django database)

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Shervinfr/Django-Contacts-List-App.git
   cd Django-Contacts-List-App

    Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Start the development server:

python manage.py runserver

Open your browser and visit:

    http://127.0.0.1:8000/

📂 Project Structure

contactlist/
├── manage.py          # Django management script
├── contactlist/
│   ├── settings.py    # Project settings
│   ├── urls.py        # URL mappings
│   ├── wsgi.py        # WSGI config
├── contacts/
│   ├── models.py      # Database models
│   ├── views.py       # Application views
│   ├── urls.py        # Application URLs
│   ├── templates/     # HTML templates
└── static/            # Static files (CSS, JS, Images)
