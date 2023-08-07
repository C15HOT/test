from datetime import datetime
from pydantic import BaseModel


class EventsSchema(BaseModel):
    title: str
    description: str
    datetime: datetime