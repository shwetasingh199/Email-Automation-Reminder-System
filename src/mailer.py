import os

import aiosmtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()


class Mailer:

    def __init__(self):

        self.host = os.getenv("SMTP_HOST")

        self.port = int(os.getenv("SMTP_PORT"))

        self.username = os.getenv("SMTP_USER")

        self.password = os.getenv("SMTP_PASS")

    async def send_email(
        self,
        to_email,
        subject,
        html_content,
        dry_run=True
    ):

        if dry_run:

            print(f"[DRY RUN] Email sent to {to_email}")

            return {
                "success": True,
                "message": "Dry Run Success"
            }

        message = MIMEMultipart()

        message["From"] = self.username

        message["To"] = to_email

        message["Subject"] = subject

        message.attach(
            MIMEText(html_content, "html")
        )

        try:

            smtp = aiosmtplib.SMTP(
                hostname=self.host,
                port=self.port,
                use_tls=True
            )

            await smtp.connect()

            await smtp.login(
                self.username,
                self.password
            )

            await smtp.send_message(message)

            await smtp.quit()

            return {
                "success": True,
                "message": "Email Sent"
            }

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }