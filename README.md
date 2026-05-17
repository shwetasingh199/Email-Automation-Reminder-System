# 📧 Email Automation & Reminder System

An industry-level Email Automation & Reminder System built using Python, FastAPI, Streamlit, SQLite, SMTP, and APScheduler.

This project automates reminder scheduling, email notifications, status tracking, and dashboard monitoring — similar to productivity and communication systems used by startups, HR teams, operations teams, educators, and business automation platforms.

---

# 🚀 Project Overview

The Email Automation & Reminder System is designed to automate repetitive communication workflows such as:

- Meeting reminders
- Task notifications
- Project deadline alerts
- Webinar reminders
- Payment follow-ups
- Team communication alerts
- Productivity notifications

The system allows users to:

✅ Create reminders  
✅ Schedule automated emails  
✅ Send real-time reminder notifications  
✅ Track reminder status  
✅ Validate real email addresses  
✅ View analytics in dashboard  
✅ Monitor sent and failed reminders  

This project simulates a real-world automation platform using Gmail SMTP, SQLite database, and Streamlit dashboard.

---

# 🎯 Industry Relevance

This project is highly relevant for:

- Python Developer Roles
- Backend Developer Roles
- Automation Engineer Roles
- Productivity Software Development
- HR Automation Systems
- CRM Automation
- Operations Management Tools
- Admin Automation Platforms
- SaaS Product Development

Real companies use similar systems for:

- Customer follow-ups
- Employee reminders
- Interview scheduling
- Marketing email automation
- Event notifications
- Payment reminders
- Productivity tracking

---

# 🧠 Problem Statement

Organizations waste time manually sending repetitive emails and reminders.

This project solves that problem by automating:

- reminder scheduling
- email delivery
- contact management
- notification tracking
- productivity communication workflows

---

# ✨ Features

## ✅ Contact Management

- Import contacts from CSV
- Real email validation
- Duplicate prevention
- Contact dashboard

## ✅ Reminder System

- Create reminders from UI
- Schedule reminders
- Real-time email reminders
- Pending/Sent/Failed tracking

## ✅ Email Automation

- SMTP-based email delivery
- Gmail integration
- HTML email support
- Dynamic message generation

## ✅ Dashboard

- Streamlit interactive dashboard
- Contact analytics
- Reminder analytics
- Reminder monitoring

## ✅ Notification System

- Desktop popup reminders
- Real-time alerts
- Productivity notifications

## ✅ Logging & Monitoring

- Reminder status tracking
- Sent/Failed logs
- Error handling

---

# 🏗️ System Architecture

```text
User Dashboard
       ↓
Reminder Creation
       ↓
SQLite Database
       ↓
Scheduler Engine
       ↓
SMTP Email Service
       ↓
Recipient Email
       ↓
Status Tracking
       ↓
Dashboard Analytics
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core backend logic |
| FastAPI | REST API |
| Streamlit | Dashboard UI |
| SQLite | Database |
| SMTP | Email sending |
| APScheduler | Reminder scheduling |
| SQLAlchemy | ORM |
| Pandas | CSV handling |
| Plyer / Win10Toast | Desktop notifications |
| dotenv | Environment variables |

---

# 📂 Project Structure

```text
Email-Automation-Reminder-System/
│
├── api/
│   ├── __init__.py
│   └── app.py
│
├── src/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── scheduler.py
│   ├── mailer.py
│   ├── csv_loader.py
│   ├── notifications.py
│   └── utils.py
│
├── dashboard/
│   └── streamlit_app.py
│
├── data/
│   └── contacts.csv
│
├── templates/
│
├── outputs/
│
├── logs/
│
├── images/
│
├── worker.py
├── main.py
├── import_contacts.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/Email-Automation-Reminder-System.git
```

---

## 2️⃣ Open Project Folder

```bash
cd Email-Automation-Reminder-System
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create `.env` file:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_gmail_app_password
```

⚠️ Never upload your real `.env` file to GitHub.

---

# 📧 Gmail App Password Setup

Enable:

- Google 2-Step Verification
- Gmail App Password

Generate App Password from:

```text
Google Account → Security → App Passwords
```

Use generated password in `.env`.

---

# ▶️ How To Run

## Step 1 — Create Database

```bash
python main.py
```

---

## Step 2 — Import Contacts

```bash
python import_contacts.py
```

---

## Step 3 — Start FastAPI Server

```bash
uvicorn api.app:app --reload
```

---

## Step 4 — Start Worker Scheduler

```bash
python worker.py
```

---

## Step 5 — Start Streamlit Dashboard

```bash
streamlit run dashboard/streamlit_app.py
```

---

# 📊 Dashboard Features

The dashboard provides:

✅ Contact Management  
✅ Reminder Creation  
✅ Reminder Analytics  
✅ Pending Reminder Monitoring  
✅ Real-Time Status Tracking  

---

# 📬 Real Email Reminder Flow

```text
Create Reminder
      ↓
