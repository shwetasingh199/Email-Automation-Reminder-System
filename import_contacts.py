from src.database import SessionLocal

from src.csv_loader import import_contacts

db = SessionLocal()

import_contacts(
    "data/contacts.csv",
    db
)