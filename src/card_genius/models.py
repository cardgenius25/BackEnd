from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Contact(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    full_name: str
    company: str
    position: str
    phone: str
    email: str


app = FastAPI()




@app.post("/contacts/")
def create_contact(contact: Contact):
    with Session(engine) as session:
        session.add(contact)
        session.commit()
        session.refresh(contact)
        return contact