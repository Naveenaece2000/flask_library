# 📚 Flask Library Manager

A web-based application to manage a personal book collection. This project was built to demonstrate the **Three-Tier Architecture** pattern using Python, Flask, and SQLite.

## 🚀 Project Overview

This application separates the **Presentation**, **Application Logic**, and **Data Storage** layers, ensuring a clean separation of concerns. It allows users to perform CRUD (Create, Read, Delete) operations on a database.

### The 3-Tier Architecture
*   **Tier 1 (Presentation):** HTML5 & CSS3 (User Interface)
*   **Tier 2 (Application):** Python Flask (Business Logic & Routing)
*   **Tier 3 (Data):** SQLite with SQLAlchemy ORM (Persistent Storage)

---

## 🛠️ Tech Stack

*   **Backend:** Python 3.x, Flask
*   **Database:** SQLite, SQLAlchemy
*   **Frontend:** HTML5, CSS3, Jinja2 Templating
*   **Tools:** VS Code, Git

---

## 📂 Project Structure

```text
flask_library/
│
├── static/
│   └── style.css       # Tier 1: Styling
│
├── templates/
│   └── index.html      # Tier 1: Structure (HTML)
│
├── app.py              # Tier 2 & 3: Application Logic & DB Model
├── library.db          # Tier 3: Database file (Created on first run)
└── README.md           # Documentation
```

---

## ⚡ Setup & Installation
Follow these steps to run the project locally on your machine.

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/flask-library-manager.git
cd hello-jenkins-ci-cd
```
### 2.Install Dependencies
```bash
pip install flask flask-sqlalchemy
```
### 3.Run the Application
Start the Flask server:
```bash
python app.py
```
### 4. Open in Browser
Visit the following URL in your web browser:
```bash

http://127.0.0.1:5000
![image alt](https://github.com/Naveenaece2000/flask_library/blob/e6ccc83648c256f3ab49fde1cf662dc68a0e03d5/Screenshot%20(69).png)
```

# 📖 How to Use
1. Add a Book: Enter the Title and Author in the input fields and click "Add Book".
2. View Library: The book will automatically appear in the list below (fetched from the database).
3. Delete a Book: Click the red "Delete" button next to any book to remove it from the database permanently.

# 🧠 Key Concepts Demonstrated
1. MVC / 3-Tier Architecture: Decoupling the UI from the database.
2. RESTful Routing: Handling HTTP GET and POST requests.
3. ORM (Object Relational Mapping): Using Python classes to interact with the SQL database.
4. Server-Side Rendering: Using Jinja2 to inject data into HTML before sending it to the client.









