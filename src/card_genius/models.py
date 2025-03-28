from sqlmodel import Field, SQLModel

class Contact(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    full_name: str
    company: str
    position: str
    phone: str
    email: str

