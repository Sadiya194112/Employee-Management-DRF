# Django REST API Project

This is a simple Django REST Framework (DRF) API project with user authentication (JWT-based), token blacklisting, and basic API functionality.

---

## 🚀 Features

- User registration and login
- JWT Authentication with refresh and access tokens
- Token blacklisting on logout
- Auth-protected views using `IsAuthenticated`

---

## 🛠 Requirements

Make sure you have the following installed:

- Python 3.8 or higher
- `pip` (Python package manager)
- `virtualenv` (recommended)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject



python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate


pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver



Authorization: Bearer <access_token>
