import uuid

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()
metadata = Base.metadata


class Events(Base):
    __tablename__ = 'event'
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    title = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False)
    description = Column(String, nullable=True)
