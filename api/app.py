from fastapi import FastAPI

from src.database import SessionLocal

from src.models import Contact

app = FastAPI()


@app.get("/contacts")

def get_contacts():

    db = SessionLocal()

    contacts = db.query(Contact).all()

    return contacts
