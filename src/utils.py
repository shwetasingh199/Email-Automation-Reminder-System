from src.renderer import render_template

from src.mailer import Mailer

from src.logger import logger


async def process_email(contact):

    context = {
        "name": contact.name
    }

    html = render_template(
        "reminder_template.html",
        context
    )

    mailer = Mailer()

    result = await mailer.send_email(
        contact.email,
        "Reminder Notification",
        html,
        dry_run=False
    )

    logger.info(
        f"{contact.email} : {result}"
    )

    return result