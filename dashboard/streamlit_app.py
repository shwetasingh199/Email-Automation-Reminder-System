import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st
import pandas as pd

from src.database import SessionLocal
from src.models import Contact
from src.models import Reminder

db = SessionLocal()

st.set_page_config(
    page_title="Email Automation System",
    layout="wide"
)

st.title(
    "📧 Email Automation & Reminder System"
)

# =========================
# CONTACTS SECTION
# =========================

st.header("📋 Contacts")

contacts = db.query(Contact).all()

contact_data = []

for contact in contacts:

    contact_data.append({
        "Name": contact.name,
        "Email": contact.email
    })

contact_df = pd.DataFrame(contact_data)

st.dataframe(contact_df)

st.metric(
    "Total Contacts",
    len(contact_df)
)

# =========================
# ADD REMINDER SECTION
# =========================

st.header("⏰ Create Reminder")

title = st.text_input(
    "Reminder Title"
)

recipient = st.text_input(
    "Recipient Email"
)

message = st.text_area(
    "Reminder Message"
)

reminder_time = st.text_input(
    "Reminder Time (Example: 2026-05-18 10:00)"
)

if st.button("Create Reminder"):

    reminder = Reminder(
        title=title,
        recipient_email=recipient,
        message=message,
        reminder_time=reminder_time
    )

    db.add(reminder)

    db.commit()

    st.success("Reminder Created Successfully")

# =========================
# REMINDER DISPLAY
# =========================

st.header("📅 Scheduled Reminders")

reminders = db.query(Reminder).all()

reminder_data = []

for reminder in reminders:

    reminder_data.append({
        "Title": reminder.title,
        "Recipient": reminder.recipient_email,
        "Time": reminder.reminder_time,
        "Status": reminder.status
    })

reminder_df = pd.DataFrame(reminder_data)

st.dataframe(reminder_df)

# =========================
# ANALYTICS
# =========================

st.header("📊 Analytics")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Total Reminders",
        len(reminder_df)
    )

with col2:

    pending = len(
        reminder_df[
            reminder_df["Status"] == "PENDING"
        ]
    ) if not reminder_df.empty else 0

    st.metric(
        "Pending Reminders",
        pending
    )

st.success(
    "System Running Successfully"
)