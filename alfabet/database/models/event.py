from sqlalchemy import Column, Integer, NVARCHAR, DateTime, func
from alfabet.database import db
from datetime import datetime


class Event(db.Model):
    __tablename__ = 'Event'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(NVARCHAR(255), unique=True)
    location = Column(NVARCHAR(255))
    venue = Column(NVARCHAR(255))
    date = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True),key="createdAt", server_default=func.now(), default=func.now())
    participants_number = Column(Integer,key="participantsNumber")

    def __init__(self, uuid: str,location: str, date: str, participants_number: int, venue: str):
        self.location = location
        self.date = datetime.strptime(date, f"%Y-%m-%dT%H:%M:%SZ")
        self.participants_number = participants_number
        self.venue = venue
        self.uuid = uuid

    def to_json(self) -> dict:
        return {
            "id": self.uuid,
            "location": self.location,
            "venue": self.venue,
            "date": str(self.date),
            "participantsNumber": self.participants_number,
            "creationTime": str(self.created_at)
        }

def find_event_by_uuid(event_uuid: str) -> Event:
    return db.session.query(Event).filter_by(uuid=event_uuid).scalar()
