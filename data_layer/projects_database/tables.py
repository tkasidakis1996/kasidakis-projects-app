from sqlmodel import SQLModel, Field

from datetime import date

class Project(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    technologies_used: str
    start_date: date
    end_date: date
