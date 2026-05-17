import pandas as pd

from email_validator import validate_email
from email_validator import EmailNotValidError

from src.models import Contact


def import_contacts(csv_path, db):

    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():

        try:

            valid = validate_email(
                row["email"]
            )

            email = valid.email

            existing = db.query(Contact).filter(
                Contact.email == email
            ).first()

            if not existing:

                contact = Contact(
                    name=row["name"],
                    email=email
                )

                db.add(contact)

        except EmailNotValidError:

            print(
                f"Invalid Email Skipped: {row['email']}"
            )

    db.commit()

    print("Contacts Imported Successfully")