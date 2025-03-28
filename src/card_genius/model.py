

from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Contact(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    full_name: str
    company: str
    position: str
    phone: str
    email: str

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/contacts/")
def create_contact(contact: Contact):
    with Session(engine) as session:
        session.add(contact)
        session.commit()
        session.refresh(contact)
        return contact