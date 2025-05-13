# WSAA-Project - 🛒 Shopping Tracker

###### Lecturer Andrew Beatty at [ATU](https://vlegalwaymayo.atu.ie/).

A full-stack web application built with Flask and Bootstrap to manage your household shopping list.

Easily add, update, and remove shopping items while also managing categories and shops. This project demonstrates your understanding of RESTful APIs, database integration, and dynamic front-end interaction.

[Live demo on PythonAnywhere](https://hugocamachoromero1.pythonanywhere.com/items)

---
## 🧭 Overview

The Shopping Tracker is a web-based application that allows users to manage a shared household shopping list. The project was created for the *Web Services and Applications* module at ATU under the guidance of [Andrew Beatty](https://www.atu.ie/).

It demonstrates key concepts such as:
- Creating and consuming RESTful APIs
- Connecting a Flask backend to an SQLAlchemy database
- Building dynamic front-end interactions using the Fetch API
- Deploying a Python web app on PythonAnywhere

---

## 🎯 Project Objectives

- Design a web application with RESTful API support
- Use a relational database to store and query structured data
- Implement full CRUD functionality via both API and frontend
- Apply Bootstrap to create a responsive and user-friendly interface
- Deploy the solution using PythonAnywhere

---

## 🚀 Features

- 📝 Add, view, and delete shopping items
- 📦 Manage categories and shops dynamically
- ⚙️ Powered by Flask and SQLite
- 💬 Real-time updates using JavaScript fetch API
- 💻 Responsive design with Bootstrap 5

---

## ▶️ Usage

Visit `/items` to access the web interface.  
Use the form to add shopping items, categories, and shops dynamically.  
Items can be deleted with a click and will reflect real-time changes in the list.

---

## 📁 Project Structure



```
WSAA-project/
├── shopping-tracker/
│ ├── app.py # Main Flask application
│ ├── db.py # SQLAlchemy setup
│ ├── models.py # Database models
│ ├── requirements.txt # Python dependencies
│ ├── instance/ # (contains database.db, optional)
│ ├── static/ # (Optional) Static files (e.g., CSS, JS)
│ ├── templates/ # HTML templates (Bootstrap UI)
│ ├── venv/ # Virtual environment (not included in GitHub)
│ └── pycache/ # Compiled Python files (ignored)
├── README.md
├── shopping-tracker.zip # ZIP file for PythonAnywhere deployment
└── .gitignore
```

---

## 🛠️ Installation & Setup

To run the application locally:

1. **Clone this repository:**

   ```bash
   git clone https://github.com/hugcamrom/WSAA-project.git
   cd WSAA-project/shopping-tracker


2. (Optional but recommended) Create and activate a virtual environment:

- On Windows:
```
python -m venv venv
venv\Scripts\activate

```
- On macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate

```

3. Install dependencies:

```
pip install -r requirements.txt

```

4. Start the Flask server:

```
python app.py

```
5. Open your browser and visit:

```
http://127.0.0.1:5000/items

```
---

## 🧰 Tools and Libraries

- [Python 3.12](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Bootstrap 5](https://getbootstrap.com/)
- [PythonAnywhere](https://www.pythonanywhere.com/)

---


