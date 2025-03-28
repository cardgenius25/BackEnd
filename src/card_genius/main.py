from fastapi import FastAPI
from sqlmodel import Session, SQLModel, create_engine, select

from models import Contact

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


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/contacts/")
def create_contact(contact: Contact):
    with Session(engine) as session:
        session.add(contact)
        session.commit()
        session.refresh(contact)
        return contact