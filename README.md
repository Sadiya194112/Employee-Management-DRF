# Employee-Management-DRF
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
git clone https://github.com/Sadiya194112/Employee-Management-DRF.git
cd yourproject


### 2. **Create and Activate Virtual Environment**
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

### 3. **Install Dependencies**
pip install -r requirements.txt


### 4. **Run Migrations**
python manage.py migrate

### 5. **Create a Superuser**
python manage.py createsuperuser

### 6. **Run a Development Server**
python manage.py runserver










