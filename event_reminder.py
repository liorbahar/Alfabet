
from time import sleep
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta, timezone
from alfabet.database.models.event import Event
import threading
import pytz

engine = create_engine("mssql+pyodbc://localhost/alfabet?driver=ODBC+Driver+17+for+SQL+Server")
session_factory = sessionmaker(bind=engine)
session = session_factory()

def notify(event: Event, *args, **kwargs):
    print(f"event start at location {event.location}")

class EventReminder:

    def listen(self):
        while True:
            events = session.query(Event).filter(Event.date >= datetime.now() + timedelta(minutes=30),
                    Event.date <= datetime.now() + timedelta(minutes=60)).all()
            for event in events:
                self.__schedule_event(event)
            sleep(1800)
    
    def __schedule_event(self, event: Event):
        israel_timezone = pytz.timezone('Asia/Jerusalem')
        parsed_datetime = event.date.replace(tzinfo=None)
        parsed_datetime_israel = israel_timezone.localize(parsed_datetime)
        parsed_datetime_utc = parsed_datetime_israel.astimezone(pytz.utc)

        scheduled_datetime = parsed_datetime_utc - timedelta(minutes=30)
        time_difference = (scheduled_datetime - datetime.now(timezone.utc)).total_seconds()
        timer = threading.Timer(time_difference, notify, args=[event])
        timer.start()


if __name__ == "__main__":
    reminder = EventReminder()
    reminder.listen()
