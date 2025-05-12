# Django User Account Management

This is a mini Django project focused on implementing user account functionality. It includes registration, login/logout, profile viewing, and profile editing (including profile image upload).

## 📁 Features

- ✅ User registration and login
- ✅ Profile page with user information
- ✅ Profile editing (username, email, password, and profile image)
- ✅ Custom user form and validation
- ✅ Authentication and session management
- ✅ Bootstrap-based responsive UI

## 🔧 Tech Stack

- Python 3.10+
- Django 4.x
- SQLite3 (default Django DB)
- HTML/CSS (Bootstrap)

## 🚀 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/django-user-account.git
cd django-user-account
```

2. **Create a virtual environment and activate it**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Run the development server**

```bash
python manage runserver
```
Visit http://127.0.0.1:8000 in your browser.


## 🧩 App Structure

```graphql
accounts/
├── forms.py           # Custom user forms
├── models.py          # Custom user model or profile (if used)
├── urls.py            # URL patterns for accounts
├── views.py           # View functions
├── templates/
│   └── accounts/
│       ├── register.html
│       ├── login.html
│       ├── profile.html
│       └── edit_profile.html
```

## 📄 License
This project is open-source and available under the MIT License.


## 📬 Contact
For questions or suggestions, feel free to contact m.hesam.norouzi@gmail.com or visit hesamnorouzi.ir .