Reminder Saved
      ↓
Scheduler Checks Time
      ↓
SMTP Sends Email
      ↓
Desktop Notification Triggered
      ↓
Status Updated to SENT
```

---

# 📸 Recommended Screenshots

## Dashboard UI
  <img width="1855" height="570" alt="Screenshot 2026-05-17 130007" src="https://github.com/user-attachments/assets/49159912-d2b0-4552-beb9-412499ff4735" />

## Reminder Creation
  <img width="1810" height="812" alt="Screenshot 2026-05-17 130024" src="https://github.com/user-attachments/assets/9bbd1c1b-401b-4cf6-b58a-29697dbe9166" />
  
## Scheduled Reminders
<img width="1812" height="846" alt="Screenshot 2026-05-17 130039" src="https://github.com/user-attachments/assets/dbaea7f4-ed10-407f-bcd2-fc181f750562" />

## Desktop Notification
 <img width="1003" height="756" alt="Screenshot 2026-05-17 130628" src="https://github.com/user-attachments/assets/616f0d08-6e6b-42af-8e6e-84c8ed579689" />

## Real Email Received
<img width="1802" height="631" alt="Screenshot 2026-05-17 131211" src="https://github.com/user-attachments/assets/8a80dd3e-379e-46a0-b69e-8ff0af600cb1" />


---

# 🧪 Sample Contacts CSV

```csv
name,email
Shweta Singh,example@gmail.com
John Doe,johndoe@gmail.com
```

---

# 📈 Future Enhancements

- JWT Authentication
- Docker Deployment
- PostgreSQL Support
- Redis Queue
- Twilio SMS Reminders
- AI Smart Scheduling
- Google Calendar Integration
- Multi-user Support
- Role-Based Access

---

# 🔒 Security Practices

✅ Environment Variables  
✅ App Password Authentication  
✅ Input Validation  
✅ Email Validation  
✅ Duplicate Prevention  

---

# 🧠 Learning Outcomes

Through this project, I learned:

- Backend Development
- REST API Development
- Email Automation
- Task Scheduling
- Database Management
- Dashboard Development
- SMTP Integration
- Python Project Architecture
- Environment Variable Security
- Real-world Automation Workflows

---

# 💼 Resume / Portfolio Value

This project demonstrates skills in:

- Python Backend Development
- Automation Engineering
- Productivity Systems
- API Integration
- Scheduling Systems
- Database Design
- Real-Time Notification Systems
- Full Project Architecture

---

# 👩‍💻 Author

Shweta Singh

B.Tech Electronics & Computer Engineering Student

Passionate about:
- Python Development
- Automation Systems
- Backend Engineering
- AI & Productivity Tools

---

# ⭐ GitHub Topics

```text
python
fastapi
streamlit
automation
email-automation
scheduler
smtp
backend
sqlite
productivity
apscheduler
```

---

# 🙌 Acknowledgements

Inspired by real-world automation platforms used in:

- HR Systems
- Productivity Tools
- CRM Platforms
- Startup Operations
- Admin Workflow Automation
- SaaS Communication Systems
