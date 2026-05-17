from apscheduler.schedulers.asyncio import AsyncIOScheduler

from datetime import datetime

from src.database import SessionLocal

from src.models import Reminder

from src.mailer import Mailer

from src.notifications import show_notification

scheduler = AsyncIOScheduler()


async def check_reminders():

    db = SessionLocal()

    reminders = db.query(Reminder).filter(
        Reminder.status == "PENDING"
    ).all()

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M"
    )

    mailer = Mailer()

    for reminder in reminders:

        if reminder.reminder_time == current_time:

            result = await mailer.send_email(
                reminder.recipient_email,
                reminder.title,
                f"""
                <h2>Reminder Notification</h2>

                <p>{reminder.message}</p>
                """,
                dry_run=False
            )

            if result["success"]:

               reminder.status = "SENT"

               show_notification(
                   reminder.title,
                   reminder.message
               )

            else:

                reminder.status = "FAILED"

    db.commit()

    print("Reminder Check Completed")


scheduler.add_job(
    check_reminders,
    "interval",
    minutes=1
)