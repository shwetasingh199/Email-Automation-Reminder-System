from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean

from datetime import datetime

from src.database import Base


class Contact(Base):

    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    email = Column(String, unique=True)

    timezone = Column(String, default="Asia/Kolkata")

    unsubscribed = Column(Boolean, default=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Reminder(Base):

    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    recipient_email = Column(String)

    message = Column(String)

    reminder_time = Column(String)

    status = Column(
        String,
        default="PENDING"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class EmailLog(Base):

    __tablename__ = "email_logs"

    id = Column(Integer, primary_key=True)

    recipient = Column(String)

    subject = Column(String)

    status = Column(String)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )

    error_message = Column(
        String,
        nullable=True
    )