# Sevenwings Portfolio Website

This is a full-stack **personal portfolio website** built with **Django** and jinja templating system, featuring a blog, authentication system, and project showcase. It is deployed on **AWS EC2**, served using **Gunicorn**, **Supervisor**, and **Nginx** for production readiness.

---

## 🔧 Project Structure

The project contains three core Django apps:

### 1. `/`
- Showcases featured projects and skills.
- Includes dynamic sections like services, testimonials, contact, and featured work.
- Acts as the homepage of the website.

### 2. `acct/` (Authentication)
- Handles user authentication (login, registration, logout).
- Uses Django’s built-in authentication system with customization as needed.
- Secures access to the admin and content management.
- Still under development.

### 3. `blog/` 
- A blog system to share thoughts and updates.
- Supports CRUD/Markdown editor for users, detail views, and categorization.

---

## 🚀 Deployment Stack

The site is deployed on an **Ubuntu server (AWS EC2)** and uses:

### 🔹 Gunicorn
A Python WSGI HTTP server used to serve the Django application in production.

### 🔹 Supervisor
A process control system that ensures the Gunicorn server runs continuously, restarts on failure, and starts on boot.

### 🔹 Nginx
Used as a reverse proxy server:
- Serves static and media files.
- Forwards requests to Gunicorn.
- Enhances performance and security.

---

## 🛠️ Setup & Usage (For Developers)

### Clone the Repository
```bash
git clone https://github.com/Sevenwings26/7wings-portfolio.git
cd project
````

### Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

```cmd
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations & Run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🌐 Production Notes

* Static files are collected and served via Nginx.
* Gunicorn is run and monitored by Supervisor.
* The system is hardened with best practices for security and uptime.

---

## 📫 Contact

For collaboration or inquiries, feel free to reach out via the contact form on the site or connect on [LinkedIn](https://www.linkedin.com/in/iyanuarowosola).

---

## License

This project is licensed under the MIT License.

```
