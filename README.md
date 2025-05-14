# WSAA-Project - 🛒 Shopping Tracker


<p align="center">
  <a href="https://hugocamachoromero1.pythonanywhere.com/items">
    <img src="https://img.shields.io/badge/LIVE%20APP-PythonAnywhere-brightgreen?style=for-the-badge&logo=python" alt="Live App">
  </a>
</p>

---

## 🧭 Overview

The Shopping Tracker is a web-based application that allows users to manage a shared household shopping list. The project was created for the *Web Services and Applications* module at Atlantic Technological University under the guidance of
lecturer [Andrew Beatty](https://www.atu.ie/).

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
- 🧺 Create and delete custom categories and shops directly from the UI
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

```bash

WSAA-project/
├── shopping-tracker/
│   ├── app.py              # Main Flask application
│   ├── db.py               # SQLAlchemy setup
│   ├── models.py           # Database models
│   ├── requirements.txt    # Python dependencies
│   ├── instance/           # (contains database.db, optional)
│   ├── static/             # Static files (e.g., CSS, JS)
│   ├── templates/          # HTML templates (Bootstrap UI)
│   ├── venv/               # Virtual environment (not included in GitHub)
│   └── __pycache__/        # Compiled Python files (ignored)
├── README.md
├── shopping-tracker.zip   # ZIP file for PythonAnywhere deployment
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

3.Install dependencies:

```

pip install -r requirements.txt

```

4.Start the Flask server:

```

python app.py

```

5.Open your browser and visit:

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

## 📚 Documentation and Insights

Throughout development, the project evolved from a basic inventory tracker into a more intuitive and styled application that supports:

- Adding items, shops, and categories through the UI
- Populating dropdown menus dynamically from the database
- Dropdown menus enhanced with deletion options for categories and shops
- Handling backend logic with clean, modular Python files (`app.py`, `models.py`, `db.py`)
- Simple deployment with minimal changes to Flask's default structure

---

## 🔗 Sources and References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy Docs](https://flask-sqlalchemy.palletsprojects.com/)
- [PythonAnywhere Help](https://help.pythonanywhere.com/)
- [Bootstrap Docs](https://getbootstrap.com/)
- My class labs and assignments from the WSAA module

---

## 🧠 AI Assistance

This project was developed using:

- [GitHub Copilot](https://github.com/features/copilot) for real-time code suggestions inside Visual Studio Code.

- [ChatGPT](https://chat.openai.com/) for guidance, error troubleshooting, RESTful API design ideas, deployment tips, and README structuring.

All decisions and customisations were made and reviewed by the author. AI tools were used to support the learning process, not to replace it.

---

## 📌 Additional Resources

- [Live App](https://hugocamachoromero1.pythonanywhere.com/items)
- [GitHub Repository](https://github.com/hugcamrom/WSAA-project)

---

## 📄 Licence

This project is provided for educational purposes as part of an academic submission. Not licenced for commercial reuse.

---

✅ Status
This project is complete and live. Additional enhancements (e.g. meal planning or user accounts) are ideas for future development.

🌐 Deployment Notes
Deployed on PythonAnywhere.
The ZIP file shopping-tracker.zip was uploaded, extracted, and configured as a WSGI app with a working virtual environment.

🙏 Acknowledgements
This project was developed for the Web Services and Applications module as part of my coursework. It reflects RESTful API practices, front-end/back-end integration, and live deployment experience.

Big thanks to PythonAnywhere for free hosting and to everyone who supported the learning process.

---

## 🏷️ Tags

 #WSAA #Flask #Python #SQLite #WebDevelopment #Bootstrap #API

---

### 👤 Author

Hugo Camacho Romero

Student at [ATU](https://www.atu.ie/)

Course: WEB SERVICES AND APPLICATIONS

---
