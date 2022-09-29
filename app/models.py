import enum
from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.sql import func

from .database import Base


class Status(str, enum.Enum):
    NOT_STARTED = 'Not Started'
    WORKING = 'Working'
    PAUSED = 'Paused'
    COMPLETED = 'Completed'


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(Enum(Status), default=Status.NOT_STARTED, nullable=False)
    job_id = Column(Integer, nullable=False)
    file_name = Column(String, nullable=True)

    created = Column(
        DateTime(timezone=True), default=func.current_timestamp(), nullable=False,
    )
    modified = Column(
        DateTime(timezone=True),
        default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        nullable=False,
    )
